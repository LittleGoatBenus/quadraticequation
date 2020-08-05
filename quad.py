#importing math for the square root option
import math
# importing the required module 
import matplotlib.pyplot as plt 
#importing symbols etc.
from sympy import symbols, solve




print("""

         _________
        / 2
-b +- \/ b  - 4 a c
------------------
        2 a



""")
#asking user their values for a b and c
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

def calculator(a,b,c): # function for calculating the values 
    discriminant = (b**2) - (4*a*c)
    solution1 = (-b-math.sqrt(discriminant))/(2*a)
    solution2 = (-b+math.sqrt(discriminant))/(2*a)
    return solution1, solution2


    

value = calculator(a,b,c)
print("solutions: ", value) # prints the values



