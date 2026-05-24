from .trivia_questions import define_questions
from .positions import define_locations

class Data:
    def __init__(self,ui, goal, shop_upgrades, shop_colors, shop_music, shop_sounds, gift_coins, milestone_interval, timecap_interval,
                           Starting_coin_count, Death_link, Death_link_mercy, Time_dilation, enable_trivial_pursuit, enable_trivia_questions):
        self.ui = ui
        self.milestoneint = milestone_interval
        self.archipelagoactive = False
        self.goal = goal
        self._milestonesforce = 1
        self._points = Starting_coin_count
        self.timecapint = timecap_interval
        self.randoopts = [False for _ in range (4)]
        self.enabletrivialpursuit = enable_trivial_pursuit
        self.enabletriviaquestion = enable_trivia_questions

        self.WINDOW_WIDTH = 1920
        self.WINDOW_HEIGHT = 1080

        self.queued_events = []
        self.connected = 0
        self.activeinput = 3
        self.inputs = [0 for _ in range(4)]
        self.inputs[0] = "Archipelago.gg"
        self.inputs[1] = "25655"
        self.inputs[2] = "Slot Name"
        self.inputs[3] = ""
        
        self.randoopts[0] = shop_upgrades
        self.randoopts[1] = shop_colors
        self.randoopts[2] = shop_music
        self.randoopts[3] = shop_sounds

        self.devcount = 0
        self.timescale = Time_dilation
        self._speedups = 0
        self.timescaledev = 1
        self.devmode = 0
        self.giftcoins = gift_coins
        self.giftedcoins = Starting_coin_count
        self.startingcoincount = Starting_coin_count
        self.spentcoins = 0

        self.blocksave = False
        self.blockload = False
        self.needload = False
        self.earnedcoins = 0
        self.ddelay = 0
        self.clientexists = 0
        self.deathtext = ""
        self.recievedeath = False
        self.deathlink = Death_link
        self.deathlinkcount = 0
        self.deathlinkmercy = Death_link_mercy
        self.needsync = 0
        self.connected = 0
        self._maxtime = 0
        self._currenttime = 0
        #0 = main menu, 1 = click to start, 2 = timer active, 3 = you died, -1 = archipelago connect menu, -2 = goal menu, -3 = delete save menu, -4 = trivial pursuit
        self._playingstate = 0
        self._shopstate = 0
        self._peaktime = 0
        self._totaltime = 0
        self._timecaps = 1
        self._forcestatechange = 0
        self._timecap = self.timecapint
        self._digits = 1
        self._colorselect = 0
        self._musicselect = 11
        self.currentsong = self._musicselect
        self.goalled = False
        self.leave = 0
        self._milestones = [[0 for _ in range(4)] for _ in range (86400)]
        self.checked_locations_player: set[int] = []
        self.checked_locations: set[int] = []
        self.missing_locations: list[int] = []
        
        #self.names[shop item][shop state]
        #[x][0] = upgrades
        #[x][1] = colors
        #[x][2] = music
        #[x][3] = colors
        self.names = [[0 for _ in range(4)] for _ in range (11)]
        self.names[0][0] = "Auto-restart      : "
        self.names[1][0] = "Auto-milestone   : "
        self.names[2][0] = "Unlock next Digit : "
        self.names[3][0] = "Unlock next Digit : "
        self.names[4][0] = "Unlock next Digit : "
        self.names[5][0] = "Unlock next Digit : "
        self.names[6][0] = "Unlock next Digit : "
        self.names[7][0] = "Unlock next Digit : "
        self.names[8][0] = "Unlock Trivial Pursuit: "
        self.names[9][0] = ""
        self.names[10][0] = ""
        self.names[0][1] = "Gray       : "
        self.names[1][1] = "Blue        : "
        self.names[2][1] = "Green     : "
        self.names[3][1] = "Pink        : "
        self.names[4][1] = "White     : "
        self.names[5][1] = "Black      : "
        self.names[6][1] = "Orange  : "
        self.names[7][1] = "Yellow    : "
        self.names[8][1] = "Purple   : "
        self.names[9][1] = "Cyan      : "
        self.names[10][1] = "Matrix     : "
        self.names[0][2] = "song1    : "
        self.names[1][2] = "song2   : "
        self.names[2][2] = "song3   : "
        self.names[3][2] = "song4   : "
        self.names[4][2] = "song5   : "
        self.names[5][2] = "song6   : "
        self.names[6][2] = "song7   : "
        self.names[7][2] = "song8   : "
        self.names[8][2] = "song9   : "
        self.names[9][2] = "song10 : "
        self.names[10][2] = ""
        self.names[0][3] = "Sound1    : "
        self.names[1][3] = "Sound2   : "
        self.names[2][3] = "Sound3   : "
        self.names[3][3] = "Sound4   : "
        self.names[4][3] = "Sound5   : "
        self.names[5][3] = "Sound6   : "
        self.names[6][3] = "Sound7   : "
        self.names[7][3] = "Sound8   : "
        self.names[8][3] = "Sound9   : "
        self.names[9][3] = "Sound10 : "
        self.names[10][3] = ""
        #self.colors[color index][text/background color]
        #[x][0] = background color
        #[x][1] = text color
        self.colors =[[0 for _ in range (2)] for _ in range (11)]
        self.colors[0][0] = (100,100,100)
        self.colors[0][1] = (255,255,255)
        self.colors[1][0] = (0,0,255)
        self.colors[1][1] = (255,255,255)
        self.colors[2][0] = (35,140,35)
        self.colors[2][1] = (255,255,255)
        self.colors[3][0] = (255,0,255)
        self.colors[3][1] = (255,255,255)
        self.colors[4][0] = (255,255,255)
        self.colors[4][1] = (0,0,0)
        self.colors[5][0] = (0,0,0)
        self.colors[5][1] = (255,255,255)
        self.colors[6][0] = (255,140,0)
        self.colors[6][1] = (255,255,255)
        self.colors[7][0] = (255,255,0)
        self.colors[7][1] = (0,0,0)
        self.colors[8][0] = (140,0,140)
        self.colors[8][1] = (255,255,255)
        self.colors[9][0] = (0,140,140)
        self.colors[9][1] = (255,255,255)
        self.colors[10][0] = (0,0,0)
        self.colors[10][1] = (40,200,40)
        #self.milestones[milestone index][data]
        #[x][0] = milestone time value
        #[x][1] = is milestone collected
        #[x][2] = archipelago location value
        for x in range(86400):
            self._milestones[x][0] = (x+1)*self.milestoneint
            self._milestones[x][2] = x+1
        #self.shop[shop state][shop item][data]
        #[x][y][0] = shop item text
        #[x][y][1] = is shop item purchased
        #[x][y][2] = is shop item recieved
        #[x][y][3] = item cost
        #[x][y][4] = archipelago location value
        self._shop = [[[0 for _ in range (5)] for _ in range (11)] for _ in range (4)]
        self._shop[1][0][1] = 1
        self._shop[1][0][2] = 1
        for x in range (4):
            for y in range (10):
                if x == 0 and y > 1:
                    self._shop[x][y][3] = 1
                else:
                    self._shop[x][y][3] = 2
                self._shop[x][y][4] = 86400+(x*10)+(y+1)
        
        self._shop[0][9][3] = ""
        #self.questions[card][question][answers or line or result][line/answer index]
        self.questions = [[[[0 for _ in range (4)] for _ in range (3)] for _ in range (6)] for _ in range (300)]
        define_questions(self)
        #self.answered_questions[card][question][data]
        #[x][y][0] = has question been answered
        #[x][y][1] = archipelago location value
        self.answered_questions = [[[0 for _ in range(2)] for _ in range(6)] for _ in range(300)]
        for x in range (300):
            for y in range(6):
                self.answered_questions[x][y][1] = 87000 + x + (y * 300)
        self.trivia_selected_team = False
        self.trivia_team = 0
        self.trivia_question = 0
        self.trivia_color = 0
        self.trivia_shown_color = 0
        self.positions = [[0 for _ in range (2)] for _ in range(73)]
        define_locations(self)
        self.trivia_location = 0
        self.trivia_last_direction = 0
        self.trivia_roll = 0
        self.trivia_moves = 0
        self.trivia_goal = False
        self.trivia_intro = False
        self.trivia_last_location = 0
        self.trivia_move = False
        self.trivia_need_direction = True
        self.trivia_need_question = False
        self.trivia_last_question = False
        self.trivia_question_charge = True
        self.trivia_used_blue = False
        self.trivia_used_green = False
        self.trivia_enabled = True
        self.trivia_penalty = 0
        #0 = intro & team select, 1 = roll, 2 = start move, 3 = moving, 4 = question select and answer, 5 = penalty, 6 =victory
        self.trivia_state = 0
        #self.trivia_wedges[color][data]
        #[x][0] = has wedges been earned
        #[x][1] = archipelago location value
        self.trivia_wedges = [[0 for _ in range(3)] for _ in range(6)]
        for x in range (6):
            self.trivia_wedges[x][1] = 86441 + x
            self.trivia_wedges[x][2] = True
        self.trivia_abilities = [["" for _ in range(7)] for _ in range(10)]
        for x in range (10):
            self.trivia_abilities[x][2] = "Pink: see card number"
            self.trivia_abilities[x][3] = "Yellow: see questions for other colors"
            self.trivia_abilities[x][4] = "Purple: return to center of board instead of rolling"
            self.trivia_abilities[x][6] = "Orange: reduce penalties by half"
        self.trivia_abilities[0][0] = "Teku"
        self.trivia_abilities[0][1] = "Blue: add +1 to dice roll"
        self.trivia_abilities[0][5] = "Green: add -1 to dice roll"
        self.trivia_abilities[1][0] = "Metal Maniacs"
        self.trivia_abilities[1][1] = "Blue: set roll to 1"
        self.trivia_abilities[1][5] = "Green: set roll to 5"
        self.trivia_abilities[2][0] = "Silencerz"
        self.trivia_abilities[2][1] = "Blue: double dice roll"
        self.trivia_abilities[2][5] = "Green: half dice roll"
        self.trivia_abilities[3][0] = "Racing Drones"
        self.trivia_abilities[3][1] = "Blue: you can change directions during movement"
        self.trivia_abilities[3][5] = "Green: instead of moving, switch sides of the board"
        self.trivia_abilities[4][0] = "CLYP"
        self.trivia_abilities[4][1] = "Blue: triple dice roll"
        self.trivia_abilities[4][5] = "Green: you do not have to move your full roll"
        self.trivia_abilities[5][0] = "Wave Rippers"
        self.trivia_abilities[5][1] = "Blue: add +2 to dice roll"
        self.trivia_abilities[5][5] = "Green: add -2 to dice roll"
        self.trivia_abilities[6][0] = "Dune Ratz"
        self.trivia_abilities[6][1] = "Blue: you can earn any accelecharger on any wedge space"
        self.trivia_abilities[6][5] = "Green: You can treat all spaces as 'roll again' spaces"
        self.trivia_abilities[7][0] = "Street Breed"
        self.trivia_abilities[7][1] = "Blue: you can reroll the dice once per question"
        self.trivia_abilities[7][5] = "Green: you can roll a second die"
        self.trivia_abilities[8][0] = "Scorchers"
        self.trivia_abilities[8][1] = "Blue: skip one question between correct answers"
        self.trivia_abilities[8][5] = "Green: add +1, 2, or 3 to dice roll"
        self.trivia_abilities[9][0] = "Road Beasts"
        self.trivia_abilities[9][1] = "Blue: after correctly answering a question you can return to your previous position"
        self.trivia_abilities[9][5] = "Green: move to an adjacent roll again spaces"
        

    def update_arch_settings(self, goal, shop_upgrades, shop_colors, shop_music, shop_sounds, gift_coins, milestone_interval, timecap_interval,
                            Starting_coin_count, Death_link, Death_link_mercy, Time_dilation, enable_trivial_pursuit, enable_trivia_questions):
        self.connected = 1
        self.milestoneint = milestone_interval
        for x in range(86400):
            self._milestones[x][0] = (x+1)*self.milestoneint
        self.archipelagoactive = True
        self.goal = goal
        self.timecapint = timecap_interval
        self._timecap = self.timecapint
        self.randoopts[0] = shop_upgrades
        self.randoopts[1] = shop_colors
        self.randoopts[2] = shop_music
        self.randoopts[3] =shop_sounds
        self.timescale = Time_dilation
        self.giftcoins = gift_coins
        self.giftedcoins = Starting_coin_count
        self.startingcoincount = Starting_coin_count
        self.deathlink = Death_link
        self.deathlinkmercy = Death_link_mercy
        self.enabletrivialpursuit = enable_trivial_pursuit
        self.enabletriviaquestion = enable_trivia_questions


    @property
    def currenttime(self):
        return self._currenttime
    
    @currenttime.setter
    def currenttime(self,value):
        self._currenttime = value
        self.ui.timer(self.currenttime)

    @property
    def maxtime(self):
        return self._maxtime
    
    @maxtime.setter
    def maxtime(self,value):
        self._maxtime = value
        self.ui.maxtimer(self.maxtime)

    @property
    def totaltime(self):
        return self._totaltime
    
    @totaltime.setter
    def totaltime(self,value):
        self._totaltime = value
        self.ui.totaltimer(self.totaltime)

    @property
    def peaktime(self):
        return self._peaktime
    
    @peaktime.setter
    def peaktime(self,value):
        self._peaktime = value
        self.ui.peaktimer(self.peaktime)
    
    @property
    def points(self):
        return self._points
    
    @points.setter
    def points(self,value):
        self._points = value
        self.ui.pointer(self.points)

    @property
    def playingstate(self):
        return self._playingstate
    
    @playingstate.setter
    def playingstate(self,value):
        self._playingstate = value
        self.ui.playingstater(self.playingstate)

    @property
    def shopstate(self):
        return self._shopstate
    
    @shopstate.setter
    def shopstate(self,value):
        self._shopstate = value
        self.ui.shopstater(self.shopstate)

    @property
    def timecap(self):
        return self._timecap
    
    @timecap.setter
    def timecap(self,value):
        self._timecap = value
        self.ui.timecaper(self.timecap)

    @property
    def speedups(self):
        return self._speedups
    
    @speedups.setter
    def speedups(self,value):
        self._speedups = value
        self.ui.speedupser(self.speedups)

    @property
    def timecaps(self):
        return self._timecaps
    
    @timecaps.setter
    def timecaps(self,value):
        self._timecaps = value
        self.ui.timecapser(self.timecaps)

    @property
    def digits(self):
        return self._digits
    
    @digits.setter
    def digits(self,value):
        self._digits = value
        self.ui.digitser(self.digits)

    @property
    def forcestatechange(self):
        return self._forcestatechange
    
    @forcestatechange.setter
    def forcestatechange(self,value):
        self._forcestatechange = value
        self.ui.forcestatechanger(self.forcestatechange)

    @property
    def milestonesforce(self):
        return self._milestonesforce
    
    @milestonesforce.setter
    def milestonesforce(self,value):
        self._milestonesforce = value
        self.ui.milestoneforcer(self.milestonesforce)

    @property
    def milestones(self):
        return self._milestones
    
    @milestones.setter
    def milestones(self,value,row):
        self._milestones[row,1] = value
        self.ui.milestoner(self.milestones)

    @property
    def shop(self):
        return self._shop
    
    @shop.setter
    def shop(self,value,state,position,row):
        self._shop[state][position][row] = value
        self.ui.shoper(self.shop)

    @property
    def colorselect(self):
        return self._colorselect
    
    @colorselect.setter
    def colorselect(self,value):
        self._colorselect = value
        self.ui.colorselecter(self.colorselect)

    @property
    def musicselect(self):
        return self._musicselect
    
    @musicselect.setter
    def musicselect(self,value):
        self._musicselect = value
        self.ui.musicselecter(self.musicselect)
        