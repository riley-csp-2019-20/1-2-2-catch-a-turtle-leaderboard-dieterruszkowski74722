# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random 

#-----game configuration----
turtleshape = "turtle"
turtlesize = 2 
turtlecolor = "purple"

score = 0

timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
ike = trtl.Turtle(shape=turtleshape)
ike.color(turtlecolor)
ike.shapesize(turtlesize)
ike.speed(0)

score_writer = trtl.Turtle()
score_writer.ht()
score_writer.penup()
score_writer.goto(-370,270)

font_setup = ("Fascinate Inline", 15, "bold")
score_writer.write(score, font=font_setup)

counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(100,275)



#-----game functions--------
def ike_clicked(x,y):
    print("ike got clicked")
    change_position()
    update_score()

def change_position():
    ike.penup()
    ike.ht()
    if not timer_up: 
      ikex = random.randint(-400,400)
      ikey = random.randint(-300,300)
      ike.goto(ikex,ikey)
      ike.st()
    
def update_score():
    global score
    score += 1 
    print(score)
    score_writer.clear()
    score_writer.write(score, font=font_setup)


def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Game Over! :( Better Luck Next Time", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

    
#-----events----------------


wn = trtl.Screen()
wn.bgcolor("yellow")
ike.onclick(ike_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()