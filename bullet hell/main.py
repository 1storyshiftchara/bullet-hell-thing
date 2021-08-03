import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
print("start")
import pygame
import time
import random
from shapes import *
# dont touch
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
skyblue = (135,206,235)
#colors

pygame.init()
pygame.font.init()
#makes stuff work
infos = pygame.display.Info()
screen_size = (infos.current_w, infos.current_h)
(width,height) = screen_size
width=int(width/2)+100
height=height-100
#window stuff
global fillcol;fillcol = (0,0,0)
global globalticks; globalticks = 0
global localticks; localticks=0
# time stuff
screen = pygame.display.set_mode((width, height))
camerax = 0
cameray = 0
effectivewidth = width-200
# more window stuff
maps = []
mapthing = mapp([
spawner(75,75,effectivewidth/2,height,10,5,25,blue,False,10,30),
spawner(effectivewidth-75,75,effectivewidth/2,height,10,5,25,blue,False,10,30),
spawner(effectivewidth/2,75,effectivewidth/2,height,10,2,50,blue,False,100,60),
spawner(effectivewidth-75,75,effectivewidth/2,height,10,5,25,blue,False,10,140),
spawner(75,75,effectivewidth/2,height,10,5,25,blue,False,10,140)]
,skyblue)
maps.append(mapthing)
#^ change this for changing when/how bullets appear
# spawner(startx,starty,endx,endy,bulletspeed,delay between bullets,radius of bullets,color,is from player,amount of bullets,time to start firing)
# put is from player to false for it to be able to damage the player


running = True
objects = [circle(500,500,25,red,screen)]
health=10
objects.append(spawner(objects[0].x-50,objects[0].y,objects[0].x-50,0,10,1,5,white,True,9999,0))
objects.append(spawner(objects[0].x+50,objects[0].y,objects[0].x+50,0,10,1,5,white,True,9999,0))
# player stuff



font = pygame.font.SysFont('martinaregular',30)
global stage; stage = 0
def loadmap(map1):
    global stage; stage = 1
    global fillcol; fillcol = map1.background
    global localticks; localticks=0
    for thing in map1.data:
        objects.append(thing)
loadmap(maps[0]) 
# loads in maps 
keys = []
# stores keyd
controllable = True
# if its false the player cant move
#mouse = pygame.mouse


menucolor = (50,0,0)
menutext = (169,169,169)
while running:
    #(mousex,mousey) = mouse.get_pos()
    #ignore
    objects[1].startx=objects[0].x-50
    objects[2].startx=objects[0].x+50
    objects[1].endx=objects[0].x-50
    objects[2].endx=objects[0].x+50
    objects[1].starty=objects[0].y
    objects[2].starty=objects[0].y
    # locks side bullets to player
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys.append(pygame.key.name(event.key))
        elif event.type == pygame.KEYUP:
            keys.remove(pygame.key.name(event.key))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # yea it doesnt sence
            if event.button == 1:
                keys.append('mouse1')
            elif event.button == 2:
                keys.append('mouse3')
            elif event.button == 3:
                keys.append('mouse2')
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                keys.remove('mouse1')
            elif event.button == 2:
                keys.remove('mouse3')
            elif event.button == 3:
                keys.remove('mouse2')
    # controls and closing the game
    for z in objects:
        offsetx = camerax
        offsety = cameray
        
        z.rendered = False
        if z.type == 'Rect':
            if z.y>height+cameray or z.y+z.h<cameray:
                # checks if its above or below the screen
                continue
            if z.x+z.w<camerax or z.x>effectivewidth+camerax:
                # checks if its to the left or the right of the screen
                continue
        elif z.type == 'Circle':
            if z.y-z.r>height+cameray or z.y+z.r<cameray:
                # checks if its below or above the screen
                continue
            if z.x-z.r>effectivewidth+camerax or z.x+z.r<camerax:
                # check if its to the left or the right of the screen
                continue
        # makes sure the object will be seen
        z.rendered = True
        # means that its being rendered
        z.display(camerax,cameray)
        if z.type == 'Bullet':
            if z.allegience==False:
                if z.testcollision(objects[0]):
                    health-=1
            if z.x==z.endx and z.y==z.endy:
                objects.remove(z)
                continue
            z.x+=(z.endx-z.startx)/z.speed
            z.y+=(z.endy-z.starty)/z.speed
        elif z.type == 'Spawner':
            if z.tick==localticks:
                z.tick+=z.delay
                z.amount-=1
                objects.append(bullet(z.startx,z.starty,z.size,z.c,screen,z.endx,z.endy,z.speed,z.allegience))
            if z.amount==0:
                objects.remove(z)
                continue
        if z == objects[0] and controllable:
            width1 = 0
            height1 = 0
            left = 0
            right = 0
            up = 0
            down = 0
            if z.type == 'Circle':
                width1 = z.r
                height1=z.r
                left = z.x-z.r
                right = z.x+z.r
                up = z.y-z.r
                down = z.y+z.r
            elif z.type == 'Rect':
                width1=z.w
                height1=z.h
                left = z.x
                up = z.y
                down = z.y+z.h
                right = z.x+z.w
            for q in keys:
                    if q == 'a':
                        objects[0].x-=width1
                        if (left<=0):
                            objects[0].x+=width1
                    elif q == 'd':
                        objects[0].x+=width1
                        if (right>=effectivewidth):
                            objects[0].x-=width1
                    elif q == 's':
                        objects[0].y+=height1
                        if (down>=height):
                            objects[0].y-=height1
                    elif q == 'w':
                        objects[0].y-=height1
                        if (up<=0):
                            objects[0].y+=height1
    # rendering stuff            
    pygame.draw.rect(screen,menucolor, pygame.Rect(effectivewidth,0,(width-effectivewidth),height))   
    healthsurface = font.render('Health:{}'.format(health), False, menutext)
    stagesurface = font.render('stage:{}'.format(stage), False, menutext)       
    screen.blit(healthsurface,(width-150,50))
    screen.blit(stagesurface,(width-150,300))
    # side menu
                        
    
    pygame.display.flip()
    screen.fill(fillcol)
    time.sleep(0.06)
    localticks+=1
    globalticks+=1
    # dont touch