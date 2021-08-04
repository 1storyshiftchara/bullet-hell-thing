import os, pygame, re
sprites = []
Curfile = __file__
Curfile = re.sub("loadsprites.py", "",Curfile)
Imagefile = Curfile + "sprites"
Imagefile = re.sub("/",r'\\',Imagefile)
Imagefile += r'\''
Imagefile = re.sub("'","",Imagefile)
# yet its dumb no i dont know how to change it
print("file: "+Curfile)
print("images: "+Imagefile)
def loadimage(name):
    try:
        image = pygame.image.load('{}{}'.format(Imagefile,name))
        return image
    except:
        print("image doesnt exist", name)
