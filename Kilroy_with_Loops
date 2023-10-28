import turtle

def draw_finger(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(10, -180)
    t.backward(20)
    t.circle(10, -180)
    t.backward(20)

def draw_eyes(t):
    for x in [-20, 20]:
        t.penup()
        t.goto(x, 42)
        t.pendown()
        t.dot(7, "blue")

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()
    
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
    
    # Draw head
    t.penup()
    t.goto(-80, 0)
    t.pendown()
    t.circle(-80, 180)
    
    # Draw eyes
    draw_eyes(t)
    
    # Draw fingers
    for x in [-175, -155, -135, 115, 135, 155]:
        draw_finger(t, x, 0)
    
    # Draw a line
        segments = [25, 60, 95, 40, 95, 60, 25]
        t.penup()
        t.goto(-200, 0)
        t.pendown()
        t.left(90)
    
        for segment in segments:
          if(segment % 2 == 1):
            t.forward(segment)
            t.penup()
          else:
            t.forward(segment)
            t.pendown()
    
    screen.exitonclick()

if __name__ == "__main__":
    main()
