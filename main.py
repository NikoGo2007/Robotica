import tkinter as tk
from turtle import RawTurtle, TurtleScreen, ScrolledCanvas


def create_turtle_pattern():
    root = tk.Tk()
    root.title("Мой узор")

    canvas = ScrolledCanvas(root, width=600, height=500)
    canvas.pack()

    screen = TurtleScreen(canvas)
    screen.bgcolor("white")

    turtle = RawTurtle(screen)
    turtle.speed(5)

    # Цвета
    colors = ["red", "blue", "green", "purple"]

    # Рисуем узор
    for i in range(100):
        turtle.color(colors[i % 4])
        turtle.pensize(1 + (i % 3))
        turtle.forward(i * 2)
        turtle.left(91)

    # Подпись
    turtle.penup()
    turtle.goto(200, -200)
    turtle.color("black")
    turtle.write("Алексей", font=("Arial", 14, "normal"))

    turtle.hideturtle()
    root.mainloop()


create_turtle_pattern()