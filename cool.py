import turtle as trtl
import random
width = 1
#width = random.randint(1,30)
squares = 50000000
angle = 180.00001
#angle = random.randint(30,180)
drawer = trtl.Turtle()
drawer.speed(0)
drawer.pensize()
drawer.ht()
print(width)
print (angle)
counter1 = 0
while counter1 < (squares*4):
    drawer.forward(15+(counter1*width))
    drawer.left(angle)
    counter1 += 1





wn = trtl.Screen()
wn.mainloop()