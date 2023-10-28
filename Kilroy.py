import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle
t = turtle.Turtle()

# Set pen size and color
t.color("blue")
t.pensize(7)

# Draw nose
t.penup()
t.goto(-20, 20)
t.pendown()
t.right(90)
t.forward(60)
t.circle(20, 180)
t.forward(60)

# Left Eye
t.penup()
t.goto(-20, 42)
t.pendown()
t.dot(7, "blue")

# Right Eye
t.penup()
t.goto(20, 42)
t.pendown()
t.dot(7, "blue")

# Draw head
t.penup()
t.goto(-80, 0)
t.pendown()
t.circle(-80, 180)

# Draw first finger
t.penup()
t.goto(-175, 0)
t.pendown()
t.circle(10, -180)
t.backward(20)
t.circle(10, -180)
t.backward(20)

# Draw second finger
t.penup()
t.goto(-155, 0)
t.pendown()
t.circle(10, -180)
t.backward(20)
t.circle(10, -180)
t.backward(20)

# Draw third finger
t.penup()
t.goto(-135, 0)
t.pendown()
t.circle(10, -180)
t.backward(20)
t.circle(10, -180)
t.backward(20)

# Draw fourth finger
t.penup()
t.goto(115, 0)
t.pendown()
t.circle(10, -180)
t.backward(20)
t.circle(10, -180)
t.backward(20)

# Draw fifth finger
t.penup()
t.goto(135, 0)
t.pendown()
t.circle(10, -180)
t.backward(20)
t.circle(10, -180)
t.backward(20)

# Draw sixth finger
t.penup()
t.goto(155, 0)
t.pendown()
t.circle(10, -180)
t.backward(20)
t.circle(10, -180)
t.backward(20)

# Draw a line
t.penup()
t.goto(-200, 0)
t.pendown()
t.left(90)
t.forward(25)
t.penup()
t.forward(60)
t.pendown()
t.forward(95)
t.penup()
t.forward(40)
t.pendown()
t.forward(95)
t.penup()
t.forward(60)
t.pendown()
t.forward(25)
t.penup()
t.goto(200, 200)

# Close the turtle graphics window on click
screen.exitonclick()
