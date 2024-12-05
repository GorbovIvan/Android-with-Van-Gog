import turtle as t
import random
android = t.Pen()
van_gog = t.Pen()

color = ["red", "blue", "green", "purple", "orange", "pink", "cyan", "gray", "black"]
android.left(90)
android.speed(100)
android.color("red")
android.forward(100)
android.pensize(10)

van_gog.right(90)
van_gog.speed(100)
van_gog.color("green")
van_gog.forward(100)
van_gog.pensize(10)

turns = ["left", "right"]
turn = None
for dist in range(10000):
    android.forward(50)
    android.color(random.choice(color))
    van_gog.forward(50)
    van_gog.color(random.choice(color))
    turn = random.choice(turns)
    if turn == "left":
        android.left(random.randint(10, 50))
        van_gog.left(random.randint(10, 50))
    else:
        van_gog.right(random.randint(10, 50))
        android.right(random.randint(10, 50))
input()