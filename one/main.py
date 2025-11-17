import tkinter as tk
from turtle import RawTurtle, TurtleScreen, ScrolledCanvas


def create_turtle_pattern():
    root = tk.Tk()
    root.title("Задане Экзамен")

    canvas = ScrolledCanvas(root, width=600, height=500)
    canvas.pack()

    screen = TurtleScreen(canvas)
    screen.bgcolor("white")

    turtle = RawTurtle(screen)
    turtle.speed(5)

    colors = ["red", "blue", "green", "purple"]

    line_width = 5

    for i in range(100):
        turtle.color(colors[i % 4])
        turtle.pensize(line_width + (i % 2))
        turtle.forward(i * 2)
        turtle.left(91)

    # Подпись
    turtle.penup()
    turtle.goto(200, -200)
    turtle.color("black")
    turtle.write("Никита", font=("Arial", 14, "normal"))

    turtle.hideturtle()
    root.mainloop()


create_turtle_pattern()