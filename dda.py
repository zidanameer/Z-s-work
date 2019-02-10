from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time
ready=0
def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-500.0,500.0,-500.0,500.0)
x1=float(input("Enter x co-ordinate"))
y1=float(input("Enter the y-co-ordinate"))
x2=float(input("Enter x co-ordinate"))
y2=float(input("Enter the y-co-ordinate"))
x3=float(input("Enter x co-ordinate"))
y3=float(input("Enter the y-co-ordinate"))
x4=float(input("Enter x co-ordinate"))
y4=float(input("Enter the y-co-ordinate"))
def round(a):
    return int(a+0.5)
def setpixel(x,y):
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()
def dda(x6,y6,x7,y7):
    dx=x7-x6
    dy=y7-y6
    if(abs(dx)>abs(dy)):
        step=abs(dx)
    else:
        step=abs(dy)
    x=x6
    y=y6
    xinc=dx/(step+0.0)
    yinc=dy/(step+0.0)
    setpixel(round(x),round(y))
    for k in range (0,int(step)):
        x=x+xinc
        y=y+yinc
        setpixel(round(x),round(y))
        glFlush()
def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(2.0)
    global x1,y1,x2,y2
    global x3,y3,x4,y4,ready
    dda(x1,y1,x2,y2)
    dda(x2,y2,x3,y3)
    dda(x3,y3,x4,y4)
    dda(x4,y4,x1,y1)
    if not ready:
        a=input("are u ready to reflect")
        ready=1
    print(" 1. x-axis  2.y-axis")
    k=int(input(""))
    glClear(GL_COLOR_BUFFER_BIT)
    if (k==1):
        dda(x1,-y1,x2,-y2)
        dda(x2,-y2,x3,-y3)
        dda(x3,-y3,x4,-y4)
        dda(x4,-y4,x1,-y1)
    elif(k==2):
        dda(-x1,y1,-x2,y2)
        dda(-x2,y2,-x3,y3)
        dda(-x3,y3,-x4,y4)
        dda(-x4,y4,-x1,y1)
    else :
        print("Wrong Option")    
    
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,50)
    glutInitWindowSize(1000,1000)
    glutCreateWindow("DDA")
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()
main()
    
    
