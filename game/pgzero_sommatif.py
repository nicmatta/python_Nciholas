import pgzrun
WIDTH = 200
HEIGHT = 200
elapsed_time = 30
def draw():
    screen.clear()
    message = str(elapsed_time) + " seconde"
    screen.draw.text(message, midtop = (WIDTH / 2, 5))
def update_timer():
    global elapsed_time
    elapsed_time +=1
pgzrun.go() 