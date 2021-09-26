import pygame, re
from time import sleep
from pygame.image import save
from filestuff import *
pygame.init()


class upgrade(object):
    def __init__(self,cost,text,name):
        self.cost=cost
        self.text=text
        self.name=name

saveobject = open("data.txt","r")
savedata = []
for line in saveobject:
    line = line.strip("\n")
    savedata.append(int(line))

while (len(savedata)<=11):
    savedata.append(0)
saveobject.close()
savedata[11]=list(str(savedata[11]))
if (len(savedata[11])<6):
    i = len(savedata[11])
    while i<6:
        i+=1
        savedata[11]+="0"



i=0
while (i<len(savedata[11])):
    
    savedata[11][i]=int(savedata[11][i])
    i+=1
i=0
curupgrade = 0
for x in savedata[11]:
    if (x==1):
        print(i)
        curupgrade=i+1
        break
    i+=1


print(savedata)

window = pygame.display.set_mode((1000,800))

upgrades = [upgrade(100,"doubles the size of your spoon!","comically larger spoon")]

red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
brown = (160,82,45)
Running = True

keys = []
mousedown = False




font = pygame.font.SysFont('martinaregular',30)


font2 = pygame.font.SysFont('rondaloregular',20)

images = []
images.append(getimage("spoon.png"))
images[0]=pygame.transform.scale(images[0],(200,200))



pygame.display.set_icon(pygame.transform.scale(getimage("spoon2.png"),(32,32)))
print(savedata[11])
spc=1*savedata[11][0]+1
frame = 0


def buy1():
    if (frame!=0):
        if (savedata[0]>=(savedata[1]+1)*savedata[1]+10) and gridy==0:
            savedata[0]-=(savedata[1]+1)*savedata[1]+10
            savedata[1]+=1
    return "1"
def buy2():
    if (frame!=0):
        if (savedata[0]>=(savedata[2]+1)*(savedata[2]*10)+100) and gridy==1:
            savedata[0]-=(savedata[2]+1)*(savedata[2]*10)+100
            savedata[2]+=1
    return "2"
def buy3():
    if (frame!=0):
        if (savedata[0]>=(savedata[3]+1)*(savedata[3]*500)+1000):
            savedata[0]-=(savedata[3]+1)*(savedata[3]*500)+1000
            savedata[3]+=1
    return "3"
def buy4():
    if (frame!=0):
        if (savedata[0]>=(savedata[4]+1)*(savedata[4]*1000)+2500):
            savedata[0]-=(savedata[4]+1)*(savedata[4]*1000)+2500
            savedata[4]+=1
buyswitch = {"0":buy1,"1":buy2,"2":buy3,"3":buy4}
millnames = ["","K","M","B","T","Quad","Quint","Sext","Sept","Oct","Non","Dec","Und","Duo","Tre"]
while Running:
    (mousex,mousey)= pygame.mouse.get_pos()
    gridx = int(mousex/50)
    gridy = int(mousey/50)
    mousedownthisframe = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys.append(pygame.key.name(event.key))
        elif event.type == pygame.KEYUP:
            keys.remove(pygame.key.name(event.key))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousedown=True
            mousedownthisframe = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mousedown=False
        elif event.type == pygame.QUIT:
            Running = False
            pygame.quit()
            break
        #sadly python doesnt have switch statements
    if (Running):
        
        pygame.draw.rect(window,brown,pygame.Rect(0,0,600,800))
        pygame.draw.rect(window,white,pygame.Rect(0,0,301,799),1)
        i = 0
        while i <=10:
            pygame.draw.rect(window,white,pygame.Rect(300,50*i,300,50),1)
            i+=1
        pygame.draw.rect(window,white,pygame.Rect(300,550,300,250),1)
        sps = (savedata[1]*savedata[11][1]+1)+((savedata[2]*10)*savedata[11][2]+1)+((savedata[3]*100)*savedata[11][3]+1)+((savedata[4]*100)*savedata[11][4]+1)
        if (frame%60==0):
            savedata[0]+=sps
            
        if (mousedownthisframe and gridx>=1 and gridx<=4 and gridy>=5 and gridy<=8):
            savedata[0]+=spc
        elif (gridx>=5 and gridx<=11 and mousedownthisframe):
            if (gridy<11):
                #buy time
                try:
                    buyswitch[str(gridy)]()
                except:
                    print("tba")
            cost = upgrades[curupgrade].cost
            if (cost<savedata[0]):
                #can afford
                if (curupgrade==0):
                    sps*=2
                savedata[11][curupgrade]=1
                curupgrade+=1
                
            #upgrade time
        
        
        cappedspoonfulls=""
        arrspoons = list(str(savedata[0]))
        length = len(arrspoons)-1
        if (length-3>=0):
            i=int(length/3)
            i2=(length/3)
            if (i2-i==0):
                cappedspoonfulls+=arrspoons[0]
            elif (i2-i<0.66):
                cappedspoonfulls+=arrspoons[0]
                cappedspoonfulls+=arrspoons[1]
            else:
                cappedspoonfulls+=arrspoons[0]
                cappedspoonfulls+=arrspoons[1]
                cappedspoonfulls+=arrspoons[2]
            cappedspoonfulls+=millnames[i]


            
        else:
            cappedspoonfulls=savedata[0]
        
        window.blit(font.render('spoonfulls: {}'.format(cappedspoonfulls), False, white),(50,150))   
        
        window.blit(font2.render('sps: {}'.format(sps),False,white),(100,200))
        window.blit(font2.render('plastic benders: {}   cost: {}'.format(savedata[1],
        (savedata[1]+1)*savedata[1]+10),False,white)
        ,(325,15))

        window.blit(font2.render('plastic recyclers: {}  cost:  {}'.format(savedata[2],
        (savedata[2]+1)*(savedata[2]*10)+100)
        ,False,white),(325,65))

        window.blit(font2.render('plastic forge:{}  cost: {}'.format(savedata[3],
        (savedata[3]+1)*(savedata[3]*500)+1000)
        ,False,white),(325,115))
        
        
        window.blit(font2.render('plastic factory: {} cost {}'.format(savedata[4],
        (savedata[4]+1)*(savedata[4]*1000)+2500),
        False,white),(325,165))
        #buildings
        try:
            window.blit(font2.render('{}'.format(upgrades[curupgrade].name),False,white),(325,575))
            window.blit(font2.render('{}'.format(upgrades[curupgrade].text),False,white),(325,625))
            window.blit(font2.render('cost: {}'.format(upgrades[curupgrade].cost),False,white),(325,675))
        except:
            pass
        #upgrades
        window.blit(images[0],(50,250))
        pygame.display.flip()
        window.fill(black)
        pygame.display.set_caption('{} spoonfulls'.format(savedata[0]))
    sleep(0.016)
    frame+=1
    #pretty sure thats like 60 fps
#to do
    #play "only a spoon full" when spoon clicked
saveobject = open("data.txt","w")
savedata2=savedata.copy()
savedata2.pop(11)
def writedata(data):
    saveobject.write(str(data))
    saveobject.write("\n")
for x in savedata2:
    writedata(x)

writedata(re.sub(" ","",' '.join(map(str,savedata[11]))))
#converts upgrades list into one line
saveobject.close()
#put code to run when game closed here probably saving stuff    
quit()