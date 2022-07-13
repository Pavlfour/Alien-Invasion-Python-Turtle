import turtle, random, math

screen = turtle.Screen()
screen.bgcolor('black')
screen.title('Space Invaders')
screen.setup(width=600,height=600)
screen.listen()

player = turtle.Turtle()
player.color('red')
player.speed(0)
player.penup()
player.setposition(0,-250)
player.shape('triangle')
player.setheading(90)

bullet = turtle.Turtle()
bullet.hideturtle()
bullet.speed(0)
bullet.penup()
bullet.shape('triangle')
bullet.color('yellow')
bullet.setheading(90)
bullet.shapesize(0.5,0.5)

score = 0
playerspeed = 15
enemyspeed = 2
bulletspeed = 7
bulletstate= 'ready'
number_of_enemies = 7
enemies = []
ending = 1

score_draw = turtle.Turtle()
score_draw.hideturtle()
score_draw.speed(0)
score_draw.color('white')
score_draw.penup()
score_draw.setposition(-290,280)
string = 'Score: %s' % score
score_draw.write(string,font=('Arial',14,'normal'))

game_over = turtle.Turtle()
game_over.hideturtle()
game_over.speed(0)
game_over.color('red')
game_over.penup()
game_over.setposition(-80,0)


for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
    enemies[i].hideturtle()
    enemies[i].speed(0)
    enemies[i].penup()
    x = random.randint(-270,270)
    y = random.randint(140,280)
    enemies[i].setposition(x, y)
    enemies[i].shape('circle')
    enemies[i].color('green')
    enemies[i].showturtle()

def move_player_right():
    x = player.xcor()
    x += playerspeed
    if x < 290:
        player.setx(x)

def move_player_left():
    x = player.xcor()
    x -= playerspeed
    if x > -300:
        player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == 'ready':
        bulletstate = 'fire'
        x2 = player.xcor()
        y2 = player.ycor()
        bullet.setposition(x2,y2+10)
        bullet.showturtle()

def isCollision(t1,t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 27:
        return True
    else:
        return False

screen.onkeypress(move_player_right, "Right")
screen.onkeypress(move_player_left, "Left")
screen.onkey(fire_bullet,"space")

while ending:

    for enemy in enemies:
        x1 = enemy.xcor()
        x1 += enemyspeed
        enemy.setx(x1)

        if enemy.xcor() > 290 or enemy.xcor() < -290:
            y = enemy.ycor()
            y -= 40
            enemy.sety(y)
            enemyspeed *= -1

        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bullet.setposition(0, -400)
            bulletstate = 'ready'
            x = random.randint(-280, 280)
            y = random.randint(140, 280)
            enemy.setposition(x, y)
            score += 10
            enemyspeed*=1.05
            string = "Score: %s" % score
            score_draw.clear()
            score_draw.write(string, font=('Arial', 14, 'normal'))

        if isCollision(player, enemy) or enemy.ycor()<-270:
            player.hideturtle()
            enemy.hideturtle()
            bulletstate='fire'
            game_over.write('GAME OVER!', font=('Arial', 20,'normal'))
            ending=0

        y3 = bullet.ycor()
        y3 += bulletspeed
        bullet.sety(y3)

        if bullet.ycor() > 290:
            bullet.hideturtle()
            bulletstate = 'ready'



screen.mainloop()