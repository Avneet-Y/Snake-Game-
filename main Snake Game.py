from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("The Snake Game")
cordinate_list = [(0,0), (-20,0), (-40,0)]
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    if snake.head.distance(food) < 15:   #Collision with food
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False                 #for collison with wall
        scoreboard.game_over()
    
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment)<10:
            game_on = False
            scoreboard.game_over()
        
 
screen.exitonclick()