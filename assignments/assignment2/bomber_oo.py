from tkinter import *
from tkinter import font
from math import sqrt
from random import *
from time import time
import random

#some global constants
CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 700
SPACING = 100

speed = 1.0

class Point(object):
    '''Creates a point on a coordinate plane with values x and y.'''
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    '''create a new object from this one.  we use this when we want to
       create a modified copy of a point without modifying the original object'''
    def copy(self):
        return Point(self.X, self.Y)

    ''' vector addition of points '''
    def add(self, other):
        self.X = self.X + other.X
        self.Y = self.Y + other.Y

    def move(self, dx, dy):
        self.X = self.X + dx
        self.Y = self.Y + dy

    def __str__(self):
        return "Point(%s,%s)"%(self.X, self.Y) 

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return sqrt(dx*dx + dy*dy)

''' update_position takes a list of x and y coordinates and a Point.
    It creates a new list of x and y coordintes by adding the Point to all
    the coordintes from the original list '''    
def update_position(position_list, position):
    newlist = []
    is_x = True;
    for val in position_list:
        if is_x:
            newlist.append(val + position.getX())
        else:
            newlist.append(val + position.getY())
        is_x = not is_x
    return newlist


''' The Building class holds all the state associated with one building '''
class Building():
    
    
    def __init__(self, canvas, building_num, height, width,):
        self.canvas = canvas
        self.height = height
        self.x = building_num*SPACING
        self.width = width

        if self.x >= CANVAS_WIDTH:
            return
        self.main_rect = canvas.create_rectangle(self.x, CANVAS_HEIGHT, self.x + self.width, CANVAS_HEIGHT-self.height, fill="brown")
        

    ''' is_inside tests if a point is inside the building '''
    def is_inside(self, point):
        if point.X < self.x or point.X > self.x + self.width or point.Y < CANVAS_HEIGHT-self.height:
            return False
        return True

    ''' shrink the building when a bomb drops on it '''
    def shrink(self):
        if self.height <= 0:
            self.cleanup()
            print("Building destroyed")
        self.height = self.height - 50
        self.canvas.delete(self.main_rect)
        COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
        'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
        'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
        'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
        'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
        'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
        'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
        'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
        'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
        'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
        'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
        'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
        'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
        'indian red', 'saddle brown', 'sandy brown',
        'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
        'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
        'pale violet red', 'maroon', 'medium violet red', 'violet red',
        'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
        'thistle', 'snow2', 'snow3',
        'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
        'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
        'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
        'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
        'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
        'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
        'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
        'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
        'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
        'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
        'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
        'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
        'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
        'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
        'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
        'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
        'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
        'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
        'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
        'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
        'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
        'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
        'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
        'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
        'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
        'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
        'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
        'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
        'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
        'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
        'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
        'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
        'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
        'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
        'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
        'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
        'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
        'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
        'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
        'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
        'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
        'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
        'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
        'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
        'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
        'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
        'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
        'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
        'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
        'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
        'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
        'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
        'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
        'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
        'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
        'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
        'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
        
        self.main_rect = self.canvas.create_rectangle(self.x, CANVAS_HEIGHT, self.x + self.width, CANVAS_HEIGHT-self.height, fill=random.choice(COLORS))
        
    def cleanup(self):
        self.canvas.delete(self.main_rect)

''' The Bomb class holds the state associated with the bomb.  There's
    only one bomb.  Once it explodes it can be reused again '''
class Bomb():
    def __init__(self, canvas):
        self.canvas = canvas
        self.falling = False
        self.drawn = False
        self.position = Point(0,0)
        ''' self.points contains x,y coordinate pairs to draw a bomb with top left
            corner at position 0,0'''
        self.points = [0,0, 10,0, 5,5, 10,10, 10,20, 5,22, 0,20, 0,10, 5,5]
        self.draw()

    ''' draw the bomb at its current position '''
    def draw(self):
        current_points = update_position(self.points, self.position)
        self.polygon = self.canvas.create_polygon(*current_points, fill="black")
        self.drawn = True

    ''' erase the old bomb, and redraw it '''
    def redraw(self):
        if self.drawn:
            self.canvas.delete(self.polygon)
        if self.falling:
            self.draw()

    def move(self):
        if self.falling:
            self.position.move(0, 8 * speed)

    ''' drop the bomb from the plane '''
    def drop(self, point):
        if self.falling:
            # don't drop again while bomb is still falling
            return
        self.falling = True
        # copy the plane's position, rather that taking a reference to it.
        # Note: if we instead do self.position = point, we'll end up
        # changing the plane's position as the bomb falls)
        self.position = point.copy()

    def explode(self):
        self.falling = False

