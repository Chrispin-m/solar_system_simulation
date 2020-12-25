#Representation of the solar system
#3d simulation
'''
Among the essential information about the solar system includes:
 Mass of the sun=1.989 × 10^30 kg
 Mass of the planet
 Distance from the center of the sun to the center of the planet
 speed of a planet
 gravitational force
 centrifugal force and
 Gravitation constant = 6.674×10−11 m3⋅kg−1⋅s−2
'''
from math import sin, cos
from vpython import *
import numpy as np
print("-"*25)
print("Coded by Crispine Wachira")
print("-"*25)
print("Contact me via email:chrismwangicw@gmail.com \nLinkedIn:https:www.linkedin.com/in/mwangi-wachira-5a4b1a1a3 \nWhatsapp:+254710358658")

x0=5
y0=3
x1=4*(2)**0.5
y1=4
sun=sphere(radius=0.8, color=color.yellow, pos=vector((x0**2-y0**2)**0.5,0,0))
mercury=sphere(radius=0.5, color=color.orange, pos=vector(5.171236166328254,0,0), make_trail=True)
venus=sphere(radius=0.5, color=color.red, pos=vector(0.5,3,0), make_trail=True)
earth=sphere(radius=0.54, color=color.blue, pos=vector(-10.5,0,0), make_trail=True)
moon=sphere(radius=0.15, color=color.white, pos=vector(-11,0,0))
mars=sphere(radius=0.53, color=color.red, pos=vector(-17,0,0), make_trail=True)
jupiter=sphere(radius=0.8, color=color.green, pos=vector(-40,0,0), make_trail=True)
saturn=sphere(radius=0.7, color=color.yellow, pos=vector(-4,16.8,0), make_trail=True)
uranus=sphere(radius=0.6, color=color.green, pos=vector(-6,20,0), make_trail=True)
neptune=sphere(radius=0.6, color=color.blue, pos=vector(-4,24,0), make_trail=True)
pluto=sphere(radius=0.7, color=color.orange, pos=vector(25,-18,0), make_trail=True)
#ad=sphere(radius=0.01),color=

j=0
def ellipse(a,b,c):
    z=c*(1-(a/b)**2)**0.5
    return z

