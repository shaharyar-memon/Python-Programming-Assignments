#Q1
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")
#Q2
import sys
print(sys.version)
print(sys.version_info)
#Q3
import datetime
current_dt = datetime.datetime.now()
print(current_dt.strftime("%d-%m-%Y %H:%M:%S"))
#Q4
import math
rad = int(input("Enter radius of circle : "))
area = math.pi * rad**2
print(area)
#Q5
fname = input("Enter first name : ")
lname = input("Enter last name : ")
print(lname + " " + fname)
#Q6
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
r = n1 + n2
print(n1, " + ", n2, " = ", r)