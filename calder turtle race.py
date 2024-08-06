import turtle, random

s=turtle.Screen()
s.setup(500,500)
s.bgcolor("#4287f5")


t=turtle.Turtle()
t.shape("turtle")
t.color("#4287a9")
t.speed(0)
t.turtlesize(2)



t.up()
t.goto(-200, 100)
t.down()
t.setheading(-90)
t.pensize(5)
t.fd(200)
t.up()
t.goto(150,0)
t.down()
t.circle(50)
t.up()
t.goto(165,-20)
t.write("circle", font=("Comic Sans MS",20))
t.up()
t.setheading(0)
t.goto(-234,0)
t.speed(2)
t.color("orange")


def quiz():
    num1=random.randint(1,100)
    num2=random.randint(1,100)
    guess=int(input("what is "+str(num1)+"+ "+str(num2)))
    if guess==num1+num2:
        print("u gyattst it")
        return True
    else:
        print ("so not sigma ohio skibbity")
while True:
    go=quiz()
    if go==True:
        t.fd(100)
    if t.xcor()>=150:
        print("jo mama did it")
        break
    
























































































































































































































































































































































































