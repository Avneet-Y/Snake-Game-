from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]  #constants are in capitals
MOVE_DISTANCE = 20  
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
     
    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_segment(position)
        
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())      #adding a new segment to snake by getting hold
                                                            #of last segment in list and its position and add
                                                            # new segment at pos of last segment

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):  #range(Start,stop,step)
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:  #if current heading is moving up it cant's move down
            self.head.setheading(UP)   #above heading is a member function of turtle
                        #if you are moving forward you can't go backwards at same time
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        