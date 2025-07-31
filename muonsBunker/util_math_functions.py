import math
from decimal import *
import numpy as np

# p1 and p2 are the points, d1 and d2 are the direction vectors
# each trajectory is represented by a point p on it, and a direction
# vector d
def POCA(p1, d1, p2, d2):
    
    # these parametric equations represent the lines
    first_parametric = ((d1[0], p1[0]), (d1[1], p1[1]), (d1[2], p1[2]))
    second_parametric = ((d2[0], p2[0]), (d2[1], p2[1]), (d2[2], p2[2]))
    # subtract the two parametrics to get the length between
    p1p2 = ((d2[0], -d1[0], p2[0]-p1[0]),
            (d2[1], -d1[1], p2[1]-p1[1]),
            (d2[2], -d1[2], p2[2]-p1[2]))
    # use dot product to obtain system of equations to solve
    dotProd_d1 = (p1p2[0][0]*d1[0]+p1p2[1][0]*d1[1]+p1p2[2][0]*d1[2],
                  p1p2[0][1]*d1[0]+p1p2[1][1]*d1[1]+p1p2[2][1]*d1[2],
                  p1p2[0][2]*d1[0]+p1p2[1][2]*d1[1]+p1p2[2][2]*d1[2])
    
    dotProd_d2 = (p1p2[0][0]*d2[0]+p1p2[1][0]*d2[1]+p1p2[2][0]*d2[2],
                  p1p2[0][1]*d2[0]+p1p2[1][1]*d2[1]+p1p2[2][1]*d2[2],
                  p1p2[0][2]*d2[0]+p1p2[1][2]*d2[1]+p1p2[2][2]*d2[2])
    
    # now we have systems of equations, solve it
    # first multiply to get rid of the first variable
    manip_eq1 = [dotProd_d2[0]*x for x in dotProd_d1]
    manip_eq2 = [dotProd_d1[0]*x for x in dotProd_d2]
    subtract = [manip_eq2[i]-manip_eq1[i] for i in range(len(manip_eq1))]
    second_var = -subtract[2]/subtract[1]
    # get rid of the second variable
    manip_eq1 = [dotProd_d2[1]*x for x in dotProd_d1]
    manip_eq2 = [dotProd_d1[1]*x for x in dotProd_d2]
    subtract = [manip_eq2[i]-manip_eq1[i] for i in range(len(manip_eq1))]
    first_var = -subtract[2]/subtract[0]

    # get the two points where the vectors get closest
    point1 = [d1[i]*second_var+p1[i] for i in range(3)]
    point2 = [d2[i]*first_var+p2[i] for i in range(3)]

    # find the midpoint of the two points -> POCA
    closest_approach = [0.5*(point1[i]+point2[i]) for i in range(3)]
    return tuple(closest_approach)

def angleBetween(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    angle = math.degrees(math.acos(np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))))
    if angle > 90:
        angle = 180-angle
    return angle

def subtract(v1, v2):
    return tuple(np.array(v1) - np.array(v2))

def test():
    print(POCA((1,1,1),(-1,1,1),(1,1,1),(1,1,1)))
    print(subtract((0,0,0),(-3,-5,2)))
    print(angleBetween((1,1,1),(-1,-1,-1)))
    print(angleBetween((2,4,5),(-2,6,-4)))

if __name__ == '__main__':
    test()
