# 1. Find the roots of given Quadratic Equation

import math


a = float(input("Please enter the coefficent of x^2: "))
while a==0:
    a = float(input("coefficent of x^2 can not be 0, input again: "))

b = float(input("Please enter the coefficent of x: "))
c = float(input("Please enter the free  term: "))

delta = (b*b)-(4*a*c)
if delta >=0:
        x_one = ((-b) + math.sqrt(delta)) / (2 * a)
        x_two = ((-b) - math.sqrt(delta)) / (2 * a)
        print("First root is: ", x_one, ", second root is: ", x_two)
else:
    print("Delta is negative")






