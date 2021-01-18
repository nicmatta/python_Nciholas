import pgzrun
WIDTH  = 500
HEIGH = 300
alien = Actor("alien.png")
speed = 0.5
def draw():	
    screen.fill("black")	    
    alien.draw()
def update():
    alien.x = alien.x + speed
def on_mouse_move(pos):
    global p_text, a_text
    p_text = "Position: " + str(pos)
    alien.angle = alien.angle_to(pos)
    a_text = "Angle: " + str(round(alien.angle))
pgzrun.go() 
