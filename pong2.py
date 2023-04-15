import turtle

speed = 0.1
no_of_balls = 2
n = 2*no_of_balls
s = 700
paddles = {}

# Window
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = s+50, height = s+50)
wn.tracer(0)


# Paddles
for number in range(0,n):
    paddles["paddle_%s" %number] = 0 ### MAKE THIS GLOBALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL

print(paddles)

k=0

for i in paddles.keys():
	i = turtle.Turtle()
	i.speed(0)
	i.shape("square")
	i.shapesize(stretch_wid=1, stretch_len=5)
	i.color("white")
	i.penup()

	i.tilt((360/n)*k)

	if k % 2 == 1:
		i.sety(0)
		i.setx(pow(-1,(k-1)/2)*s/2)
	else:
		i.sety(pow(-1,k/2)*s/2)
		i.setx(0)

	k += 1

# Balls
dict1 = {}

for number in range(0,no_of_balls):
    dict1["ball_%s" %number] = 0

print(dict1)

i=0

for b in dict1.keys():
	i=i+0.05
	b = turtle.Turtle()
	b.speed(0)
	b.shape("square")
	b.color("white")
	b.penup()

	b.dx = speed+i
	b.dy = speed-i


while True:
	wn.update()

	# Ball movements
	#for b in dict1.keys():
		#b.setx( b.xcor() + b.dx )
		#b.sety( b.ycor() + b.dy )