import turtle as t
from tkinter import *

def print_grid_label(gridx,gridy,x,y,s,text_size=30):
    t.pu()
    
    t.hideturtle()
    t.speed('fastest')
    t.tracer(False)
    t.update()
    t.setup(gridx*y,gridy*x)
    t.mode('logo')
    t.clear()
    for i in range(1,x):
        
      t.pu()
      t.setx(-0.5*gridx*y)
      t.sety(gridy*i-0.5*gridy*x)
      t.seth(90)
      t.pd()
      t.forward(gridx*y)
    for j in range(1,y):
      t.pu()
      t.setx(gridx*j-0.5*gridx*y)
      t.sety(0.5*gridy*x)
      t.seth(180)
      t.pd()
      t.forward(gridy*x)
    t.pu()
    for i in range(1,x+1):
        for j in range(1,y+1):
            t.sety(gridy*(i-1)-0.5*gridy*x)
            t.setx(gridx*(j-1)-0.5*gridx*y)
            t.write(s,align='left',font=("宋体",text_size,"normal"))
    t.home()
    t.pd()
    t.color('white')
    t.forward(1)
    t.pu()
    # 将Turtle图形转换为PNG图像并保存
    canvas = t.getscreen().getcanvas()
    canvas.postscript(file="my_drawing.eps")
    t.done()

#print_grid_label(100,80,10,10,"螺丝A",text_size=25)
#其中前两个为画布长宽，后两个为行列数
