import pgzrun
import random
WIDTH, HEIGHT = 600, 270
monnaie = Actor("dollar.png")
vaisseau = Actor("startup.png",)
roche = Actor("rock (1).png")
score=0
monnaie.speed = 1.5
roche.speed = 1
game_over = False
def reset():
   roche.speed += 0
   roche.x = 0
   roche.y =random.randint(0,HEIGHT - roche.height)
   monnaie.speed += 0
   monnaie.x = 0
   monnaie.y = random.randint(0, HEIGHT - monnaie.height)
def draw():
  screen.clear()
  screen.draw.text("point: " + str(score), midtop = (WIDTH / 2, 5), fontsize = 40)
  if (not game_over):
    monnaie.draw()
    vaisseau.draw() 
    roche.draw()
  else:
    screen.draw.text("Game Over", center = (WIDTH / 2,HEIGHT / 2), fontsize = 40)
def update():
    global score, game_over
    if (monnaie.x < WIDTH):
        monnaie.x += monnaie.speed
        roche.x += roche.speed 
    else:
        game_over = True
    if (vaisseau.colliderect(monnaie)):
        score += 1
        reset()
    if (vaisseau.colliderect(roche)):
      score -= 2
      reset()
def on_mouse_move(pos):
    vaisseau.pos = pos
pgzrun.go() 
