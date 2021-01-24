import pgzrun
# je métre les dimision du fenatre 
WIDTH  = 700
HEIGHT = 500
# indentifi les actor
alien = Actor("alien.png")
dog = Actor("2alien.png")
# code les vitess 
speed = 0.5 
dogspeed=0.1
# coleur du fenatre 
def draw():	
    screen.fill("black")	    
    alien.draw()
    dog.draw()
def update():
    alien.x = alien.x + speed
    dog.x=dog.x+dogspeed 
# changement de angle 
def on_mouse_move(pos):
    global p_text, a_text
    p_text = "Position: " + str(pos)
    alien.angle = alien.angle_to(pos)
    a_text = "Angle: " + str(round(alien.angle))
pgzrun.go() 
