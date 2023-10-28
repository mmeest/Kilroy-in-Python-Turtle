import turtle as t

t.pensize(1)
t.Screen().bgcolor("black") 
  
def main():
  
  # Draw nose
  t.pendown()
  
  for i in range(24):
    for j in range(15):
      t.pencolor(i*15, j*25, 111)
      t.circle(150-i*5, 110)
      t.left(90)
      t.circle(150-i*5, 110)
      t.right(180)
      t.circle(12, 38)

if __name__ == "__main__":
  main()