''' The Plane class holds the state associated with the plane. '''
class Plane():
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.start_position = Point(x, y)
        self.position = Point(x, y)
        ''' plane is drawn as four polygons.  The following four lists
            contains x,y coordinate pairs to draw a plane with top
            left corner at position 0,0 '''
        self.body_points = [0,28, 20,16, 120,16, 94,32, 12,32]
        self.wing1_points = [40,28, 76,28, 94,48, 80,48]
        self.wing2_points = [52,16, 78,8, 94,8, 81,16]
        self.tail_points = [90,16, 110,0, 124,0, 116,16]
        self.width = 10 # plane width
        self.draw()

    ''' reset the plane to its starting position at the start of a new level '''
    def reset_position(self):
        self.position = self.start_position.copy()

    def draw(self):
        current_body_points = update_position(self.body_points, self.position)
        current_wing1_points = update_position(self.wing1_points, self.position)
        current_wing2_points = update_position(self.wing2_points, self.position)
        current_tail_points = update_position(self.tail_points, self.position)
        self.body = self.canvas.create_polygon(*current_body_points, fill="red")
        self.wing1 = self.canvas.create_polygon(*current_wing1_points, fill="grey")
        self.wing2 = self.canvas.create_polygon(*current_wing2_points, fill="grey")
        self.tail = self.canvas.create_polygon(*current_tail_points, fill="grey")

    def redraw(self):
        self.canvas.delete(self.body)
        self.canvas.delete(self.wing1)
        self.canvas.delete(self.wing2)
        self.canvas.delete(self.tail)
        self.draw()

    ''' move the plane however much it moves during one frame '''
    def move(self):
        self.position.move(-4 * speed, 0)
        if self.position.getX() < -self.width:
            self.position.move(CANVAS_WIDTH, 40)
            #ensure we don't go off the bottom of the screen
            if self.position.getY() > CANVAS_HEIGHT:
                self.position.Y = CANVAS_HEIGHT
            #we get 10 points each row the plane moves down
            return 10
        else:
            return 0

    def movetoend(self):
        self.position.move(-25 * speed, 0)
        if self.position.getX() < -self.width:
            self.position.move(CANVAS_WIDTH, 40)
            #ensure we don't go off the bottom of the screen
            if self.position.getY() > CANVAS_HEIGHT:
                self.position.Y = CANVAS_HEIGHT
            #we get 10 points each row the plane moves down
            return 10
        else:
            return 0


