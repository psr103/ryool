import turtle
import random

## 전역 변수 선언 부분 ##
r, g, b = [0]*3
swidth, sheight = 500, 500

## 코드 실행 부분 ##
turtle.title('거북소라')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.shape('turtle')
turtle.screensize(swidth, sheight)
while True :
    dist = 0
    for dist in range(5, 85, 1):
        r = random.random()
        g = random.random()
        b = random.random()
        turtle.pencolor((r, g, b))
        turtle.pendown()
        turtle.left(30)
        turtle.forward(dist)
        dist = dist + 1
    

    turtle.done()

