import turtle as t
import keyboard as btn
android = t.Pen()

canvas = t.Screen()
screenx = 960
screeny = 848
canvas.screensize(screenx, screeny)
color = ["red", "blue", "green", "purple", "orange", "pink", "cyan", "gray", "black"]
android.speed(100)
android.color("red")

while True:    
    if android.xcor() or android.ycor() > screenx or screeny:
        android.goto(0,0)    
    if btn.is_pressed("w"):
        android.forward(20)
    elif btn.is_pressed("a"):
        android.left(20)
    elif btn.is_pressed("d"):
        android.right(20)        