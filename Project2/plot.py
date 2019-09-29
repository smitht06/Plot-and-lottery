"""
Anthony Smith
SDEV300
LAB 2
graph plot
"""

#import math library
import math

#in range only works for int so create method that will work wiht floats
def floatRange(start,stop,step):
    while start < stop:
        yield start
        start += step

#methods to return the points between a min and max and the sin of those points
def sinPoint(min1, max1, step1):
    for num in floatRange(min1,max1,step1):
        print(round(num,2), round(math.sin(num),2))

#methods to return the points between a min and max and the cosin of those points
def cosinPoint(min2, max2, step2):
    for num in floatRange(min2,max2,step2):
        print(round(num,2), round(math.cos(num),2))

#methods to return the points between a min and max and the squareroot of those points
def squarerootPoint(min3,max3,step3):
    for num in floatRange(min3,max3,step3):
        print(round(num,2),round(math.sqrt(num),2))

#methods to return the points between a min and max and the log10 of those points
def log10Point(min3,max3,step3):
    for num in floatRange(min3,max3,step3):
        print(round(num,2),round(math.log10(num),2))

#intitialize methods and print to the user
sinPoint(-2*math.pi,2*math.pi,math.pi/64)
print("")
print("Cosin")
cosinPoint(-2*math.pi,2*math.pi,math.pi/64)
print("")
print("Squareroot")
squarerootPoint(0,200,.5)
print("")
print("Log 10")
#log10 of 0 is undefined, starting at 1
log10Point(1,200,.5)