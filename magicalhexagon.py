import turtle

colors = ["red", "green", "blue", "purple", "orange", "yellow"]
tm = turtle.Pen()
turtle.bgcolor("black")
tm.speed(0)

for xi in range(360):
    tm.pencolor(colors[xi % 6])
    tm.width(xi // 100 + 1)
    tm.forward(xi)
    tm.left(59)
    
