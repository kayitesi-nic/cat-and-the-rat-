import pgzrun
from random import randint

WIDTH= 600
HEIGHT= 500
TITLE= "Cat and the rat"

cat= Actor("cat")
cat.pos= 100,100

rat= Actor("rat")
rat.pos= 50,50

score= 0
game_over= False

def draw():
    screen.blit("background image",(0,0))
    cat.draw()
    rat.draw()

    screen.draw.text("Score:" +str(score), topleft= (15,15), color=("black"), fontsize=40)

    if game_over:
        screen.fill("pink")
        screen.draw.text("Time's up! Your Score is:" +str(score), color=("red"), topleft= (250,250))

def place_rat():
    rat.x= randint(50,WIDTH-50)
    rat.y= randint(50,HEIGHT-50)

def time_up():
    global game_over
    game_over= True 

def update():
    global score
    
    if keyboard.left:
        cat.x= cat.x-2
    if keyboard.right:
        cat.x= cat.x+2
    if keyboard.up:
        cat.y= cat.y-2
    if keyboard.down:
        cat.y= cat.y+2

    rat_touched= cat.colliderect(rat)
    if rat_touched:
        score= score+10
        place_rat()

clock.schedule(time_up, 15)


pgzrun.go()