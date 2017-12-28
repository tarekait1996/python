''' this is question 1 of the assignment'''
import math


class Line(object):
    def __init__ (self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        distance = abs( ((self.coor1[0] - self.coor2[0])**2 +(self.coor1[1] - self.coor2[1])**2)**(1/2))
        return distance
    def slope (self):
        slope = ((self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0]))
        return slope


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
di = li.distance()
sl = li.slope()

print('DISTANCE: ', di, ', SLOPE: ', sl)

''' this is question 2 of the assignment on OOP'''
import math
class Cylinder(object):
    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius
    def volume(self):
        return (math.pi * self.radius**2 *self.height)
    def surface_area(self):
        return ((2* math.pi * self.radius**2) + (2 * math.pi * self.radius*self.height))

c = Cylinder(2,3)
v = c.volume()
a = c.surface_area()

print('volume of the cylinder: %1.2f, surface area of the cylinder: %1.2f'%(v,a))