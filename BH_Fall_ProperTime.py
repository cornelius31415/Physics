#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 10:14:34 2023

@author: cornelius
"""

import numpy as np
import matplotlib.pyplot as plt

c = 3e8 # speed of light in meters per second
G = 6.67e-11 # gravitational constant in m^3/(kg s^2)
sun = 1.988e30 # solar mass in kg
initial_spot = 1e13 # initial distance from the singularity in meters
initial_speed = 1e4 # inital speed in meters per second
r0 = 1e13
v0 = 1e4


def event_horizon(M):
    r_S = 2*M*G/c**2  # Schwarzschild radius
    return round(r_S,2)

event_sun = event_horizon(sun)
# print("The event horizon of the sun is: ", event_sun, "meters")

# print(event_horizon(7*sun))
M = 4e6*sun


'''
x = np.linspace(1.5e13,1e14,10000)

def function(r):
    
    b = event_horizon(M)
    alpha0 = 1-(b/r)
    a = ((1-(b/r))/(1-((1-(b/r))**-2)*v0**2*(c**-2)))-1
    return a
plt.plot(x,function(x))
plt.show()
'''

# THOSE CALCULATIONS DO NOT WORK
# THE INTEGRAL BRAKES DOWN 
# ONLY NUMERICAL INTEGRATION WORKS
# FOR LARGE INITIAL SPOTS R0 THE INTEGRAL YIELDS THE
# SAME RESULT AS THE NUMERICAL INTEGRATION
'''
def time_to_fall(M):

    b = event_horizon(M)
    alpha0 = 1-(b/initial_spot)
    a = 1- (alpha0/(1-(alpha0**-2)*initial_speed**2*(c**-2)))
    t0 = (r0*np.sqrt(a+(b/r0)))/a - b*np.arctanh(np.sqrt(1+b/(r0*a)))/a**1.5
    t1 = (b*np.sqrt(a+(b/b)))/a - b*np.arctanh(np.sqrt(1+b/(b*a)))/a**1.5
    return (t0-t1)/(c*60*60*24*365)

    t0 = (1/np.sqrt(a))*(
        np.sqrt(r0**2+(b*r0/a))
        - b/(2*a) * np.arccosh(
            (2*a/b)*(r0+(b/(2*a)))
            )
        )
    t1 = (1/np.sqrt(a))*(
        np.sqrt(b**2+(b*b/a))
        - b/(2*a) * np.arccosh(
            (2*a/b)*(b+(b/(2*a)))
            )
        )
    return (t0-t1)/(c*60*60*24*365)

#print(time_to_fall(M))
'''




# NUMERICAL INTEGRATION


from scipy.integrate import quad

M = 13.5e30
M = 4.1e6*sun
M = 13.5e30
def integrand(r):
    b = event_horizon(M)
    alpha0 = 1-(b/initial_spot)
    a = (alpha0/(1-(alpha0**-2)*initial_speed**2*(c**-2)))-1
    return -(1/c)*(np.sqrt(a+b/r))**-1
    
I = quad(integrand,initial_spot,event_horizon(M))
print("Fall Time: ",I[0]/(60*60*24*365),"years")



'''
# APPROXIMATION FROM TEXT BOOK SOLUTION
a = initial_spot/initial_speed # I need
b = 2*M*G
C = initial_speed**2 * initial_spot
d = b/C # I need
e = 1+d
f = np.sqrt(e) # I need
g = C/b
h = np.sqrt(g)
i = np.arcsinh(h) # I need
ergebnis = a*(f-d*i)
print(ergebnis/(60*60*24))
'''


# ENERGY SET TO 1
def time(M,r0):
    rs = event_horizon(M)
    time = (2/3) * (r0*np.sqrt(r0/rs)-rs)
    return time/c
    
print(time(M,initial_spot)/(60*60*24*365))



























