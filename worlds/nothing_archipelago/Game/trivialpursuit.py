import pygame
from .buttons import Button
from .events import LocationClearedEvent
from random import randint

class triviagame:
    def __init__(self, font, font2, font3, frames):
        self.display_surface = pygame.display.get_surface()
        self.font = font
        self.font2 = font2
        self.font3 = font3
        WINDOW_WIDTH = 1920
        WINDOW_HEIGHT = 1080
        self.board_surf = pygame.transform.smoothscale_by(frames['board'],0.7)
        self.car_surf = frames['car000000']
        self.car000000_surf = frames['car000000']
        self.car000001_surf = frames['car000001']
        self.car000010_surf = frames['car000010']
        self.car000011_surf = frames['car000011']
        self.car000100_surf = frames['car000100']
        self.car000101_surf = frames['car000101']
        self.car000110_surf = frames['car000110']
        self.car000111_surf = frames['car000111']
        self.car001000_surf = frames['car001000']
        self.car001001_surf = frames['car001001']
        self.car001010_surf = frames['car001010']
        self.car001011_surf = frames['car001011']
        self.car001100_surf = frames['car001100']
        self.car001101_surf = frames['car001101']
        self.car001110_surf = frames['car001110']
        self.car001111_surf = frames['car001111']
        self.car010000_surf = frames['car010000']
        self.car010001_surf = frames['car010001']
        self.car010010_surf = frames['car010010']
        self.car010011_surf = frames['car010011']
        self.car010100_surf = frames['car010100']
        self.car010101_surf = frames['car010101']
        self.car010110_surf = frames['car010110']
        self.car010111_surf = frames['car010111']
        self.car011000_surf = frames['car011000']
        self.car011001_surf = frames['car011001']
        self.car011010_surf = frames['car011010']
        self.car011011_surf = frames['car011011']
        self.car011100_surf = frames['car011100']
        self.car011101_surf = frames['car011101']
        self.car011110_surf = frames['car011110']
        self.car011111_surf = frames['car011111']
        self.car100000_surf = frames['car100000']
        self.car100001_surf = frames['car100001']
        self.car100010_surf = frames['car100010']
        self.car100011_surf = frames['car100011']
        self.car100100_surf = frames['car100100']
        self.car100101_surf = frames['car100101']
        self.car100110_surf = frames['car100110']
        self.car100111_surf = frames['car100111']
        self.car101000_surf = frames['car101000']
        self.car101001_surf = frames['car101001']
        self.car101010_surf = frames['car101010']
        self.car101011_surf = frames['car101011']
        self.car101100_surf = frames['car101100']
        self.car101101_surf = frames['car101101']
        self.car101110_surf = frames['car101110']
        self.car101111_surf = frames['car101111']
        self.car110000_surf = frames['car110000']
        self.car110001_surf = frames['car110001']
        self.car110010_surf = frames['car110010']
        self.car110011_surf = frames['car110011']
        self.car110100_surf = frames['car110100']
        self.car110101_surf = frames['car110101']
        self.car110110_surf = frames['car110110']
        self.car110111_surf = frames['car110111']
        self.car111000_surf = frames['car111000']
        self.car111001_surf = frames['car111001']
        self.car111010_surf = frames['car111010']
        self.car111011_surf = frames['car111011']
        self.car111100_surf = frames['car111100']
        self.car111101_surf = frames['car111101']
        self.car111110_surf = frames['car111110']
        self.car111111_surf = frames['car111111']
        self.pos = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2)
        self.delta1 = 0
        self.final_question = False
        self.gotocenterbutton = Button(self.font, "Goto Center of the Board", WINDOW_WIDTH/2, WINDOW_HEIGHT-80,(255,255,255),0)
        self.nextteambutton = Button(self.font, "next Team", WINDOW_WIDTH/2, WINDOW_HEIGHT-80,(255,255,255),0)
        self.prevteambutton = Button(self.font, "next Team", WINDOW_WIDTH/2, WINDOW_HEIGHT-80,(255,255,255),0)
        self.rollbutton = Button(self.font, "Roll", WINDOW_WIDTH/2, WINDOW_HEIGHT-80,(255,255,255),0)
        self.acknowledgeintro = Button(self.font,"[Continue]",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.selectteambutton = Button(self.font,"Select Teku",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.upbutton = Button(self.font,"Up",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.downbutton = Button(self.font,"Down",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.uprightbutton = Button(self.font,"Up Right",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.upleftbutton = Button(self.font,"Up Left",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.downleftbutton = Button(self.font,"Down Left",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.downrightbutton = Button(self.font,"Down Right",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.clockwisebutton = Button(self.font,"Clockwise",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.counterclockwisebutton = Button(self.font,"Counter Clockwise",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.stopbutton = Button(self.font,"Stop Movement",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.continuebutton = Button(self.font,"continue Movement",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.add1button = Button(self.font,"+1 to roll",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.add2button = Button(self.font,"+2 to roll",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.remove1button = Button(self.font,"-1 to roll",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.remove2button = Button(self.font,"-2 to roll",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.doublebutton = Button(self.font,"double roll",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.halfbutton = Button(self.font,"half roll",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.triplebutton = Button(self.font,"triple roll",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.set1button = Button(self.font,"set roll to 1",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.set5button = Button(self.font,"set roll to 5",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.switchboardsidebutton = Button(self.font,"change sides of the board",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.rerollbutton = Button(self.font,"Reroll",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.questionbutton = Button(self.font,"Normal Question",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.normalquestionbutton = Button(self.font,"Normal Question",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.skipquestionbutton = Button(self.font,"Skip Question",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.rollagainquestionbutton = Button(self.font,"Roll Again Question",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.returntopreviousspotbutton = Button(self.font,"Return to Previous Position",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.movetoadjecentrollagainbutton = Button(self.font,"Move to Adjecent Roll Again",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.roll2nddiebutton = Button(self.font,"Roll a Second Die",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.add3button = Button(self.font,"+3 to Roll",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.bluebutton = Button(self.font,"Blue Question",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.pinkbutton = Button(self.font,"Pink Question",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.yellowbutton = Button(self.font,"Yellow Question",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.purplebutton = Button(self.font,"Purple Question",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.greenbutton = Button(self.font,"Green Question",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.orangebutton = Button(self.font,"Orange Question",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.answer1button = Button(self.font,"answer 1",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.answer2button = Button(self.font,"answer 2",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.answer3button = Button(self.font,"answer 3",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.answer4button = Button(self.font,"answer 4",WINDOW_WIDTH/2,520,(255,255,255),0)
        self.returntonothingbutton = Button(self.font,"Return to Doing Nothing",WINDOW_WIDTH/2,520,(255,255,255),0)

    def display_intro(self,data,dt):
        text_surf = self.font3.render("A Word of Warning",False,data.colors[data.colorselect][1])
        text_rect = text_surf.get_frect(center = (data.WINDOW_WIDTH/2,80))
        self.display_surface.blit(text_surf, text_rect)
        text_surf2 = self.font.render("This is not a normal game of Trivial Pursuit",False,data.colors[data.colorselect][1])
        text_rect2 = text_surf2.get_frect(center = (data.WINDOW_WIDTH/2,160))
        self.display_surface.blit(text_surf2, text_rect2)
        text_surf3= self.font.render("All the trivia in this game is based on the 2003-2005 series of Hotwheels movies,",False,data.colors[data.colorselect][1])
        text_rect3 = text_surf3.get_frect(center = (data.WINDOW_WIDTH/2,200))
        self.display_surface.blit(text_surf3, text_rect3)
        text_surf12= self.font.render("the associated comics, and details confirmed by the creator",False,data.colors[data.colorselect][1])
        text_rect12 = text_surf12.get_frect(center = (data.WINDOW_WIDTH/2,240))
        self.display_surface.blit(text_surf12, text_rect12)
        text_surf4 = self.font.render("The following additional changes have been made:",False,data.colors[data.colorselect][1])
        text_rect4 = text_surf4.get_frect(center = (data.WINDOW_WIDTH/2,300))
        self.display_surface.blit(text_surf4, text_rect4)
        text_surf5 = self.font.render("Earning wedges (accelechargers) will provide additional benefits based on the team you select,",False,data.colors[data.colorselect][1])
        text_rect5 = text_surf5.get_frect(center = (data.WINDOW_WIDTH/2,360))
        self.display_surface.blit(text_surf5, text_rect5)
        text_surf6 = self.font.render("Roll again spaces have been replaced with a question based on dice roll,",False,data.colors[data.colorselect][1])
        text_rect6 = text_surf6.get_frect(center = (data.WINDOW_WIDTH/2,400))
        self.display_surface.blit(text_surf6, text_rect6)
        text_surf7 = self.font.render("The answers are provided in a multiple choice format,",False,data.colors[data.colorselect][1])
        text_rect7 = text_surf7.get_frect(center = (data.WINDOW_WIDTH/2,440))
        self.display_surface.blit(text_surf7, text_rect7)
        text_surf8 = self.font.render("wedges (accelechargers) are 'removed' (disabled) if you answer wrong on a wedge after earning them,",False,data.colors[data.colorselect][1])
        text_rect8 = text_surf8.get_frect(center = (data.WINDOW_WIDTH/2,480))
        self.display_surface.blit(text_surf8, text_rect8)
        text_surf9 = self.font.render("if you get the final question wrong all accelecharges are disabled till you answer a question correctly,",False,data.colors[data.colorselect][1])
        text_rect9 = text_surf9.get_frect(center = (data.WINDOW_WIDTH/2,520))
        self.display_surface.blit(text_surf9, text_rect9)
        text_surf10 = self.font.render("you must have all accelecharges active to attempt the final question,",False,data.colors[data.colorselect][1])
        text_rect10 = text_surf10.get_frect(center = (data.WINDOW_WIDTH/2,560))
        self.display_surface.blit(text_surf10, text_rect10)
        text_surf11 = self.font.render("and answering any question wrong will result in a penalty time (and send a death)",False,data.colors[data.colorselect][1])
        text_rect11 = text_surf11.get_frect(center = (data.WINDOW_WIDTH/2,600))
        self.display_surface.blit(text_surf11, text_rect11)
        self.acknowledgeintro.updatec("[Continue]",data.WINDOW_WIDTH/2,680,data.colors[data.colorselect][1],0)
        if self.acknowledgeintro.draw(self.display_surface):
            if self.delta1 > 0.5:
                data.trivia_intro = True
                self.delta1 = 0
        self.delta1 += dt

    def display_team_select(self, data,dt):
        text_surf = self.font.render(data.trivia_abilities[data.trivia_team][0],False,data.colors[data.colorselect][1])
        text_rect = text_surf.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2-120))
        self.display_surface.blit(text_surf, text_rect)
        text_surf1 = self.font.render(data.trivia_abilities[data.trivia_team][1],False,data.colors[data.colorselect][1])
        text_rect1 = text_surf1.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2-80))
        self.display_surface.blit(text_surf1, text_rect1)
        text_surf2 = self.font.render(data.trivia_abilities[data.trivia_team][2],False,data.colors[data.colorselect][1])
        text_rect2 = text_surf2.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2-40))
        self.display_surface.blit(text_surf2, text_rect2)
        text_surf3 = self.font.render(data.trivia_abilities[data.trivia_team][3],False,data.colors[data.colorselect][1])
        text_rect3 = text_surf3.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2))
        self.display_surface.blit(text_surf3, text_rect3)
        text_surf4 = self.font.render(data.trivia_abilities[data.trivia_team][4],False,data.colors[data.colorselect][1])
        text_rect4 = text_surf4.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2+40))
        self.display_surface.blit(text_surf4, text_rect4)
        text_surf5 = self.font.render(data.trivia_abilities[data.trivia_team][5],False,data.colors[data.colorselect][1])
        text_rect5 = text_surf5.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2+80))
        self.display_surface.blit(text_surf5, text_rect5)
        text_surf6 = self.font.render(data.trivia_abilities[data.trivia_team][6],False,data.colors[data.colorselect][1])
        text_rect6 = text_surf6.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2+120))
        self.display_surface.blit(text_surf6, text_rect6)
        self.selectteambutton.updatec("Select " + data.trivia_abilities[data.trivia_team][0],data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2+200,data.colors[data.colorselect][1],0)
        if self.selectteambutton.draw(self.display_surface):
            if self.delta1 > 0.5:
                data.trivia_selected_team = True
                data.trivia_state = 1
                self.delta1 = 0
        self.nextteambutton.updatec("Next Team",data.WINDOW_WIDTH/2+360,data.WINDOW_HEIGHT/2+200,data.colors[data.colorselect][1],0)
        if self.nextteambutton.draw(self.display_surface):
            if self.delta1 > 0.5:
                self.delta1 = 0
                if data.trivia_team == 9:
                    data.trivia_team = 0
                else:
                    data.trivia_team += 1
        self.prevteambutton.updatec("Previous Team",data.WINDOW_WIDTH/2-360,data.WINDOW_HEIGHT/2+200,data.colors[data.colorselect][1],0)
        if self.prevteambutton.draw(self.display_surface):
            if self.delta1 > 0.5:
                self.delta1 = 0
                if data.trivia_team == 0:
                    data.trivia_team = 9
                else:
                    data.trivia_team -= 1
        self.delta1 += dt
        
        
    def display_board(self,data):
        self.check_pos(data)
        self.check_car(data)
        board_rect = self.board_surf.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2-100))
        self.display_surface.blit(self.board_surf,board_rect)
        player_rect = self.car_surf.get_frect(center = self.pos)
        self.display_surface.blit(self.car_surf,player_rect)

    def check_pos(self,data):
        self.pos = data.positions[data.trivia_location][0]

    def check_car(self,data):
        carindex = 0
        if data.trivia_wedges[5][0] == 1 and data.trivia_wedges[5][2]:
            carindex += 1
        if data.trivia_wedges[4][0] == 1 and data.trivia_wedges[4][2]:
            carindex += 2
        if data.trivia_wedges[3][0] == 1 and data.trivia_wedges[3][2]:
            carindex += 4
        if data.trivia_wedges[2][0] == 1 and data.trivia_wedges[2][2]:
            carindex += 8
        if data.trivia_wedges[1][0] == 1 and data.trivia_wedges[1][2]:
            carindex += 16
        if data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]:
            carindex += 32
        match carindex:
            case 0:
                self.car_surf = self.car000000_surf
            case 1:
                self.car_surf = self.car000001_surf
            case 2:
                self.car_surf = self.car000010_surf
            case 3:
                self.car_surf = self.car000011_surf
            case 4:
                self.car_surf = self.car000100_surf
            case 5:
                self.car_surf = self.car000101_surf
            case 6:
                self.car_surf = self.car000110_surf
            case 7:
                self.car_surf = self.car000111_surf
            case 8:
                self.car_surf = self.car001000_surf
            case 9:
                self.car_surf = self.car001001_surf
            case 10:
                self.car_surf = self.car001010_surf
            case 11:
                self.car_surf = self.car001011_surf
            case 12:
                self.car_surf = self.car001100_surf
            case 13:
                self.car_surf = self.car001101_surf
            case 14:
                self.car_surf = self.car001110_surf
            case 15:
                self.car_surf = self.car001111_surf
            case 16:
                self.car_surf = self.car010000_surf
            case 17:
                self.car_surf = self.car010001_surf
            case 18:
                self.car_surf = self.car010010_surf
            case 19:
                self.car_surf = self.car010011_surf
            case 20:
                self.car_surf = self.car010100_surf
            case 21:
                self.car_surf = self.car010101_surf
            case 22:
                self.car_surf = self.car010110_surf
            case 23:
                self.car_surf = self.car010111_surf
            case 24:
                self.car_surf = self.car011000_surf
            case 25:
                self.car_surf = self.car011001_surf
            case 26:
                self.car_surf = self.car011010_surf
            case 27:
                self.car_surf = self.car011011_surf
            case 28:
                self.car_surf = self.car011100_surf
            case 29:
                self.car_surf = self.car011101_surf
            case 30:
                self.car_surf = self.car011110_surf
            case 31:
                self.car_surf = self.car011111_surf
            case 32:
                self.car_surf = self.car100000_surf
            case 33:
                self.car_surf = self.car100001_surf
            case 34:
                self.car_surf = self.car100010_surf
            case 35:
                self.car_surf = self.car100011_surf
            case 36:
                self.car_surf = self.car100100_surf
            case 37:
                self.car_surf = self.car100101_surf
            case 38:
                self.car_surf = self.car100110_surf
            case 39:
                self.car_surf = self.car100111_surf
            case 40:
                self.car_surf = self.car101000_surf
            case 41:
                self.car_surf = self.car101001_surf
            case 42:
                self.car_surf = self.car101010_surf
            case 43:
                self.car_surf = self.car101011_surf
            case 44:
                self.car_surf = self.car101100_surf
            case 45:
                self.car_surf = self.car101101_surf
            case 46:
                self.car_surf = self.car101110_surf
            case 47:
                self.car_surf = self.car101111_surf
            case 48:
                self.car_surf = self.car110000_surf
            case 49:
                self.car_surf = self.car110001_surf
            case 50:
                self.car_surf = self.car110010_surf
            case 51:
                self.car_surf = self.car110011_surf
            case 52:
                self.car_surf = self.car110100_surf
            case 53:
                self.car_surf = self.car110101_surf
            case 54:
                self.car_surf = self.car110110_surf
            case 55:
                self.car_surf = self.car110111_surf
            case 56:
                self.car_surf = self.car111000_surf
            case 57:
                self.car_surf = self.car111001_surf
            case 58:
                self.car_surf = self.car111010_surf
            case 59:
                self.car_surf = self.car111011_surf
            case 60:
                self.car_surf = self.car111100_surf
            case 61:
                self.car_surf = self.car111101_surf
            case 62:
                self.car_surf = self.car111110_surf
            case 63:
                self.car_surf = self.car111111_surf
        self.car_surf = pygame.transform.smoothscale_by(self.car_surf,0.1)
        self.car_surf = pygame.transform.rotate(self.car_surf,data.positions[data.trivia_location][1])

    def display_roll(self,data,dt):
        if data.trivia_last_question:
            text_surf = self.font.render("Correct",False,data.colors[data.colorselect][1])
            text_rect = text_surf.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT-80))
            self.display_surface.blit(text_surf, text_rect)
        self.rollbutton.updatec("Roll Die",data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT-40,data.colors[data.colorselect][1],0)
        if self.rollbutton.draw(self.display_surface):
            if self.delta1 > 0.5:
                x = randint(1,6)
                data.trivia_roll = x
                data.trivia_moves = x
                data.trivia_state = 2
                data.trivia_last_location = data.trivia_location
                data.trivia_last_question = False
                self.delta1 = 0
                data.trivia_used_blue == False
                data.trivia_used_green == False
        if data.trivia_enabled:
            self.switchboardsidebutton.updatec("Switch Sides of the Board",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
            if data.trivia_team == 3 and data.trivia_wedges[5][0] == 1 and data.trivia_wedges[5][2]:
                if self.switchboardsidebutton.draw(self.display_surface):
                    if self.delta1 > 0.5:
                        self.flipboard(data)
                        data.trivia_state = 4
                        self.delta1 = 0
                        data.trivia_used_blue == False
                        data.trivia_used_green == False
            self.gotocenterbutton.updatec("Goto Center of the Board",data.WINDOW_WIDTH*3/4,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
            if data.trivia_wedges[4][0] == 1 and data.trivia_wedges[4][2]:
                if self.gotocenterbutton.draw(self.display_surface):
                    if self.delta1 > 0.5:
                        data.trivia_last_location = data.trivia_location
                        data.trivia_location = 0
                        data.trivia_state = 4
                        self.delta1 = 0
                        data.trivia_used_blue == False
                        data.trivia_used_green == False
            self.returntopreviousspotbutton.updatec("Return to Previous Location",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
            if data.trivia_team == 9 and data.trivia_wedges[0][0] == 1 and data.trivia_last_question and data.trivia_wedges[0][2]:
                if self.returntopreviousspotbutton.draw(self.display_surface):
                    if self.delta1 > 0.5:
                        data.trivia_location = data.trivia_last_location
                        data.trivia_last_question = False
                        self.delta1 = 0
        self.delta1 += dt

            
    def flipboard(data):
        if data.trivia_location == 0:
            data.trivia_location = 0
        elif data.trivia_location < 16:
            data.trivia_location += 15
        elif data.trivia_location < 31:
            data.trivia_location -= 15
        elif data.trivia_location < 52:
            data.trivia_location += 21
        else:
            data.trivia_location -= 21
            
    def display_abilities(self,data,dt):
        if data.trivia_enabled:
            match data.trivia_team:
                case 0:
                    self.add1button.updatec("+1 to Roll",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-120,data.colors[data.colorselect][1],0)
                    self.remove1button.updatec("-1 to Roll",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
                    if data.trivia_wedges[0][0] == 1 and data.trivia_used_blue == False and data.trivia_wedges[0][2]:
                        if self.add1button.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_moves += 1
                                data.trivia_roll = ((data.trivia_moves + 5) % 6) + 1
                                data.trivia_used_blue = True
                                self.delta1 = 0
                    if data.trivia_wedges[4][0] == 1 and data.trivia_used_green == False and data.trivia_wedges[4][2]:
                        if self.remove1button.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_moves -= 1
                                data.trivia_roll = ((data.trivia_moves + 5) % 6) + 1
                                data.trivia_used_green = True
                                self.delta1 = 0
                case 1:
                    self.set1button.updatec("Set Roll to 1",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-120,data.colors[data.colorselect][1],0)
                    self.set5button.updatec("Set Roll to 5",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
                    if data.trivia_wedges[0][0] == 1 and data.trivia_used_blue == False and data.trivia_wedges[0][2]:
                        if self.set1button.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_moves = 1
                                data.trivia_roll = 1
                                data.trivia_used_blue = True
                                self.delta1 = 0
                    if data.trivia_wedges[4][0] == 1 and data.trivia_used_green == False and data.trivia_wedges[4][2]:
                        if self.set5button.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_moves = 5
                                data.trivia_roll = 5
                                data.trivia_used_green = True
                                self.delta1 = 0
                case 2:
                    self.doublebutton.updatec("Double Roll",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-120,data.colors[data.colorselect][1],0)
                    self.halfbutton.updatec("Half Roll",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
                    if data.trivia_wedges[0][0] == 1 and data.trivia_used_blue == False and data.trivia_wedges[0][2]:
                        if self.doublebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_moves = data.trivia_moves*2
                                data.trivia_roll = ((data.trivia_moves + 5) % 6) + 1
                                data.trivia_used_blue = True
                                self.delta1 = 0
                    if data.trivia_wedges[4][0] == 1 and data.trivia_used_green == False and data.trivia_wedges[4][2]:
                        if self.halfbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_moves = int(data.trivia_moves/2)
                                data.trivia_roll = data.trivia_moves
                                data.trivia_used_green = True
                                self.delta1 = 0
                case 4:
                    self.triplebutton.updatec("Triple Roll",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-120,data.colors[data.colorselect][1],0)
                    if data.trivia_wedges[0][0] == 1 and data.trivia_used_blue == False and data.trivia_wedges[0][2]:
                        if self.triplebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_moves = data.trivia_moves*3
                                data.trivia_roll = ((data.trivia_moves + 5) % 6) + 1
                                data.trivia_used_blue = True
                                self.delta1 = 0
                case 5:
                    self.add2button.updatec("+2 to Roll",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-120,data.colors[data.colorselect][1],0)
                    self.remove2button.updatec("-2 to Roll",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
                    if data.trivia_wedges[0][0] == 1 and data.trivia_used_blue == False and data.trivia_wedges[0][2]:
                        if self.add2button.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_moves += 2
                                data.trivia_roll = ((data.trivia_moves + 5) % 6) + 1
                                data.trivia_used_blue = True
                                self.delta1 = 0
                    if data.trivia_wedges[4][0] == 1 and data.trivia_used_green == False and data.trivia_moves > 1 and data.trivia_wedges[4][2]:
                        if self.remove2button.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_moves -= 2
                                data.trivia_roll = ((data.trivia_moves + 5) % 6) + 1
                                data.trivia_used_green = True
                                self.delta1 = 0
                case 7:
                    self.rerollbutton.updatec("ReRoll",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-120,data.colors[data.colorselect][1],0)
                    self.roll2nddiebutton.updatec("Roll Second Die",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
                    if data.trivia_wedges[0][0] == 1 and data.trivia_used_blue == False and data.trivia_wedges[0][2]:
                        if self.rerollbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                x = randint(1,6)
                                data.trivia_moves = x
                                if data.trivia_used_green:
                                    y = randint(1,6)
                                    data.trivia_moves += y
                                    data.trivia_roll = ((data.trivia_moves + 5) % 6) + 1
                                else:
                                    data.trivia_roll = x
                                data.trivia_used_blue = True
                                self.delta1 = 0
                    if data.trivia_wedges[4][0] == 1 and data.trivia_used_green == False and data.trivia_moves > 1 and data.trivia_wedges[4][2]:
                        if self.roll2nddiebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                x = randint(1,6)
                                data.trivia_moves += x
                                data.trivia_roll = ((data.trivia_moves + 5) % 6) + 1
                                data.trivia_used_green = True
                                self.delta1 = 0
                case 8:
                    self.add3button.updatec("+3 to Roll",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-120,data.colors[data.colorselect][1],0)
                    self.add2button.updatec("+2 to Roll",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
                    self.add1button.updatec("+1 to Roll",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
                    if data.trivia_wedges[4][0] == 1 and data.trivia_used_green == False and data.trivia_wedges[4][2]:
                        if self.add3button.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_moves += 3
                                data.trivia_roll = ((data.trivia_moves + 5) % 6) + 1
                                data.trivia_used_green = True
                                self.delta1 = 0
                        if self.add2button.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_moves += 2
                                data.trivia_roll = ((data.trivia_moves + 5) % 6) + 1
                                data.trivia_used_green = True
                                self.delta1 = 0
                        if self.add1button.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_moves += 1
                                data.trivia_roll = ((data.trivia_moves + 5) % 6) + 1
                                data.trivia_used_green = True
                                self.delta1 = 0
            self.delta1 += dt

    def display_moves(self,data,dt):
        if data.trivia_need_direction:
            text_surf = self.font3.render(str(data.trivia_moves),False,data.colors[data.colorselect][1])
            text_rect = text_surf.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT-120))
            self.display_surface.blit(text_surf, text_rect)
            self.upbutton.updatec("Up",data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT-200,data.colors[data.colorselect][1],0)
            self.downbutton.updatec("Down",data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT-40,data.colors[data.colorselect][1],0)
            self.uprightbutton.updatec("Up Right",data.WINDOW_WIDTH/2+120,data.WINDOW_HEIGHT-160,data.colors[data.colorselect][1],0)
            self.upleftbutton.updatec("Up Left",data.WINDOW_WIDTH/2-120,data.WINDOW_HEIGHT-160,data.colors[data.colorselect][1],0)
            self.downrightbutton.updatec("Down Right",data.WINDOW_WIDTH/2+120,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
            self.downleftbutton.updatec("Down Left",data.WINDOW_WIDTH/2-120,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
            self.clockwisebutton.updatec("Clockwise",data.WINDOW_WIDTH/2+200,data.WINDOW_HEIGHT-120,data.colors[data.colorselect][1],0)
            self.counterclockwisebutton.updatec("Counterclockwise",data.WINDOW_WIDTH/2-200,data.WINDOW_HEIGHT-120,data.colors[data.colorselect][1],0)
            if data.trivia_moves > 0:
                if data.trivia_location == 0:
                    if data.trivia_last_direction != 1 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.downbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 4
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 2 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.downleftbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 5
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 3 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.upleftbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 6
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 4 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.upbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 1
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 5 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.uprightbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 2
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 6 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.downrightbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 3
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                elif data.trivia_location < 6:
                    if data.trivia_last_direction != 1 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.downbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 4
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 4 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.upbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 1
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                elif data.trivia_location < 11:
                    if data.trivia_last_direction != 2 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.downleftbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 5
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 5 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.uprightbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 2
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                elif data.trivia_location < 16:
                    if data.trivia_last_direction != 3 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.upleftbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 6
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 6 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.downrightbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 3
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                elif data.trivia_location < 21:
                    if data.trivia_last_direction != 1 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.downbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 4
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 4 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.upbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 1
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                elif data.trivia_location < 26:
                    if data.trivia_last_direction != 2 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.downleftbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 5
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 5 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.uprightbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 2
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                elif data.trivia_location < 31:
                    if data.trivia_last_direction != 3 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.upleftbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 6
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 6 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.downrightbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 3
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                elif data.trivia_location == 31:
                    if data.trivia_last_direction != 1 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.downbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 4
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 7 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.counterclockwisebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 8
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 8 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.clockwisebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 7
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                elif data.trivia_location == 38:
                    if data.trivia_last_direction != 2 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.downleftbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 5
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 7 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.counterclockwisebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 8
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 8 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.clockwisebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 7
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                elif data.trivia_location == 45:
                    if data.trivia_last_direction != 3 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.upleftbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 6
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 7 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.counterclockwisebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 8
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 8 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.clockwisebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 7
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                elif data.trivia_location == 52:
                    if data.trivia_last_direction != 4 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.upbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 1
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 7 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.counterclockwisebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 8
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 8 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.clockwisebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 7
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                elif data.trivia_location == 59:
                    if data.trivia_last_direction != 5 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.uprightbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 2
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 7 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.counterclockwisebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 8
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 8 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.clockwisebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 7
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                elif data.trivia_location == 66:
                    if data.trivia_last_direction != 6 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.downrightbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 3
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 7 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.counterclockwisebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 8
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 8 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.clockwisebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 7
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                else:
                    if data.trivia_last_direction != 7 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.counterclockwisebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 8
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
                    if data.trivia_last_direction != 8 or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2]):
                        if self.clockwisebutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                data.trivia_last_direction = 7
                                data.trivia_need_direction = False
                                data.trivia_move = True
                                data.trivia_state = 3
                                self.delta1 = 0
        if data.trivia_team == 4 and data.trivia_wedges[4][0] == 1 and data.trivia_moves > 0  and data.trivia_wedges[4][2]:
            self.stopbutton.updatec("Stop Movement",data.WINDOW_WIDTH*3/4,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
            if self.stopbutton.draw(self.display_surface):
                if self.delta1 > 0.5:
                    data.trivia_moves = 0
                    data.trivia_move = True
                    self.delta1 = 0
            if data.trivia_need_direction == False:
                self.continuebutton.updatec("Continue Movement",data.WINDOW_WIDTH*3/4,data.WINDOW_HEIGHT-40,data.colors[data.colorselect][1],0)
                if self.continuebutton.draw(self.display_surface):
                    if self.delta1 > 0.5:
                        data.trivia_move = True
                        self.delta1 = 0
        self.delta1 += dt

    def moving(self,data):
        if self.delta1 > 0.25:
            if data.trivia_moves > 0  and data.trivia_move:
                self.delta1 = 0
                data.trivia_moves -= 1
                if data.trivia_last_direction == 1:
                    if data.trivia_location == 0:
                        data.trivia_location = 1
                    elif data.trivia_location < 5:
                        data.trivia_location += 1
                    elif data.trivia_location == 5:
                        data.trivia_location = 31
                    elif data.trivia_location == 16:
                        data.trivia_location = 0
                    elif data.trivia_location < 21:
                        data.trivia_location -= 1
                    elif data.trivia_location == 52:
                        data.trivia_location = 20
                elif data.trivia_last_direction == 2:
                    if data.trivia_location == 0:
                        data.trivia_location = 6
                    elif data.trivia_location < 10:
                        data.trivia_location += 1
                    elif data.trivia_location == 10:
                        data.trivia_location = 38
                    elif data.trivia_location == 21:
                        data.trivia_location = 0
                    elif data.trivia_location < 26:
                        data.trivia_location -= 1
                    elif data.trivia_location == 59:
                        data.trivia_location = 25
                elif data.trivia_last_direction == 3:
                    if data.trivia_location == 0:
                        data.trivia_location = 11
                    elif data.trivia_location < 15:
                        data.trivia_location += 1
                    elif data.trivia_location == 15:
                        data.trivia_location = 45
                    elif data.trivia_location == 26:
                        data.trivia_location = 0
                    elif data.trivia_location < 31:
                        data.trivia_location -= 1
                    elif data.trivia_location == 66:
                        data.trivia_location = 30
                elif data.trivia_last_direction == 4:
                    if data.trivia_location == 0:
                        data.trivia_location = 16
                    elif data.trivia_location == 1:
                        data.trivia_location = 0
                    elif data.trivia_location < 6:
                        data.trivia_location -= 1
                    elif data.trivia_location < 20:
                        data.trivia_location += 1
                    elif data.trivia_location == 20:
                        data.trivia_location = 52
                    elif data.trivia_location == 31:
                        data.trivia_location = 5
                elif data.trivia_last_direction == 5:
                    if data.trivia_location == 0:
                        data.trivia_location = 21
                    elif data.trivia_location == 6:
                        data.trivia_location = 0
                    elif data.trivia_location < 11:
                        data.trivia_location -= 1
                    elif data.trivia_location < 25:
                        data.trivia_location += 1
                    elif data.trivia_location == 25:
                        data.trivia_location = 59
                    elif data.trivia_location == 38:
                        data.trivia_location = 10
                elif data.trivia_last_direction == 6:
                    if data.trivia_location == 0:
                        data.trivia_location = 26
                    elif data.trivia_location == 11:
                        data.trivia_location = 0
                    elif data.trivia_location < 16:
                        data.trivia_location -= 1
                    elif data.trivia_location < 30:
                        data.trivia_location += 1
                    elif data.trivia_location == 30:
                        data.trivia_location = 66
                    elif data.trivia_location == 45:
                        data.trivia_location = 15
                elif data.trivia_last_direction == 7:
                    if data.trivia_location == 72:
                        data.trivia_location = 31
                    else:
                        data.trivia_location += 1
                elif data.trivia_last_direction == 8:
                    if data.trivia_location == 31:
                        data.trivia_location = 72
                    else:
                        data.trivia_location -= 1
                if data.trivia_location == 0 or data.trivia_location == 31 or data.trivia_location == 38 or data.trivia_location == 45 or data.trivia_location == 52 or data.trivia_location == 59 or data.trivia_location == 66:
                    data.trivia_move = False
                    data.trivia_need_direction = True
            if data.trivia_enabled and ((data.trivia_team == 4 and data.trivia_wedges[4][0] ==1 and data.trivia_wedges[4][2]) or (data.trivia_team == 3 and data.trivia_wedges[0][0] == 1 and data.trivia_wedges[0][2])):
                data.trivia_move = False
                data.trivia_need_direction = True
            
        if data.trivia_team == 9 and data.trivia_wedges[4][0] == 1 and data.trivia_moves == 0  and data.trivia_wedges[4][2]:
            self.movetoadjecentrollagainbutton.updatec("Move to Adjecent 'Roll Again' Space",data.WINDOW_WIDTH*3/4,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
            if data.trivia_location == 32 or data.trivia_location == 39 or data.trivia_location == 46 or data.trivia_location == 53 or data.trivia_location == 60 or data.trivia_location == 67:
                if self.movetoadjecentrollagainbutton.draw(self.display_surface):
                    if self.delta1 > 0.5:
                        data.trivia_location += 1
                        self.delta1 = 0
            elif data.trivia_location == 34 or data.trivia_location == 41 or data.trivia_location == 48 or data.trivia_location == 55 or data.trivia_location == 62 or data.trivia_location == 69:
                if self.movetoadjecentrollagainbutton.draw(self.display_surface):
                    if self.delta1 > 0.5:
                        data.trivia_location -= 1
                        self.delta1 = 0
            elif data.trivia_location == 35 or data.trivia_location == 42 or data.trivia_location == 49 or data.trivia_location == 56 or data.trivia_location == 63 or data.trivia_location == 70:
                if self.movetoadjecentrollagainbutton.draw(self.display_surface):
                    if self.delta1 > 0.5:
                        data.trivia_location += 1
                        self.delta1 = 0
            elif data.trivia_location == 37 or data.trivia_location == 44 or data.trivia_location == 51 or data.trivia_location == 58 or data.trivia_location == 65 or data.trivia_location == 72:
                if self.movetoadjecentrollagainbutton.draw(self.display_surface):
                    if self.delta1 > 0.5:
                        data.trivia_location -= 1
                        self.delta1 = 0

        if data.trivia_moves == 0:
            self.questionbutton.updatec("Goto Question Select",data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT-40,data.colors[data.colorselect][1],0)
            if self.questionbutton.draw(self.display_surface):
                if self.delta1 > 0.5:
                    data.trivia_state = 4
                    data.trivia_last_direction = 0
                    data.trivia_move = False
                    data.trivia_need_direction = True
                    data.trivia_need_question = False
                    self.delta1 = 0
    
    def display_question_select(self,data,dt):
        self.rollagainquestionbutton.updatec("Roll Again Question",data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
        self.set1button.updatec("Set Roll to 1",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
        self.set5button.updatec("Set Roll to 5",data.WINDOW_WIDTH/4,data.WINDOW_HEIGHT-40,data.colors[data.colorselect][1],0)
        if data.trivia_need_question == False:
            if data.trivia_team == 1 and data.trivia_enabled:
                if data.trivia_wedges[0][0] == 1 and data.trivia_used_blue == False and data.trivia_wedges[0][2]:
                    if self.set1button.draw(self.display_surface):
                        if self.delta1 > 0.5:
                            data.trivia_roll = 1
                            data.trivia_used_blue = True
                            self.delta1 = 0
                if data.trivia_wedges[4][0] == 1 and data.trivia_used_green == False and data.trivia_wedges[0][2]:
                    if self.set5button.draw(self.display_surface):
                        if self.delta1 > 0.5:
                            data.trivia_roll = 5
                            data.trivia_used_green = True
                            self.delta1 = 0
            if data.trivia_location == 33 or data.trivia_location == 40 or data.trivia_location == 47 or data.trivia_location == 54 or data.trivia_location == 61 or data.trivia_location == 68:
                self.rollagainquestionbutton.updatec("Roll Again Question",data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
                if self.rollagainquestionbutton.draw(self.display_surface):
                    if self.delta1 > 0.5:
                        x = randint(0,299)
                        data.trivia_question = x
                        data.trivia_color = data.trivia_roll
                        data.trivia_shown_color = data.trivia_color - 1
                        data.trivia_need_question = True
                        self.delta1 = 0

            elif data.trivia_location == 36 or data.trivia_location == 43 or data.trivia_location == 50 or data.trivia_location == 57 or data.trivia_location == 64 or data.trivia_location == 71:
                self.rollagainquestionbutton.updatec("Roll Again Question",data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
                if self.rollagainquestionbutton.draw(self.display_surface):
                    if self.delta1 > 0.5:
                        x = randint(0,299)
                        data.trivia_question = x
                        data.trivia_color = data.trivia_roll
                        data.trivia_shown_color = data.trivia_color - 1
                        data.trivia_need_question = True
                        self.delta1 = 0

            elif data.trivia_location == 0:
                if data.trivia_wedges[0][0] == 1 and data.trivia_wedges[1][0] == 1 and data.trivia_wedges[2][0] == 1 and data.trivia_wedges[3][0] == 1 and data.trivia_wedges[4][0] == 1 and data.trivia_wedges[5][0] == 1 and data.trivia_enabled:
                    if  data.trivia_wedges[0][2] and data.trivia_wedges[1][2] and data.trivia_wedges[2][2] and data.trivia_wedges[3][2] and data.trivia_wedges[4][2] and data.trivia_wedges[5][2]:
                        self.normalquestionbutton.updatec("Final Question",data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
                        if self.normalquestionbutton.draw(self.display_surface):
                            if self.delta1 > 0.5:
                                x = randint(0,299)
                                y = randint(1,6)
                                data.trivia_question = x
                                data.trivia_color = y
                                data.trivia_shown_color = data.trivia_color - 1
                                data.trivia_need_question = True
                                self.final_question = True
                                self.delta1 = 0
                else:
                    self.bluebutton.updatec("Blue Question",data.WINDOW_WIDTH/7,data.WINDOW_HEIGHT-120,data.colors[data.colorselect][1],0)
                    self.pinkbutton.updatec("Pink Question",data.WINDOW_WIDTH*2/7,data.WINDOW_HEIGHT-120,data.colors[data.colorselect][1],0)
                    self.yellowbutton.updatec("Yellow Question",data.WINDOW_WIDTH*3/7,data.WINDOW_HEIGHT-120,data.colors[data.colorselect][1],0)
                    self.purplebutton.updatec("Purple Question",data.WINDOW_WIDTH*4/7,data.WINDOW_HEIGHT-120,data.colors[data.colorselect][1],0)
                    self.greenbutton.updatec("Green Question",data.WINDOW_WIDTH*5/7,data.WINDOW_HEIGHT-120,data.colors[data.colorselect][1],0)
                    self.orangebutton.updatec("Orange Question",data.WINDOW_WIDTH*6/7,data.WINDOW_HEIGHT-120,data.colors[data.colorselect][1],0)
                    if self.bluebutton.draw(self.display_surface):
                        if self.delta1 > 0.5:
                            x = randint(0,299)
                            data.trivia_question = x
                            data.trivia_color = 1
                            data.trivia_shown_color = data.trivia_color - 1
                            data.trivia_need_question = True
                            self.delta1 = 0
                    if self.pinkbutton.draw(self.display_surface):
                        if self.delta1 > 0.5:
                            x = randint(0,299)
                            data.trivia_question = x
                            data.trivia_color = 2
                            data.trivia_shown_color = data.trivia_color - 1
                            data.trivia_need_question = True
                            self.delta1 = 0
                    if self.yellowbutton.draw(self.display_surface):
                        if self.delta1 > 0.5:
                            x = randint(0,299)
                            data.trivia_question = x
                            data.trivia_color = 3
                            data.trivia_shown_color = data.trivia_color - 1
                            data.trivia_need_question = True
                            self.delta1 = 0
                    if self.purplebutton.draw(self.display_surface):
                        if self.delta1 > 0.5:
                            x = randint(0,299)
                            data.trivia_question = x
                            data.trivia_color = 4
                            data.trivia_shown_color = data.trivia_color - 1
                            data.trivia_need_question = True
                            self.delta1 = 0
                    if self.greenbutton.draw(self.display_surface):
                        if self.delta1 > 0.5:
                            x = randint(0,299)
                            data.trivia_question = x
                            data.trivia_color = 5
                            data.trivia_shown_color = data.trivia_color - 1
                            data.trivia_need_question = True
                            self.delta1 = 0
                    if self.orangebutton.draw(self.display_surface):
                        if self.delta1 > 0.5:
                            x = randint(0,299)
                            data.trivia_question = x
                            data.trivia_color = 6
                            data.trivia_shown_color = data.trivia_color - 1
                            data.trivia_need_question = True
                            self.delta1 = 0
            else:
                self.normalquestionbutton.updatec("Normal Question",data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT-80,data.colors[data.colorselect][1],0)
                if self.normalquestionbutton.draw(self.display_surface):
                    if self.delta1 > 0.5:
                        x = randint(0,299)
                        data.trivia_question = x
                        match data.trivia_location:
                            case 6 | 14 | 20 | 23 | 27 | 31 | 42 | 51 | 53 | 62:
                                data.trivia_color = 1
                            case 5 | 8 | 12 | 21 | 29 | 32 | 41 | 52 | 64 | 72:
                                data.trivia_color = 2
                            case 3 | 7 | 16 | 24 | 30 | 34 | 45 | 56 | 65 | 67:
                                data.trivia_color = 3
                            case 1 | 9 | 15 | 18 | 22 | 35 | 44 | 46 | 55 | 66:
                                data.trivia_color = 4
                            case 4 | 10 | 13 | 17 | 26 | 37 | 39 | 48 | 59 | 70:
                                data.trivia_color = 5
                            case 2 | 11 | 19 | 25 | 28 | 38 | 49 | 58 | 60 | 69:
                                data.trivia_color = 6
                        data.trivia_shown_color = data.trivia_color - 1
                        data.trivia_need_question = True
                        self.delta1 = 0

            if data.trivia_enabled:
                if data.trivia_team == 8 and data.trivia_wedges[0][0] == 1 and data.trivia_question_charge and data.trivia_wedges[0][2]:
                    self.skipquestionbutton.updatec("Skip Question",data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT-40,data.colors[data.colorselect][1],0)
                    if self.skipquestionbutton.draw(self.display_surface):
                        if self.delta1 > 0.5:
                            data.trivia_question_charge = False
                            data.trivia_state = 1
                            self.delta1 = 0
                if data.trivia_team == 6 and data.trivia_wedges[4][0] == 1 and data.trivia_wedges[4][2]:
                    self.rollagainquestionbutton.updatec("Roll Again Question",data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT-40,data.colors[data.colorselect][1],0)
                    if self.rollagainquestionbutton.draw(self.display_surface):
                        if self.delta1 > 0.5:
                            x = randint(0,299)
                            data.trivia_question = x
                            data.trivia_color = data.trivia_roll
                            data.trivia_shown_color = data.trivia_color - 1
                            data.trivia_need_question = True
                            self.delta1 = 0
        self.delta1 += dt

    def display_questions(self,data,dt):
        if data.trivia_enabled:
            if data.trivia_wedges[1][0] == 1 and data.trivia_wedges[1][2]:
                text_surf = self.font.render("Card Number: " + str(data.trivia_question),False,data.colors[data.colorselect][1])
                text_rect = text_surf.get_frect(topleft = (20,20))
                self.display_surface.blit(text_surf, text_rect)
            if data.trivia_wedges[2][0] == 1 and data.trivia_wedges[2][2]:
                self.bluebutton.updatetl("Blue Question",20,60,data.colors[data.colorselect][1],0)
                self.pinkbutton.updatetl("Pink Question",20,100,data.colors[data.colorselect][1],0)
                self.yellowbutton.updatetl("Yellow Question",20,140,data.colors[data.colorselect][1],0)
                self.purplebutton.updatetl("Purple Question",20,180,data.colors[data.colorselect][1],0)
                self.greenbutton.updatetl("Green Question",20,220,data.colors[data.colorselect][1],0)
                self.orangebutton.updatetl("Orange Question",20,260,data.colors[data.colorselect][1],0)
                match data.trivia_color:
                    case 1:
                        self.bluebutton.updatetl("Current Question",20,60,data.colors[data.colorselect][1],0)
                    case 2:
                        self.pinkbutton.updatetl("Current Question",20,100,data.colors[data.colorselect][1],0)
                    case 3:
                        self.yellowbutton.updatetl("Current Question",20,140,data.colors[data.colorselect][1],0)
                    case 4:
                        self.purplebutton.updatetl("Current Question",20,180,data.colors[data.colorselect][1],0)
                    case 5:
                        self.greenbutton.updatetl("Current Question",20,220,data.colors[data.colorselect][1],0)
                    case 6:
                        self.orangebutton.updatetl("Current Question",20,260,data.colors[data.colorselect][1],0)
                if self.bluebutton.draw(self.display_surface):
                    if self.delta1 > 0.25:
                        data.trivia_shown_color = 0
                if self.pinkbutton.draw(self.display_surface):
                    if self.delta1 > 0.25:
                        data.trivia_shown_color = 1
                if self.yellowbutton.draw(self.display_surface):
                    if self.delta1 > 0.25:
                        data.trivia_shown_color = 2
                if self.purplebutton.draw(self.display_surface):
                    if self.delta1 > 0.25:
                        data.trivia_shown_color = 3
                if self.greenbutton.draw(self.display_surface):
                    if self.delta1 > 0.25:
                        data.trivia_shown_color = 4
                if self.orangebutton.draw(self.display_surface):
                    if self.delta1 > 0.25:
                        data.trivia_shown_color = 5
        #print(data.trivia_location)
        #print(data.trivia_shown_color)
        #print(data.trivia_color)
        text_surf2 = self.font.render(data.questions[data.trivia_question][data.trivia_shown_color][0][0],False,data.colors[data.colorselect][1])
        text_rect2 = text_surf2.get_frect(center = (data.WINDOW_WIDTH/2,70))
        self.display_surface.blit(text_surf2, text_rect2)
        text_surf3 = self.font.render(data.questions[data.trivia_question][data.trivia_shown_color][0][1],False,data.colors[data.colorselect][1])
        text_rect3 = text_surf3.get_frect(center = (data.WINDOW_WIDTH/2,110))
        self.display_surface.blit(text_surf3, text_rect3)
        text_surf4 = self.font.render(data.questions[data.trivia_question][data.trivia_shown_color][0][2],False,data.colors[data.colorselect][1])
        text_rect4 = text_surf4.get_frect(center = (data.WINDOW_WIDTH/2,150))
        self.display_surface.blit(text_surf4, text_rect4)
        text_surf5 = self.font.render(data.questions[data.trivia_question][data.trivia_shown_color][0][3],False,data.colors[data.colorselect][1])
        text_rect5 = text_surf5.get_frect(center = (data.WINDOW_WIDTH/2,190))
        self.display_surface.blit(text_surf5, text_rect5)
        if data.answered_questions[data.trivia_question][data.trivia_shown_color][0] == 1:
            text_surf6 = self.font.render("Question Already Answered",False,data.colors[data.colorselect][1])
            text_rect6 = text_surf6.get_frect(center = (data.WINDOW_WIDTH/2,30))
            self.display_surface.blit(text_surf6, text_rect6)
        else:
            text_surf6 = self.font.render("Question Not Answered",False,data.colors[data.colorselect][1])
            text_rect6 = text_surf6.get_frect(center = (data.WINDOW_WIDTH/2,30))
            self.display_surface.blit(text_surf6, text_rect6)
        self.answer1button.updatec(data.questions[data.trivia_question][data.trivia_shown_color][1][0],data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2,data.colors[data.colorselect][1],0)
        self.answer2button.updatec(data.questions[data.trivia_question][data.trivia_shown_color][1][1],data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2+40,data.colors[data.colorselect][1],0)
        self.answer3button.updatec(data.questions[data.trivia_question][data.trivia_shown_color][1][2],data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2+80,data.colors[data.colorselect][1],0)
        self.answer4button.updatec(data.questions[data.trivia_question][data.trivia_shown_color][1][3],data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2+120,data.colors[data.colorselect][1],0)
        if self.answer1button.draw(self.display_surface):
            if self.delta1 > 0.5:
                if data.questions[data.trivia_question][data.trivia_shown_color][2][0]:
                    data.trivia_last_question = True
                    data.trivia_question_charge = True
                    data.trivia_enabled = True
                    data.trivia_state = 1
                    if data.answered_questions[data.trivia_question][data.trivia_shown_color][0] == 0:
                        if data.archipelagoactive and data.enable_trivia_questions and data.enable_trivial_pursuit:
                            data.checked_locations_player.add(data.answered_questions[data.trivia_question][data.trivia_shown_color][1])
                            data.queued_events.append(LocationClearedEvent(data.answered_questions[data.trivia_question][data.trivia_shown_color][1]))
                        else:
                            data.speedups += 1
                    data.answered_questions[data.trivia_question][data.trivia_shown_color][0] = 1
                    match data.trivia_location:
                        case 31:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[0][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[0][1]))
                                data.trivia_wedges[0][2] = True
                            else:
                                data.trivia_wedges[0][0] = 1
                                data.trivia_wedges[0][2] = True
                        case 38:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[1][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[1][1]))
                                data.trivia_wedges[1][2] = True
                            else:
                                data.trivia_wedges[1][0] = 1
                                data.trivia_wedges[1][2] = True
                        case 45:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[2][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[2][1]))
                                data.trivia_wedges[2][2] = True
                            else:
                                data.trivia_wedges[2][0] = 1
                                data.trivia_wedges[2][2] = True
                        case 52:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[3][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[3][1]))
                                data.trivia_wedges[3][2] = True
                            else:
                                data.trivia_wedges[3][0] = 1
                                data.trivia_wedges[3][2] = True
                        case 59:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[4][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[4][1]))
                                data.trivia_wedges[4][2] = True
                            else:
                                data.trivia_wedges[4][0] = 1
                                data.trivia_wedges[4][2] = True
                        case 66:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[5][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[5][1]))
                                data.trivia_wedges[5][2] = True
                            else:
                                data.trivia_wedges[5][0] = 1
                                data.trivia_wedges[5][2] = True
                    if self.final_question:
                        data.trivia_goal = True
                        data.trivia_state = 6
                else:
                    data.trivia_last_question = False
                    data.trivia_state = 5
                    self.final_question = False
                    match data.trivia_location:
                        case 31:
                            if data.trivia_wedges[0][0] == 1:
                                data.trivia_wedges[0][2] = False
                        case 38:
                            if data.trivia_wedges[1][0] == 1:
                                data.trivia_wedges[1][2] = False
                        case 45:
                            if data.trivia_wedges[2][0] == 1:
                                data.trivia_wedges[2][2] = False
                        case 52:
                            if data.trivia_wedges[3][0] == 1:
                                data.trivia_wedges[3][2] = False
                        case 59:
                            if data.trivia_wedges[4][0] == 1:
                                data.trivia_wedges[4][2] = False
                        case 66:
                            if data.trivia_wedges[5][0] == 1:
                                data.trivia_wedges[5][2] = False
                    if data.trivia_enabled and data.trivia_wedges[5][0] == 1:
                        data.trivia_penalty = 30
                    else:
                        data.trivia_penalty = 60
                data.trivia_need_question = False
                data.trivia_move = False
                data.trivia_need_direction = True
                data.trivia_used_blue = False
                data.trivia_used_green = False
                data.trivia_last_direction = 0
        if self.answer2button.draw(self.display_surface):
            if self.delta1 > 0.5:
                if data.questions[data.trivia_question][data.trivia_shown_color][2][1]:
                    data.trivia_last_question = True
                    data.trivia_question_charge = True
                    data.trivia_enabled = True
                    data.trivia_state = 1
                    if data.answered_questions[data.trivia_question][data.trivia_shown_color][0] == 0:
                        if data.archipelagoactive and data.enable_trivia_questions and data.enable_trivial_pursuit:
                            data.checked_locations_player.add(data.answered_questions[data.trivia_question][data.trivia_shown_color][1])
                            data.queued_events.append(LocationClearedEvent(data.answered_questions[data.trivia_question][data.trivia_shown_color][1]))
                        else:
                            data.speedups += 1
                    data.answered_questions[data.trivia_question][data.trivia_shown_color][0] = 1
                    match data.trivia_location:
                        case 31:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[0][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[0][1]))
                                data.trivia_wedges[0][2] = True
                            else:
                                data.trivia_wedges[0][0] = 1
                                data.trivia_wedges[0][2] = True
                        case 38:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[1][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[1][1]))
                                data.trivia_wedges[1][2] = True
                            else:
                                data.trivia_wedges[1][0] = 1
                                data.trivia_wedges[1][2] = True
                        case 45:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[2][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[2][1]))
                                data.trivia_wedges[2][2] = True
                            else:
                                data.trivia_wedges[2][0] = 1
                                data.trivia_wedges[2][2] = True
                        case 52:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[3][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[3][1]))
                                data.trivia_wedges[3][2] = True
                            else:
                                data.trivia_wedges[3][0] = 1
                                data.trivia_wedges[3][2] = True
                        case 59:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[4][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[4][1]))
                                data.trivia_wedges[4][2] = True
                            else:
                                data.trivia_wedges[4][0] = 1
                                data.trivia_wedges[4][2] = True
                        case 66:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[5][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[5][1]))
                                data.trivia_wedges[5][2] = True
                            else:
                                data.trivia_wedges[5][0] = 1
                                data.trivia_wedges[5][2] = True
                    if self.final_question:
                        data.trivia_goal = True
                        data.trivia_state = 6
                else:
                    data.trivia_last_question = False
                    data.trivia_state = 5
                    self.final_question = False
                    match data.trivia_location:
                        case 31:
                            if data.trivia_wedges[0][0] == 1:
                                data.trivia_wedges[0][2] = False
                        case 38:
                            if data.trivia_wedges[1][0] == 1:
                                data.trivia_wedges[1][2] = False
                        case 45:
                            if data.trivia_wedges[2][0] == 1:
                                data.trivia_wedges[2][2] = False
                        case 52:
                            if data.trivia_wedges[3][0] == 1:
                                data.trivia_wedges[3][2] = False
                        case 59:
                            if data.trivia_wedges[4][0] == 1:
                                data.trivia_wedges[4][2] = False
                        case 66:
                            if data.trivia_wedges[5][0] == 1:
                                data.trivia_wedges[5][2] = False
                    if data.trivia_enabled and data.trivia_wedges[5][0] == 1:
                        data.trivia_penalty = 30
                    else:
                        data.trivia_penalty = 60
                data.trivia_need_question = False
                data.trivia_move = False
                data.trivia_need_direction = True
                data.trivia_used_blue = False
                data.trivia_used_green = False
                data.trivia_last_direction = 0
        if self.answer3button.draw(self.display_surface):
            if self.delta1 > 0.5:
                if data.questions[data.trivia_question][data.trivia_shown_color][2][2]:
                    data.trivia_last_question = True
                    data.trivia_question_charge = True
                    data.trivia_enabled = True
                    data.trivia_state = 1
                    if data.answered_questions[data.trivia_question][data.trivia_shown_color][0] == 0:
                        if data.archipelagoactive and data.enable_trivia_questions and data.enable_trivial_pursuit:
                            data.checked_locations_player.add(data.answered_questions[data.trivia_question][data.trivia_shown_color][1])
                            data.queued_events.append(LocationClearedEvent(data.answered_questions[data.trivia_question][data.trivia_shown_color][1]))
                        else:
                            data.speedups += 1
                    data.answered_questions[data.trivia_question][data.trivia_shown_color][0] = 1
                    match data.trivia_location:
                        case 31:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[0][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[0][1]))
                                data.trivia_wedges[0][2] = True
                            else:
                                data.trivia_wedges[0][0] = 1
                                data.trivia_wedges[0][2] = True
                        case 38:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[1][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[1][1]))
                                data.trivia_wedges[1][2] = True
                            else:
                                data.trivia_wedges[1][0] = 1
                                data.trivia_wedges[1][2] = True
                        case 45:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[2][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[2][1]))
                                data.trivia_wedges[2][2] = True
                            else:
                                data.trivia_wedges[2][0] = 1
                                data.trivia_wedges[2][2] = True
                        case 52:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[3][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[3][1]))
                                data.trivia_wedges[3][2] = True
                            else:
                                data.trivia_wedges[3][0] = 1
                                data.trivia_wedges[3][2] = True
                        case 59:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[4][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[4][1]))
                                data.trivia_wedges[4][2] = True
                            else:
                                data.trivia_wedges[4][0] = 1
                                data.trivia_wedges[4][2] = True
                        case 66:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[5][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[5][1]))
                                data.trivia_wedges[5][2] = True
                            else:
                                data.trivia_wedges[5][0] = 1
                                data.trivia_wedges[5][2] = True
                    if self.final_question:
                        data.trivia_goal = True
                        data.trivia_state = 6
                else:
                    data.trivia_last_question = False
                    data.trivia_state = 5
                    self.final_question = False
                    match data.trivia_location:
                        case 31:
                            if data.trivia_wedges[0][0] == 1:
                                data.trivia_wedges[0][2] = False
                        case 38:
                            if data.trivia_wedges[1][0] == 1:
                                data.trivia_wedges[1][2] = False
                        case 45:
                            if data.trivia_wedges[2][0] == 1:
                                data.trivia_wedges[2][2] = False
                        case 52:
                            if data.trivia_wedges[3][0] == 1:
                                data.trivia_wedges[3][2] = False
                        case 59:
                            if data.trivia_wedges[4][0] == 1:
                                data.trivia_wedges[4][2] = False
                        case 66:
                            if data.trivia_wedges[5][0] == 1:
                                data.trivia_wedges[5][2] = False
                    if data.trivia_enabled and data.trivia_wedges[5][0] == 1:
                        data.trivia_penalty = 30
                    else:
                        data.trivia_penalty = 60
                data.trivia_need_question = False
                data.trivia_move = False
                data.trivia_need_direction = True
                data.trivia_used_blue = False
                data.trivia_used_green = False
                data.trivia_last_direction = 0
        if self.answer4button.draw(self.display_surface):
            if self.delta1 > 0.5:
                if data.questions[data.trivia_question][data.trivia_shown_color][2][3]:
                    data.trivia_last_question = True
                    data.trivia_question_charge = True
                    data.trivia_enabled = True
                    data.trivia_state = 1
                    if data.answered_questions[data.trivia_question][data.trivia_shown_color][0] == 0:
                        if data.archipelagoactive and data.enable_trivia_questions and data.enable_trivial_pursuit:
                            data.checked_locations_player.add(data.answered_questions[data.trivia_question][data.trivia_shown_color][1])
                            data.queued_events.append(LocationClearedEvent(data.answered_questions[data.trivia_question][data.trivia_shown_color][1]))
                        else:
                            data.speedups += 1
                    data.answered_questions[data.trivia_question][data.trivia_shown_color][0] = 1
                    match data.trivia_location:
                        case 31:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[0][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[0][1]))
                                data.trivia_wedges[0][2] = True
                            else:
                                data.trivia_wedges[0][0] = 1
                                data.trivia_wedges[0][2] = True
                        case 38:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[1][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[1][1]))
                                data.trivia_wedges[1][2] = True
                            else:
                                data.trivia_wedges[1][0] = 1
                                data.trivia_wedges[1][2] = True
                        case 45:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[2][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[2][1]))
                                data.trivia_wedges[2][2] = True
                            else:
                                data.trivia_wedges[2][0] = 1
                                data.trivia_wedges[2][2] = True
                        case 52:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[3][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[3][1]))
                                data.trivia_wedges[3][2] = True
                            else:
                                data.trivia_wedges[3][0] = 1
                                data.trivia_wedges[3][2] = True
                        case 59:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[4][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[4][1]))
                                data.trivia_wedges[4][2] = True
                            else:
                                data.trivia_wedges[4][0] = 1
                                data.trivia_wedges[4][2] = True
                        case 66:
                            if data.archipelagoactive and data.enable_trivial_pursuit:
                                data.checked_locations_player.add(data.trivia_wedges[5][1])
                                data.queued_events.append(LocationClearedEvent(data.trivia_wedges[5][1]))
                                data.trivia_wedges[5][2] = True
                            else:
                                data.trivia_wedges[5][0] = 1
                                data.trivia_wedges[5][2] = True
                    if self.final_question:
                        data.trivia_goal = True
                        data.trivia_state = 6
                else:
                    data.trivia_last_question = False
                    data.trivia_state = 5
                    self.final_question = False
                    match data.trivia_location:
                        case 31:
                            if data.trivia_wedges[0][0] == 1:
                                data.trivia_wedges[0][2] = False
                        case 38:
                            if data.trivia_wedges[1][0] == 1:
                                data.trivia_wedges[1][2] = False
                        case 45:
                            if data.trivia_wedges[2][0] == 1:
                                data.trivia_wedges[2][2] = False
                        case 52:
                            if data.trivia_wedges[3][0] == 1:
                                data.trivia_wedges[3][2] = False
                        case 59:
                            if data.trivia_wedges[4][0] == 1:
                                data.trivia_wedges[4][2] = False
                        case 66:
                            if data.trivia_wedges[5][0] == 1:
                                data.trivia_wedges[5][2] = False
                    if data.trivia_enabled and data.trivia_wedges[5][0] == 1:
                        data.trivia_penalty = 30
                    else:
                        data.trivia_penalty = 60
                data.trivia_need_question = False
                data.trivia_move = False
                data.trivia_need_direction = True
                data.trivia_used_blue = False
                data.trivia_used_green = False
                data.trivia_last_direction = 0

    def display_penalty(self,data,dt):
        text_surf = self.font.render("Incorrect",False,data.colors[data.colorselect][1])
        text_rect = text_surf.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT-80))
        self.display_surface.blit(text_surf, text_rect)
        text_surf2 = self.font.render("Penalty Time: " + str(round(data.trivia_penalty,3)) + " Seconds",False,data.colors[data.colorselect][1])
        text_rect2 = text_surf2.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT-40))
        self.display_surface.blit(text_surf2, text_rect2)
        if data.trivia_penalty <= 0:
            data.trivia_state = 1
        data.trivia_penalty -= dt

    def display_victory(self,data,dt):
        text_surf = self.font.render("You did it...",False,data.colors[data.colorselect][1])
        text_rect = text_surf.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2-120))
        self.display_surface.blit(text_surf, text_rect)
        if self.delta1 > 2 :
            text_surf2 = self.font.render("You beat Acceleracers Trivial Pursuit",False,data.colors[data.colorselect][1])
            text_rect2 = text_surf2.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2-80))
            self.display_surface.blit(text_surf2, text_rect2)
            if self.delta1 > 4 :
                text_surf3 = self.font.render("Good Job",False,data.colors[data.colorselect][1])
                text_rect3 = text_surf3.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2-40))
                self.display_surface.blit(text_surf3, text_rect3)
                if self.delta1 > 6:
                    text_surf4 = self.font.render("I'm sure you had a great time",False,data.colors[data.colorselect][1])
                    text_rect4 = text_surf4.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2))
                    self.display_surface.blit(text_surf4, text_rect4)
                    if self.delta1 > 8:
                        text_surf5 = self.font.render("I mean why play NOTHING, when can Acceleracers Trivial Pursuit",False,data.colors[data.colorselect][1])
                        text_rect5 = text_surf5.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2+40))
                        self.display_surface.blit(text_surf5, text_rect5)
                        if self.delta1 > 10:
                            text_surf6 = self.font.render("Since you've already come this far...",False,data.colors[data.colorselect][1])
                            text_rect6 = text_surf6.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2+80))
                            self.display_surface.blit(text_surf6, text_rect6)
                            if self.delta1 > 12:
                                text_surf7 = self.font.render("You might as well answer the rest of the questions",False,data.colors[data.colorselect][1])
                                text_rect7 = text_surf7.get_frect(center = (data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2+120))
                                self.display_surface.blit(text_surf7, text_rect7)
                                if self.delta1 > 14:
                                    self.continuebutton.updatec("[CONTINUE]",data.WINDOW_WIDTH/2,data.WINDOW_HEIGHT/2+160,data.colors[data.colorselect][1],1)
                                    if self.continuebutton.draw(self.display_surface):
                                        data.trivia_state = 1
                                        self.delta1 = 0
        self.delta1 += dt

    def display_return(self,data):
        self.returntonothingbutton.updatec("Return to Doing Nothing",data.WINDOW_WIDTH-200,data.WINDOW_HEIGHT-20,data.colors[data.colorselect][1],0)
        if self.returntonothingbutton.draw(self.display_surface):
            data.playingstate = 1
            self.delta1 = 0

    def update(self,data,dt):
        if data.playingstate == -4:
            if data.trivia_state == 0:
                if data.trivia_intro == False:
                    self.display_intro(data,dt)
                else:
                    self.display_team_select(data,dt)
            elif data.trivia_state == 1:
                self.display_board(data)
                self.display_roll(data,dt)
            elif data.trivia_state == 2:
                self.display_board(data)
                self.display_abilities(data,dt)
                self.display_moves(data,dt)
            elif data.trivia_state == 3:
                self.display_board(data)
                self.display_moves(data,dt)
                self.moving(data)
            elif data.trivia_state == 4:
                if data.trivia_need_question:
                    self.display_questions(data,dt)
                else:
                    self.display_board(data)
                self.display_question_select(data,dt)
            elif data.trivia_state == 5:
                self.display_board(data)
                self.display_penalty(data,dt)
            elif data.trivia_state == 6:
                self.display_victory(data,dt)
            self.display_return(data)