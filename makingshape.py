from turtle import *

def bunder(ukuran):
    circle(ukuran)

def square(ukuran):
    for i in range (4):
        forward(ukuran)
        left(90)

def triangle(ukuran):
    for i in range(3):
        forward(ukuran)
        left(120)

def sun(ukuran):
    for i in range (18):
        forward(ukuran)
        left(100)

def stars(ukuran):
    for i in range(5):
        forward(ukuran)
        left(144)


speed(10)
shape = input('what shape you want to use? (circle, square, triangle, sun, stars.)')
shape = shape.lower()
if shape == 'circle' or shape == 'square' or shape == 'triangle' or shape == 'sun' or shape == 'star' or shape == 'stars':
    berapa = int(input('How many shape you want to draw?'))
    for i in range (berapa):
        warna = input('What colors you want to use?')
        warna = warna.lower()
        ukuran = int(input('what size you want the shape be?'))
        x = int(input('enter the coordinates for x'))
        y = int(input('enter the coordinates for y'))
        tempat = (x, y)
        if shape == 'circle':
            penup()
            goto(x,y)
            pendown()
            color(warna)
            begin_fill()
            bunder(ukuran)
            end_fill()
        if shape == 'triangle':
            penup()
            goto(x,y)
            pendown()
            color(warna)
            begin_fill()
            triangle(ukuran)
            end_fill()
        if shape == 'square':
            penup()
            goto(x,y)
            pendown()
            color(warna)
            begin_fill()
            square(ukuran)
            end_fill()
        if shape == 'sun':
            penup()
            goto(x,y)
            pendown()
            color(warna)
            begin_fill()
            sun(ukuran)
            end_fill()
        if shape == 'stars':
            penup()
            goto(x,y)
            pendown()
            color(warna)
            begin_fill()
            stars(ukuran)
            end_fill()
else:
    print('the system cannot recognize it!')
exitonclick()

