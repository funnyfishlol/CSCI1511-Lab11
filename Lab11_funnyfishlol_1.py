"""
Degrees of Rotation
Nathan Henneman
Takes an angle and adjusts it to remove unnecessary rotations if more than a full rotation is entered
November 9, 2025
"""

def adjust_angle(angle):
    try:
        if isinstance(angle,str):
            raise TypeError('You cant use strings')
    except TypeError as e:
        return None
    while(angle<0):
        angle+=360
    return (angle%360)