import pgzrun
WIDTH, HEIGHT = 800, 600
roche = Actor("rock.png")
vaisseau = Actor("startup.png")
score=0
roche.speed = 0.5
game_over = False
def reset_faster():
    roche.speed += 1
    roche.x = 0
def draw():
  screen.clear()
  screen.draw.text("Score: " + str(score), midtop = (WIDTH / 2, 5), fontsize = 40)
  if (not game_over):
    roche.draw()
    vaisseau.draw()
  else:
    screen.draw.text("Game Over", center = (WIDTH / 2,HEIGHT / 2), fontsize = 40)
def update():
    global score, game_over
    if (roche.x < WIDTH):
        roche.x += roche.speed
    else:
        game_over = True 
    if (vaisseau.colliderect(roche)):
        score += 1
def on_mouse_move(pos):
    vaisseau.pos = pos
pgzrun.go() 
