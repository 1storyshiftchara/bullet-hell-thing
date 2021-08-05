import pygame
import math
class rectt (object):
    def __init__(self,x,y,w,h,color,screen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = color
        self.s = screen
        self.type = 'Rect'
        self.rendered = True
    def display(self,changex,changey):
        if changex==None:
            changex=0
        if changey==None:
            changey=0
        pygame.draw.rect(self.s, self.c, pygame.Rect(self.x-changex,self.y-changey,self.w,self.h))
    def testcollision(self,other):
            if other.type == 'Rect':
                endx=self.x+self.w
                endy=self.y+self.h
                endxx=other.x+other.w
                endyy=other.y+other.h
                endx-=50
                endy-=50
                endxx-=50
                endyy-=50
                # gets the right and bottom edges of each shape
                if self.x<=endxx and endx>=other.x:
                    # colliding on the x axis
                    if self.y<=endyy and endy>=other.y:
                        # colliding on the y axis
                        return True
                        # collision
                return False
            elif other.type == 'Circle':
                endx=self.x+self.w
                endy=self.y+self.h
                endxx=other.x+(other.r/2)
                endyy=other.y+(other.r/2)
                # gets the right and bottom edges of each shape
                if self.x<=endxx and endx>=other.x-(other.r/2):
                    # colliding on the x axis
                    if self.y<=endyy and endy>=other.y-(other.r/2):
                        # colliding on the y axis
                        return True
                        # collision
                return False         
class circle(object):
    def __init__(self,x,y,r,color,screen):
        self.x=x
        self.y=y
        self.r=r
        self.c = color
        self.s = screen
        self.type = 'Circle'
        self.rendered = True
    def display(self,changex,changey):
        if changex==None:
            changex=0
        if changey==None:
            changey=0
        pygame.draw.circle(self.s, self.c, (self.x-changex,self.y-changey),self.r)
        pygame.draw.circle(self.s, self.c, (self.x-changex,self.y-changey),self.r)
        #stops stuff from becoming transparent
    def testcollision(self,other):
            if other.type == 'Rect':
                # originally had circle-rect collision but the method didnt work
                # http://www.jeffreythompson.org/collision-detection/circle-rect.php
                endx=self.x+(self.r/2)
                endy=self.y+(self.r/2)
                endxx=other.x+other.w
                endyy=other.y+other.h
                 # gets the right and bottom edges of each shape
                if self.x-(self.r/2)<=endxx and endx>=other.x:
                # colliding on the x axis
                    if self.y-(self.r/2)<=endyy and endy>=other.y:
                    # colliding on the y axis
                        return True
                    # collision
                return False
            elif other.type == 'Circle':
                distancex = other.x-self.x
                distancey= other.y-self.y
                distance = math.sqrt(distancex*distancex + distancey*distancey)
                # gets distance
                if distance<other.r+self.r:
                    return True
                # collision
                return False
            elif other.type == 'Bullet':
                distancex = other.x-self.x
                distancey= other.y-self.y
                distance = math.sqrt(distancex*distancex + distancey*distancey)
                # gets distance
                if distance<other.r+self.r:
                    return True
                # collision
                return False
class bullet(circle):
    def __init__(self,x,y,r,color,screen,endx,endy,speed,allegience):
        self.x=x
        self.y=y
        self.r=r
        self.c = color
        self.s = screen
        self.type = 'Bullet'
        self.rendered = True
        self.endx = endx
        self.endy = endy
        self.startx = x
        self.starty = y
        self.speed= speed
        self.allegience = allegience
class spawner(object):
    def __init__(self,startx,starty,endx,endy,speed,delay,size,color,allegience,amount,spawntime):
        self.startx=startx
        self.starty=starty
        self.endx=endx
        self.endy=endy
        self.speed=speed
        self.delay=delay
        self.tick=spawntime
        self.type = 'Spawner'
        self.size = size
        self.c = color
        self.allegience = allegience
        self.amount=amount
        self.spawn=spawntime
        #if tick = 0 fire then tick = delay
    def display(thing,thing2,thing3):
        pass
        # this is just here so the entire thing doesnt crash when the rendering part trys to call the display function
class mapp(object):
    def __init__ (self,data,background):
        self.data = data
        self.background = background
    def loadmap(self):
        return (self.data,self.background)