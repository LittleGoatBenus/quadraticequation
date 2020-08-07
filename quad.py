import math #importing math for square root
import matplotlib.pyplot as plt # importing the graph plotter
import numpy as np #importing numpy for math expressions
import time


print("""

         _________                   .
        / 2                     |    .  |
-b +- \/ b  - 4 a c             |    .  |
------------------           . .|. . . .| . . .
        2 a                      \ _ _ /
                                     .
Quadratic equation calculator        .
                            with graph plotter
""")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))



def x(a,b,c):
    discriminant = (b**2) - (4*a*c)
    solution1 = (-b-math.sqrt(discriminant))/(2*a)
    return solution1

def x1(a,b,c):
    discriminant = (b**2) - (4*a*c)
    solution2 = (-b+math.sqrt(discriminant))/(2*a)
    return solution2

#def y(x_one, a, b, c):                      #these 2 functions were written to check if x was correct, if so they would always return 0
#    y1 = ((a*x_one**2)+(b*x_one)+(c))       # since the roots or solutions for the equation is were y = 0 or were the graph touches the x axis
#    return y1

#def y1(x_two, a, b, c):
#    y2 = ((a*x_two**2)+(b*x_two)+(c))
#    return y2

x_one = x(a,b,c)
x_two = x1(a,b,c)

#y_one = y(x_one,a,b,c)
#y_two = y1(x_two,a,b,c)

print("your coordinates are ({},0.0) ({},0.0)".format(x_one, x_two, ))

print("""please give the x axis range, put it alot greater and smaller than your x values,
put negative range first then posotive range
example: my x's are -2 and -3 , my range would be -43 and 37""")
print("recommended: atleast 40 greater and smaller than your x values")
fr0m = int(input("x-axis from: "))
t0 = int(input("to: "))

def graph(a, b, c, fr0m, t0):
    x = list(range(fr0m, t0))
    y = [(a*i**2 + b*i + c) for i in x]
    plt.plot(x, y)


graph(a,b,c,fr0m,t0)
plt.show(block=False)
plt.pause(1000)
