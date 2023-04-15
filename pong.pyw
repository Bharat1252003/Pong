import winsound
import turtle
import time

speed = 0.3
score_a = 0
score_b = 0
rally = 0


# Window
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()

ball.dx = speed
ball.dy = speed


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,220)
pen.write("Player A: 0	Player B: 0\nRally: 0", align="center", font=("Courier", 20, "normal"))


# Functions
def paddle_a_up():
	y = paddle_a.ycor()
	if y<240: y+=20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	if y>-240: y-=20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	if y<240: y+=20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	if y>-240: y-=20
	paddle_b.sety(y)


# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up") 	# up arrow
wn.onkeypress(paddle_b_down,"Down")	# down arrow

wn.update()
time.sleep(3)
# Main game loop
while True:
	wn.update()
	
	# Move the ball
	ball.setx( ball.xcor() + ball.dx )
	ball.sety( ball.ycor() + ball.dy )


	paddle_a.sety(ball.ycor())
	paddle_b.sety(ball.ycor())


	# Border Checking
	if ball.ycor()>280:
		ball.sety(280)
		ball.dy *= -1
		winsound.PlaySound("pong_sound.wav", winsound.SND_ASYNC)

	if ball.ycor()<-280:
		ball.sety(-280)
		ball.dy *= -1
		winsound.PlaySound("pong_sound.wav", winsound.SND_ASYNC)
		
	if ball.xcor()>380:
		ball.setpos(0,0)
		ball.dx *= -1
		score_a += 1
		rally = 0
		winsound.PlaySound("pong_sound1.wav", winsound.SND_ASYNC)

		pen.clear()
		pen.write("Player A: {}	Player B: {}\nRally: {}".format(score_a, score_b, rally), align="center", font=("Courier", 20, "normal"))
		
	if ball.xcor()<-380:
		ball.setpos(0,0)
		ball.dx *= -1
		score_b += 1
		rally = 0
		winsound.PlaySound("pong_sound1.wav", winsound.SND_ASYNC)

		pen.clear()
		pen.write("Player A: {}	Player B: {}\nRally: {}".format(score_a, score_b, rally), align="center", font=("Courier", 20, "normal"))
	
	
	# Paddle and ball collisions
	if (ball.xcor()>-350 and ball.xcor()<-340) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
		ball.setx(-340)
		ball.dx *= -1
		winsound.PlaySound("pong_sound.wav", winsound.SND_ASYNC)
		rally += 1

		pen.clear()
		pen.write("Player A: {}	Player B: {}\nRally: {}".format(score_a, score_b, rally), align="center", font=("Courier", 20, "normal"))
	
		
	if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
		ball.setx(340)
		ball.dx *= -1
		winsound.PlaySound("pong_sound.wav", winsound.SND_ASYNC)
		rally += 1

		pen.clear()
		pen.write("Player A: {}	Player B: {}\nRally: {}".format(score_a, score_b, rally), align="center", font=("Courier", 20, "normal"))
	