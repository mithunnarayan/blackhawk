import turtle
def draw_square(go):
	for i in range(1,5):
	    go.forward(100)
	    go.right(90)
def draw():
	window = turtle.Screen()
	window.bgcolor("red")
	new = turtle.Turtle()
        for i in range(1,37):
 		draw_square(new)
		new.right(10)
        window.exitonclick()
draw()  
