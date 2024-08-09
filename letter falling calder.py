import turtle,random

size=250
s=turtle.Screen()

s.setup(size*2,size*2)
s.title("fall guy")

s.bgcolor("orange")
s.tracer(0,0)

alph=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
min_speed=0
max_speed=1
letters=[]
lts=[]
n=5
game_over=False
score=0
d=turtle.Turtle()
d.color("red")
d.up()
d.ht()
d.goto(-size+10,size-25)


def draw_score():
    d.clear()
    d.write(f"score: {score}",font=("Arial",15,"normal"))

def set_up():
    for i in range(n):
        nt=turtle.Turtle()
        x=random.randint(-size+20,size-20)
        y=size
        nt.goto(x,y)
        nt.speed(0)
        nt.ht()
        nt.up()
        nt.color("#0000ff")
        lts.append(nt)
        while True:
            l=random.choice(alph)
            if l not in letters:
                letters.append(l)
                break






def draw_letters():
    global game_over
    for i in range (0,len(lts)):
        lts[i].clear()
        lts[i].write(letters[i],align="center",font=("arial",20,"normal"))
        ny=lts[i].ycor()-random.randint(min_speed,max_speed)
        lts[i].sety(ny)
        if lts[i].ycor()<-size:
            game_over=True
    if not game_over:
        s.ontimer(draw_letters,50)
def press(key):
    global score
    print(key)

    if key in letters:
        score+=1
        i=letters.index(key)
        while True:
            l=random.choice(alph)
            if l not in letters:
                letters[i]=l
                break
        x=random.randint(-size,size)
        y=size
        lts[i].goto(x,y)
    draw_score()


def id():
    global max_speed
    #max_speed+=1
    s.ontimer(id,500)
for letter in alph:
    s.onkey(lambda l =letter : press(l), letter)

set_up()
draw_score()
draw_letters()
id()
s.listen()
s.mainloop()











































































