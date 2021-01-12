import pgzrun
WIDTH  = 500	
HEIGH = 300
alien = Actor("alien.png")
speed = 1
def draw():	
    """ Tout ce qu'on veut voir dans notre fenêtre"""
    screen.fill("blue")	    
    alien.draw()
def update():
    alien.x = alien.x + speed
pgzrun.go() 