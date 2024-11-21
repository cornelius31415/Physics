#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:39:44 2024

@author: cornelius
"""
"""
                        REACHING ANDROMEDA GALAXY IN 15 YEARS
            
            Andromeda Galaxy is 2.5 million light years away from us.
            This means that light - which travels at the speed of 
            300,000 kilometers a second - would need 2.5 million years
            to reach Andromeda Galaxy.
            
            So basically unreachable for us.
            
            But there is a way, how we could reach Andromeda without 
            ever crossing the speed limit of light.
            
            By acceleration.
            
            If a spaceship travels with constant acceleration towards 
            Andromeda, such that the passengers would feel the effect 
            of earth's  gravitational acceleration g = 9.8 m/s^2, it 
            would take only 15 years from the passenger's perspective.
            
            The formula for the time passing on the spaceship
            can be derived with a lot of integrals.
            
            The final result is:
                
                t = (c/g) * arcosh( (g*D/c^2) + 1)
            
            c: speed of light
            g: acceleration
            D: distance to travel
            
            The following code implements this formula.
            T

"""



import numpy as np

acceleration = 9.8              # acceleration of spaceship in m/s^2
andromedaDistance = 2.5e6       # distance of Andromeda Galaxy in lightyears
speedOfLight = 3e8              # speed of light in m/s


def lightyearToKilometer(distance):
    
    # turn lightyears to kilometers
    lightyear = speedOfLight * 60 * 60 * 24 * 365
    
    # turn lightyear distance into kilometers
    distance_km = distance * lightyear 
    
    # return the distance in kilometers
    return distance_km
    

    

def travelTime(distance):
    
    # distance is given in lightyears
    # needs to be converted to meters
    distance = lightyearToKilometer(distance)
    
    # terms for the formula to calculate proper time
    term1 = speedOfLight / acceleration
    term2 = acceleration * distance / speedOfLight**2
    
    # final formula giving travel time in seconds
    timeOfTravel = term1 * np.arccosh(term2 + 1)
    # turn into years
    timeOfTravel = timeOfTravel /( 60 * 60 * 24 * 365)
    # round the result to 2 digits
    timeOfTravel = round(timeOfTravel,2)
    
    
    return timeOfTravel
    


timeToAndromeda = travelTime(andromedaDistance)

print("Travel time to Andromeda Galaxy is", timeToAndromeda, "years")







