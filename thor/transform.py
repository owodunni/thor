#!/usr/bin/env python3

from numpy import *
import transforms3d.axangles as rotations


def getRotationMatrix(axis, degrees):
    """
    Input: 
        Rotation axis, angle to rotate
    Output: 
        Rotation matrix (3x3)
    """
    angle = radians(degrees)
    return rotations.axangle2mat(axis, angle)


def lonLatToCart(lonLat):
    """
    Input: 
        Lon,lat as numpy vector
    Output:
        Cartesian coordinates, denoting earth radius as 1 unit
    """
    lon = radians(lonLat[0])
    lat = radians(lonLat[1])

    xCoord = sin(lon)
    # yCoord is upwards, computer graphics style
    yCoord = sin(lat)
    # zCoord is "towards the observer", computer graphics style
    zCoord = cos(lon)

    return vector(xCoord, yCoord, zCoord)


def cartToLonLat(cart):
    """
    Input: 
        Carthesian coordinates as numpy vector
    Output:
        Lon,lat as numpy vector
    """
    xCoord = cart[0]
    yCoord = cart[1]
    zCoord = cart[2]
    
    lon = 0
    if zCoord > 0:
        lon = arcsin(x)
    if zCoord < 0:
        lon = pi - arcsin(x)
    else:
        lon = 0
    
    lat = 0
    if yCoord != 0:
        lat = arcsin(yCoord/earthRadius)
    else:
        lat = 0

    return array(lon, lat)


def regFromRot(lon, lat):
    """
    Takes rotated coordinates and outputs regular coordinates
    """
    rotatedCoord = lonLatToCart([lon, lat])
    # Axises to rotate around
    xAxis = vector([1,0,0])
    yAxis = vector([0,1,0])
    zAxis = vector([0,0,1])
    # South Pole location in rotated coordinate system
    spRotLon = -162
    spRotLat = 39.25
    # How far to rotate around Y
    angleY = 0-spRotLon
    # How far to rotate around Z
    angleX = -90-spRotLat
    
    # Create rotation matrixes
    Ry = getRotationMatrix(yAxis, angleY)
    Rx = getRotationMatrix(xAxis, angleZ)
    
    # Get regular cart coordinates
    regCartCoord = Rx * Ry * rotatedCoord

    return cartToLonLat(regCartCoord)



