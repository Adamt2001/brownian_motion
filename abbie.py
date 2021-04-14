# this code was created to help my friend with their uni work haha, I've got no real work with numpy or pylab, so this
# is just a github/w3schools/stack overflow special

import numpy as np
import random
import math
import pylab
step = 1
num_steps = 1000
num_experiments = 10

x = 0.0
y = 0.0

xdata = [x]
ydata = [y]

# function to relay the brownian motion of random motion of particles suspended in a medium more info below
# https://en.wikipedia.org/wiki/Brownian_motion#:~:text=Brownian%20motion%2C%20or%20pedesis%20(from,a%20liquid%20or%20a%20gas).
# it will create a random particle and change its location to a random angle and take a step
def brownian(x,y,step):
    global xdata, ydata
    for i in range(num_steps):
        angle = random.random()*2*math.pi
        x = x + np.cos(angle)*step
        y = y + np.sin(angle)*step
        xdata.append(x)
        ydata.append(y)

# this will run the brownian function and plot the first and last steps with a green and red dot respectfully
brownian(x,y,step)
pylab.plot(xdata[0:],ydata[0:])
pylab.plot(xdata[0],ydata[0], "go")
pylab.plot(xdata[-1],ydata[-1], "ro")
pylab.show()

# printing out data for debugging
print("start at x= ", xdata[0], " and y= ", ydata[0])
print("end at x= ", xdata[-1], " and y= ", ydata[-1])
print(xdata)


# MSD (mean squared displacement) creates an array to store all of values of the next function
msd = []

# this will create graph 2 to show the overall increase in MSD over the number of steps to the power of 10
def norm():
    global num_steps,msd
    counter = 10
    working = 0
    while counter <= num_steps - 10:
        x = xdata[counter] - xdata[0]
        y = ydata[counter] - ydata[0]
        answer = (math.sqrt((x**2)+(y**2)))**2
        working = working + answer
        msd.append(working)
        counter = counter + 10

norm()

# plots graph 2 with the correct titles using the MSD array for the values
pylab.xlabel("Number of steps (*10)")
pylab.ylabel("MSD")
pylab.plot(msd)
pylab.show()
