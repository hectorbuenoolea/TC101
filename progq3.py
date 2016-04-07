import math

print ("This program will calculate the distance between two cartesian points given (x1,y1) and (x2,y2)")
x1 = int(input("Give me X1 -> "))
y1 = int(input("Give me Y1 -> "))
x2 = int(input("Give me X2 -> "))
y2 = int(input("Give me Y2 -> "))

def hyp (x1,y1,x2, y2):
    h = math.sqrt(((x1-x1)**2) + ((y1-y2)**2)
    return h

print (hyp(x1, y1, x2, y2))