''' Display is the main class that holds the GUI state and the game state '''
class Display(Frame):
    def __init__(self, root):
        root.wm_title("Bomber")
        self.windowsystem = root.call('tk', 'windowingsystem')
        self.frame = root
        self.canvas = Canvas(self.frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack(side = LEFT, fill=BOTH, expand=FALSE)
        self.init_fonts()
        self.init_score()
        self.rand = Random()

        #create game objects
        self.plane = Plane(self.canvas, CANVAS_WIDTH - 100, 0)
        self.bomb = Bomb(self.canvas)
        self.buildings = []
        self.building_width = SPACING * 0.8
        self.create_buildings()
        self.game_running = True
        self.won = False

    def init_fonts(self):
        self.bigfont = font.nametofont("TkDefaultFont")
        self.bigfont.configure(size=48)
        self.scorefont = font.nametofont("TkDefaultFont")
        self.scorefont.configure(size=20)

    def init_score(self):
        self.score = 0
        self.level = 1
        self.score_text = self.canvas.create_text(5, 5, anchor="nw")
        self.canvas.itemconfig(self.score_text, text="Score:", font=self.scorefont)

    def display_score(self):
        self.canvas.itemconfig(self.score_text, text="Level: " + str(self.level) + "  Score: " + str(self.score), font=self.scorefont)

    ''' create new buildings at the start of a level '''
    def create_buildings(self):
        #remove any old buildings
        while len(self.buildings) > 0:
            building = self.buildings.pop()
            building.cleanup()

        #create the new ones
        for building_num in range(0, 1200//SPACING ):
            height = self.rand.randint(10,500) #random number between 10 and 500
            self.buildings.append(Building(self.canvas, building_num, height,
                                           self.building_width))

    def drop_bomb(self):
        self.bomb.drop(self.plane.position)

    ''' check the state of the bomb each frame '''
    def check_bomb(self):

        if not self.bomb.falling:
            return

        if self.bomb.position.getY() >= CANVAS_HEIGHT - 5:
            self.bomb.explode()

        # did the bomb hit a building?
        for building in self.buildings:
            if building.is_inside(self.bomb.position):
                self.bomb.explode()
                building.shrink()

    ''' check the state of the plane each frame '''
    def check_plane(self):
        # we'll check if the plane nose hits a building, or if the
        # base of the fuselage hits, or if the wing hits
        
        numofdestroyedbuildings = 0
        plane_nose = self.plane.position.copy()
        plane_nose.move(0, 28)
        plane_body_bottom = self.plane.position.copy()
        plane_body_bottom.move(12, 32)
        plane_wing = self.plane.position.copy()
        plane_wing.move(94,48)
        for building in self.buildings:
            if (building.is_inside(plane_nose)
                or building.is_inside(plane_body_bottom)
                or building.is_inside(plane_wing)):
                self.game_over()
            if building.height <= 0:
                numofdestroyedbuildings += 1
                

        if numofdestroyedbuildings == len(self.buildings):
            print("All buildings have been destroyed")
            self.plane.movetoend()
        if plane_body_bottom.getY() == 672 and plane_body_bottom.getX() <= 40:
            print("Plane has landed")
            self.plane_landed()

    ''' game_over is called when the plane crashes to stop play and display the 
        game over message '''
    def game_over(self):
        self.game_running = False
        self.won = False

        self.text = self.canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, anchor="c")
        self.canvas.itemconfig(self.text, text="GAME OVER!", font=self.bigfont)

    ''' plane_landed is called when the plane has landed to stop plane and
        display the success message '''
    def plane_landed(self):
        self.game_running = False
        self.won = True
        self.score = self.score + 1000
        self.display_score()
        self.text = self.canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, anchor="c")
        self.canvas.itemconfig(self.text, text="SUCCESS!", font=self.bigfont)
        self.text2 = self.canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2 + 100, anchor="c")
        self.canvas.itemconfig(self.text2, text="Press n for next level.", font=self.scorefont)

    ''' restart is called after game over to start a new game '''
    def restart(self):
        self.canvas.delete(self.text)
        self.level = 1
        self.score = 0
        self.plane.reset_position()
        self.building_width = SPACING * 0.8
        self.create_buildings()
        self.won = False
        self.game_running = True

    def next_level(self):
        #don't move to next level unless we've actually won!
        if self.won == False:
            return
        
        self.level = self.level + 1
        self.canvas.delete(self.text)
        self.canvas.delete(self.text2)
        self.plane.reset_position()
        # buildings get narrower with each level
        self.building_width = self.building_width * 0.9
        self.create_buildings()
        self.won = False
        self.game_running = True
        
    def update(self):
        if self.game_running:
            self.score = self.score + self.plane.move()
            self.check_plane()
            self.bomb.move()
            self.check_bomb()
            self.plane.redraw()
            self.bomb.redraw()
            self.display_score()

''' the Game class runs the main loop, and initializes tkinter '''
class Game():
    def __init__(self):
        self.root = Tk();
        self.windowsystem = self.root.call('tk', 'windowingsystem')
        self.disp = Display(self.root)
        self.root.bind_all('<Key>', self.key)
        self.running = True
        self.disp.update()
        self.root.update()
        self.lastframe = time()
        self.framecount = 0

    ''' key is called by tkinter whenever a key is pressed '''
    def key(self, event):
        if event.char == ' ':
            self.disp.drop_bomb()
        elif event.char == 'q':
            self.running = False
        elif event.char == 'n':
            self.disp.next_level()
        elif event.char == 'r':
            self.disp.restart()

    ''' adjust game speed so it's more or less the same on different machines '''
    def checkspeed(self):
        global speed
        self.framecount = self.framecount + 1
        # only check every ten frames
        if self.framecount == 10:
            now = time()
            elapsed = now - self.lastframe
            # speed will be 1.0 if we're achieving 60 fps
            if speed == 0:
                #initial speed value
                # At 60fps, 10 frames take 1/6 of a second.
                speed = 6 * elapsed
            else:
                # use an EWMA to damp speed changes and avoid excessive jitter
                speed = speed * 0.9 + 0.1 * 6 * elapsed
            self.lastframe = now
            self.framecount = 0

    def run(self):
        while self.running:
            self.disp.update()
            self.root.update()
            self.checkspeed()
        self.root.destroy()

game = Game()
game.run()