def loop():
    i=0
    #first quarter
    for p in np.linspace(-x1,0,num=500):
        i+=0.01
        rate(30)
        mercury.pos.x=(-p)/1.5+1.4
        mercury.pos.y=-ellipse((-p)*x0/x1,x0,y0)/1.5
        venus.pos.x=p+x1+0.5
        venus.pos.y=ellipse((p+x1)*x0/x1,x0,y0)
        earth.pos.x=p*9/x1-1.5
        earth.pos.y=ellipse(p,x1,y1)*5.5/x0
        moon.pos.x=p*9/x1-1.5+0.8*cos(i)
        moon.pos.y=ellipse(p,x1,y1)*5.5/x0+0.8*sin(i)
        mars.pos.x=p*15/x1-2
        mars.pos.y=ellipse(p,x1,y1)*7.5/x0
        jupiter.pos.x=p*34/x1-6
        jupiter.pos.y=ellipse(p,x1,y1)*17/x0
        saturn.pos.x=(p+x1)*42/x1-4
        saturn.pos.y=ellipse((p+x1),x1,y1)*21/x0
        uranus.pos.x=(p+x1)*50/x1-6
        uranus.pos.y=ellipse((p+x1),x1,y1)*25/x0
        neptune.pos.x=(p+x1)*54/x1-4
        neptune.pos.y=ellipse((p+x1),x1,y1)*30/x0
        pluto.pos.x = -(p + x1)*6 +25
        pluto.pos.y = -ellipse((p + x1)*x0/x1, x0, y0) * 6
        pluto.pos.z=-5*p-5*x1
    #second quarter
    for p in np.linspace(0,x1,num=500):
        i+=0.01
        rate(30)
        mercury.pos.x=(-p)/1.5+1.4
        mercury.pos.y=-ellipse((-p)*x0/x1,x0,y0)/1.5
        venus.pos.x=x1-p+0.5
        venus.pos.y=-ellipse((x1-p)*x0/x1,x0,y0)
        earth.pos.x=p*9/x1-1.5
        earth.pos.y=ellipse(p,x1,y1)*5.5/x0
        moon.pos.x=p*9/x1-1.5+0.8*cos(i)
        moon.pos.y=ellipse(p,x1,y1)*5.5/x0+0.8*sin(i)
        mars.pos.x=p*15/x1-2
        mars.pos.y=ellipse(p,x1,y1)*7.5/x0
        jupiter.pos.x=p*34/x1-6
        jupiter.pos.y=ellipse(p,x1,y1)*17/x0
        saturn.pos.x=(x1-p)*42/x1-4
        saturn.pos.y=-ellipse((x1-p),x1,y1)*21/x0
        uranus.pos.x=(x1-p)*50/x1-6
        uranus.pos.y=-ellipse((x1-p),x1,y1)*25/x0
        neptune.pos.x=(x1-p)*54/x1-4
        neptune.pos.y=-ellipse((x1-p),x1,y1)*30/x0
        pluto.pos.x = -(x1-p)*6 +25
        pluto.pos.y = ellipse((x1-p)*x0/x1, x0, y0) * 6
        pluto.pos.z = 5 * p - 5 * x1
    #Third Quarter
    for p in np.linspace(x1,0,num=500):
        i+=0.01
        rate(30)
        mercury.pos.x=(-p)/1.5+1.4
        mercury.pos.y=ellipse((-p)*x0/x1,x0,y0)/1.5
        venus.pos.x=p-x1+0.5
        venus.pos.y=-ellipse((p-x1)*x0/x1,x0,y0)
        earth.pos.x=p*9/x1-1.5
        earth.pos.y=-ellipse(p,x1,y1)*5.5/x0
        moon.pos.x=p*9/x1-1.5+0.8*cos(i)
        moon.pos.y=-ellipse(p,x1,y1)*5.5/x0+0.8*sin(i)
        mars.pos.x=p*15/x1-2
        mars.pos.y=-ellipse(p,x1,y1)*7.5/x0
        jupiter.pos.x=p*34/x1-6
        jupiter.pos.y=-ellipse(p,x1,y1)*17/x0
        saturn.pos.x=(p-x1)*42/x1-4
        saturn.pos.y=-ellipse((p-x1),x1,y1)*21/x0
        uranus.pos.x=(p-x1)*50/x1-6
        uranus.pos.y=-ellipse((p-x1),x1,y1)*25/x0
        neptune.pos.x=(p-x1)*54/x1-4
        neptune.pos.y=-ellipse((p-x1),x1,y1)*30/x0
        pluto.pos.x = -(p - x1)*6 +25
        pluto.pos.y = ellipse((p - x1)*x0/x1, x0, y0) * 6
        pluto.pos.z = -5 * p + 5 * x1
    # Fourth Quarter/last quarter
    for p in np.linspace(0,-x1,num=500):
        i+=0.01
        rate(30)
        mercury.pos.x=(-p)/1.5+1.4
        mercury.pos.y=ellipse((-p)*x0/x1,x0,y0)/1.5
        venus.pos.x=-x1-p+0.5
        venus.pos.y=ellipse((-x1-p)*x0/x1,x0,y0)
        earth.pos.x=p*9/x1-1.5
        earth.pos.y=-ellipse(p,x1,y1)*5.5/x0
        moon.pos.x=p*9/x1-1.5+0.8*cos(i)
        moon.pos.y=-ellipse(p,x1,y1)*5.5/x0+0.8*sin(i)
        mars.pos.x=p*15/x1-2
        mars.pos.y=-ellipse(p,x1,y1)*7.5/x0
        jupiter.pos.x=p*34/x1-6
        jupiter.pos.y=-ellipse(p,x1,y1)*17/x0
        saturn.pos.x=(-x1-p)*42/x1-4
        saturn.pos.y=ellipse((-x1-p),x1,y1)*21/x0
        uranus.pos.x=(-x1-p)*50/x1-6
        uranus.pos.y=ellipse((-x1-p),x1,y1)*25/x0
        neptune.pos.x=(-x1-p)*54/x1-4
        neptune.pos.y=ellipse((-x1-p),x1,y1)*30/x0
        pluto.pos.x = -(-x1-p)*6 +25
        pluto.pos.y = -ellipse((-x1-p)*x0/x1, x0, y0) * 6
        pluto.pos.z = 5 * p + 5 * x1
while j==0:
    #first quarter
    #text(text="Coded by Crispine Wachira \nContact me via email:chrismwangicw@gmail.com \nLinkedIn:https:www.linkedin.com/in/mwangi-wachira-5a4b1a1a3", pos =vector(0,0,0), color=vector(0,1,0))
    loop()
