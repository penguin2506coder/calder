import turtle,time,os,random

sc=turtle.Screen()
sc.title ("snake")
sc.bgcolor("#FF1493")
sc.setup(width=600,height=600)
sc.tracer(0)


head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#00FF00")
head.up()
head.goto(0,0)
head.direction="right"


food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.pu()
food.goto(100,100)


tail=[]

pen=turtle.Turtle()
pen.ht()
pen.pu()
pen.goto(0,250)
pen.clear()
pen.write("score: "+str(len(tail)), align="center",font=("Arial",20))


def up():
    head.direction="up"
def down():
    head.direction="down"
def right():
    head.direction="right"
def left():
    head.direction="left"

def move():
    if head.direction=="up":
        head.sety(head.ycor()+20)
    if head.direction=="down":
        head.sety(head.ycor()-20)
    if head.direction=="right":
        head.setx(head.xcor()+20)
    if head.direction=="left":
        head.setx(head.xcor()-20)


sc.listen()
sc.onkeypress(up,"w")
sc.onkeypress(right,"d")
sc.onkeypress(left,"a")
sc.onkeypress(down,"s")





delay=0.1

while True:
    sc.update()
    if head.distance(food)<50:
        food.goto(random.randint(-300,300),random.randint(-300,300))
        newpiece=turtle.Turtle()
        newpiece.speed(0)
        newpiece.shape("turtle")
        newpiece.color("#0000FF")
        newpiece.pu()
        tail.append(newpiece)
        pen.clear()
        pen.write("score: "+str(len(tail)), align="center",font=("Arial",20))

    if len(tail)>0 and tail[0].distance(head) > 10:
        end = tail[-1]
        end.goto(head.xcor(), head.ycor())
        tail.remove(end)
        tail.insert(0, end)

    for piece in tail:
        fornt=tail[0]
    time.sleep(delay)
    move()
sc.mainloop

        





