from dataclasses import dataclass
    

@dataclass
class Event:
    pass

@dataclass
class LocationClearedEvent(Event):
    location_id: int


@dataclass
class VictoryEvent(Event):
    pass

@dataclass
class DeathEvent(Event):
    pass

@dataclass
class DisconnectEvent(Event):
    pass