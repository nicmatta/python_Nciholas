import pgzrun


WIDTH  = 500	
HEIGH = 300

alien = Actor("alien.png")
alien.pos = (0, HEIGHT / 2)
speed = 2



def draw():	
    """ Tout ce qu'on veut voir dans notre fenêtre"""
    screen.fill("blue")	    
    alien.draw()

def update():
    alien.x = alien.x + speed


pgzrun.go() 