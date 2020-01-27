import turtle
import time

root = turtle.Screen()
root.title("ANALOG CLOCK")

t_size = 1

t = turtle.Turtle()
t.speed(100)
t.shape("blank")
style = ('Courier', 16, 'bold')
flag = 1
pos = 12
cl = ["blue","red","green","orange"]
sq = turtle.Turtle()
sq.shape("blank")
sq.speed(500)

try:
    for i in range(60):

        if (flag):
            flag = 0
            sq.penup()
            sq.right(90)
            sq.forward(270*t_size)
            sq.left(90)
            sq.backward(270*t_size)
            sq.pendown()
            sq.pensize(14)
            for j in range(4):
                sq.color(cl[j])
                sq.forward(270*2*t_size)
                sq.left(90)
            t.left(90)
        if (i % 5 == 0):
            t.pencolor("red")
            t.pensize(5)
            t.penup()
            t.forward(200 * t_size)
            t.pendown()
            t.forward(10 * t_size)
            t.penup()
            t.forward(20 * t_size)
            t.pendown()
            if (pos == 12):
                t.color("black")
                t.write(str(pos),font=style)
                pos = 1
            elif(pos < 4):
                t.color("black")
                t.write(str(pos),font=style)
                pos += 1
            elif(pos == 4):
                t.color("black")
                t.penup()
                t.forward(10 * t_size)
                t.pendown()
                t.write(str(pos), font=style)
                t.penup()
                t.backward(10 * t_size)
                pos += 1
            elif(pos < 9):
                t.color("black")
                t.penup()
                t.forward(20 * t_size)
                t.pendown()
                t.write(str(pos), font=style)
                t.penup()
                t.backward(20 * t_size)
                pos += 1
            else:
                t.color("black")
                t.penup()
                t.forward(10 * t_size)
                t.pendown()
                t.write(str(pos), font=style)
                t.penup()
                t.backward(10 * t_size)
                pos += 1
            t.penup()
            t.backward(230 * t_size)
        else:
            t.pencolor("blue")
            t.pensize(2 * t_size)
            t.penup()
            t.forward(200 * t_size)
            t.pendown()
            t.forward(10 * t_size)
            t.penup()
            t.backward(210 * t_size)
        t.right(6)
    t.pencolor("black")

    up_d = 1
    up_h = 1
    up_m = 1
    up_s = 1
    while True:
        d = int(time.ctime()[8:10])
        h = int(time.ctime()[11:13])
        m = int(time.ctime()[14:16])
        s = int(time.ctime()[17:19])

        if (up_d):
            dt=turtle.Turtle()
            dt.shape("blank")
            dt.speed(200)
            dt.penup()
            dt.right(30)
            dt.forward(100 * t_size)
            dt.write(str(d)+" "+time.ctime()[4:7],font=style)
            dt.backward(100 * t_size)
            up_d = 0

        if (up_h):
            hr = turtle.Turtle()
            hr.shape("blank")
            hr.left(90)
            hr.speed(200)
            hr.pensize(14 * t_size)
            hr.right((h % 12) * 30 + m / 2)
            hr.backward(30 * t_size)
            hr.forward(160 * t_size)
            hr.penup()
            hr.backward(160 * t_size)
            hr.pencolor("green")
            hr.pensize(8 * t_size)
            hr.pendown()
            hr.forward(155 * t_size)
            hr.penup()
            hr.backward(125 * t_size)
            hr.pencolor("black")
            hr.pensize(14 * t_size)
            hr.shape("circle")
            up_h = 0

        if (up_m):
            mn = turtle.Turtle()
            mn.shape("blank")
            mn.left(90)
            mn.speed(200)
            mn.pensize(8 * t_size)
            mn.right(m * 6)
            mn.backward(30 * t_size)
            mn.forward(180 * t_size)
            mn.penup()
            mn.backward(180 * t_size)
            mn.pencolor("green")
            mn.pensize(4 * t_size)
            mn.pendown()
            mn.forward(175 * t_size)
            mn.penup()
            mn.backward(145 * t_size)
            mn.pencolor("black")
            mn.pensize(14 * t_size)
            mn.shape("circle")
            up_m = 0

        if (up_s):
            sc = turtle.Turtle()
            sc.shape("blank")
            sc.left(90)
            sc.speed(200)
            sc.pensize(2 * t_size)
            sc.color("red")
            sc.right(s * 6)
            sc.backward(30 * t_size)
            sc.forward(190 * t_size)
            up_s = 0

            nl = []
            for x in cl[1:]:
                nl.append(x)
            nl.append(cl[0])
            cl = nl
            for j in range(4):
                sq.color(cl[j])
                sq.forward(270 * 2 * t_size)
                sq.left(90)

        time.sleep(0.03)
        new_d = int(time.ctime()[8:10])
        new_h = int(time.ctime()[11:13])
        new_m = int(time.ctime()[14:16])
        new_s = int(time.ctime()[17:19])

        if (new_d != d):
            up_d = 1
            dt.clear()
            dt.reset()

        if (new_h != h):
            up_h = 1
            hr.clear()
            hr.reset()

        if (new_m != m):
            up_m = 1
            mn.clear()
            mn.reset()

        if (new_s != s):
            up_s = 1
            sc.clear()
            sc.reset()
except:
    None

