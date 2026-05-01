import asyncio
import sys
from argparse import Namespace
from enum import Enum
from CommonClient import CommonContext
from typing import TYPE_CHECKING, Any
from random import randint

from CommonClient import logger, server_loop
from NetUtils import ClientStatus

from ..Game.events import LocationClearedEvent, VictoryEvent, DeathEvent, DisconnectEvent


if TYPE_CHECKING:
    import kvui



class ConnectionStatus(Enum):
    NOT_CONNECTED = 0
    SCOUTS_NOT_SENT = 1
    SCOUTS_SENT = 2
    GAME_RUNNING = 3

class Nothing_Archipelago_Context(CommonContext):
    game = "nothing_archipelago"
    items_handling = 0b111

    client_loop: asyncio.Task[None]

    last_connected_slot: int | None = None

    slot_data: dict[str, Any]
    goal: int = 1800
    shop_upgrades: bool = True
    shop_colors: bool = True
    shop_music: bool = True
    shop_sounds: bool = True
    gift_coins: bool = True
    milestone_interval: int = 120
    timecap_interval: int = 120
    Starting_coin_count: int = 10
    Death_link: bool = False
    Death_link_mercy: int =100
    Time_dilation: int = 1
    connection_status: ConnectionStatus = ConnectionStatus.NOT_CONNECTED

    highest_processed_item_index: int = 0
    queued_locations: list[int]

    def __init__(self,data,archui,server_address: str | None = None, password: str | None = None) -> None:
        super().__init__(server_address, password)
        self.data = data
        self.password = self.data.inputs[3]
        self.archui = archui
        self._condition = asyncio.Condition()
        self.queued_locations = []
        self.items_received = []
        self.slot_data = {}
        self.needsync = 0
        self.needdeath = False
        self.needdisconnect = False
        self.updatedeathlink = False
        

    async def server_auth(self, password_requested: bool = False) -> None:
        if password_requested and not self.password:
            
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect(game=self.game)

    def handle_connection_loss(self, msg: str) -> None:
        super().handle_connection_loss(msg)

    async def connect(self, address: str | None = None) -> None:
        #self.ui.switch_to_regular_tab()
        await super().connect(address)

    async def nothing_archipelago_loop(self) -> None:
        while not self.exit_event.is_set():
            
            
            await asyncio.sleep(0.1)



            try:
                if self.updatedeathlink:
                    await self.on_deathlink_toggle()
                if self.needsync == 1:
                    await self.send_msgs([{"cmd": "Sync"}])
                    self.needsync = 0
                self.handle_game_events()
                while self.queued_locations:
                    location = self.queued_locations.pop(0)
                    self.locations_checked.add(location)
                    await self.check_locations({location})

                new_items = self.items_received[self.highest_processed_item_index :]
                if new_items:
                    for _ in new_items:
                        self.highest_processed_item_index += 1
                    self.archui.updateitems(self.data,self.items_received)

                if self.needdisconnect:
                    self.data.clientexists = 0
                    self.exit_event.set()
                #print(self.needdeath)
                if self.Death_link and self.needdeath:
                    #print("death")
                    player = self.player_names[self.slot] if self.slot is not None else "Nothing"
                    y = randint(1,10)
                    self.needdeath = False
                    if y == 1:
                        death_text = player + " tried to have fun"
                    elif y == 2:
                        death_text = player + " thought they were playing a real game"
                    elif y == 3:
                        death_text = player + " got bored of waiting"
                    elif y == 4:
                        death_text = player + " can't sit still"
                    elif y == 5:
                        death_text = player + " forgot how to play"
                    elif y == 6:
                        death_text = player + " felt that the check was more important"
                    elif y == 7:
                        death_text = player + " enjoys the suffering of others"
                    elif y == 8:
                        death_text = player + " stopped being afk"
                    elif y == 9:
                        death_text = player + " didn't set the mercy high enough"
                    else:
                        death_text = player + " did something"
                    await super().send_death(death_text)
                    

                if self.checked_locations != self.locations_checked:
                    self.locations_checked = self.checked_locations
                    self.archui.checklocations(self.data,self.checked_locations)


                if self.data.goalled and not self.finished_game:
                    await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                    self.finished_game = True
            except Exception as e:
                logger.exception(e)

            await asyncio.sleep(0.1)

    def on_package(self, cmd: str, args: dict[str, Any]) -> None:
        if cmd == "ConnectionRefused":
            #idk
            test = 1

        if cmd == "Connected":
            if self.connection_status == ConnectionStatus.GAME_RUNNING:
                # In a connection loss -> auto reconnect scenario, we can seamlessly keep going
                return

            self.last_connected_slot = self.slot

            self.connection_status = ConnectionStatus.NOT_CONNECTED  # for safety, it will get set again later
            self.checked_locations = set(args["checked_locations"])
            self.archui.checklocations(self.data,self.checked_locations)
            self.needsync = 1
            self.slot_data = args["slot_data"] 
            self.goal = self.slot_data["goal"]
            self.shop_upgrades = self.slot_data["shop_upgrades"]
            self.shop_colors = self.slot_data["shop_colors"]
            self.shop_music = self.slot_data["shop_music"]
            self.shop_sounds = self.slot_data["shop_sounds"]
            self.gift_coins = self.slot_data["gift_coins"]
            self.milestone_interval = self.slot_data["milestone_interval"]
            self.timecap_interval = self.slot_data["timecap_interval"]
            self.Starting_coin_count = self.slot_data["Starting_coin_count"]
            self.Death_link = self.slot_data["Death_link"]
            self.Death_link_mercy = self.slot_data["Death_link_mercy"]
            self.Time_dilation = self.slot_data["Time_dilation"]
            
            self.data.update_arch_settings(self.goal, self.shop_upgrades, self.shop_colors, self.shop_music, self.shop_sounds,
                                      self.gift_coins, self.milestone_interval, self.timecap_interval, self.Starting_coin_count,
                                      self.Death_link, self.Death_link_mercy, self.Time_dilation)
            self.highest_processed_item_index = 0
            self.data.needload = True
            self.data.blockload = True
            print(self.Death_link)
            if self.Death_link:
                self.updatedeathlink = True
            

    async def disconnect(self, *args: Any, **kwargs: Any) -> None:
        self.finished_game = False
        self.locations_checked = set()
        self.connection_status = ConnectionStatus.NOT_CONNECTED
        await super().disconnect(*args, **kwargs)

    def handle_game_events(self) -> None:
        if self.data is None:
            return

        while self.data.queued_events:
            event = self.data.queued_events.pop(0)

            if isinstance(event, LocationClearedEvent):
                self.queued_locations.append(event.location_id)
                continue

            if isinstance(event, VictoryEvent):
                continue

            if isinstance(event, DeathEvent):
                if self.Death_link:
                    self.needdeath = True

            if isinstance(event, DisconnectEvent):
                self.needdisconnect = True

    def trigger_server(self,server_address, password):
        super().__init__(server_address, password)

    async def on_deathlink_toggle(self):
        await super().update_death_link(self.Death_link)

    def on_deathlink(self, data):
        if self.Death_link:
            self.data.recievedeath = True
            self.data.deathtext = data.get("cause", "")
            super().on_deathlink(data)



async def main(data,archui) -> None:
    ctx = Nothing_Archipelago_Context(data,archui,data.inputs[0]+":"+data.inputs[1],data.inputs[3])
    ctx.auth = data.inputs[2]
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")


    ctx.client_loop = asyncio.create_task(ctx.nothing_archipelago_loop(), name="Client Loop")

    await ctx.exit_event.wait()
    await ctx.shutdown()


def launch() -> None:
    from .launch import launch_nothing_archipelago

    launch_nothing_archipelago()


if __name__ == "__main__":
    launch(*sys.argv[1:])