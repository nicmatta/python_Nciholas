## Programmer par:Nicholas Matta
# projet sommatif:Pygame Zero
# crée le 15 janvier 2022
# modifier le 27 janvier 2021
# adress couriel:matnic02@ecolecatholique.ca
# je import pygame est redom pour mais image
import pgzrun
import random
# je mettre les mésure pour mon fenatre
WIDTH, HEIGHT = 600, 260
# indentifi mes image
monnaie = Actor("dollar.png")
vaisseau = Actor("startup.png", )
roche = Actor("rock (1).png")
rocket = Actor("rocket (1).png")
#je metre le score du jeux que tu comence avec
score = 0
#je did a quel vitess je veux mes actor a bouger
monnaie.speed = 1.3
roche.speed = 1
rocket.speed = 0.7
#je indique que si sest game over a arréter le jeux
game_over = False
#je indique que je veux que les actore vien a des point diféren du l'axe des y est rest la mémes dans l'axe de x
def reset():
    roche.speed += 0
    roche.x = 0
    roche.y = random.randint(0, HEIGHT - roche.height)
    monnaie.speed += 0
    monnaie.x = 0
    monnaie.y = random.randint(0, HEIGHT - monnaie.height)
    rocket.speed += 0
    rocket.x = 0
    rocket.y = random.randint(0, HEIGHT - rocket.height)
#je disigne tout l'écriture est acotre dans mon programe
def draw():
    screen.blit("bg", (0, 0))
    screen.draw.text("point: " + str(score),
                     midtop=(WIDTH / 2, 5),
                     fontsize=40)
    if (not game_over):
        monnaie.draw()
        vaisseau.draw()
        roche.draw()
        rocket.draw()
    else:
        screen.draw.text("Game Over",
                         center=(WIDTH / 2, HEIGHT / 2),
                         fontsize=40)
# je indique que si le monnaie dépase le fenatre de faire game over
def update():
    global score, game_over
    if (monnaie.x < WIDTH):
        # je programe le vitees des actor
        monnaie.x += monnaie.speed
        roche.x += roche.speed
        rocket.x += rocket.speed
#je indique le reaction que je veux can les actor fair can eux se frapp est les point que eux predre
    else:
        game_over = True
    if (vaisseau.colliderect(monnaie)):
        score += 1
        reset()
    if (vaisseau.colliderect(roche)):
        score -= 2
        reset()
    if (vaisseau.colliderect(rocket)):
        game_over = True
# je indique que can le souri bouge le actor "vaisseau" bouge avec le souri
def on_mouse_move(pos):
    vaisseau.pos = pos
pgzrun.go()
