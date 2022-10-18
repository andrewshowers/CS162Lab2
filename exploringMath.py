"""Lab 2 – Working with Math

Andrew Showers
I certify that this work was done in accordance with
GV academic honesty policies.

Fall, 2022"""
import math

w = "3"
x = 3
y = 2
z = 2.0

print(type(w))
print(type(x))
print(type(y))
print(type(z))


userinput = input('please enter the amount of seconds you would like converted')
userinput = (int(userinput))
hours = userinput//3600
userinput %= 3600
minutes = userinput//60
userinput %= 60
seconds = userinput
print(hours, 'hour(s)')
print(minutes, 'minute(s)')
print(seconds, 'second(s)')


print(type(math.radians(50)))

degrees = 5
print("The number of degrees is " + str(degrees))

name = "Andrew Showers"
age = 19
favoriteNumber = 24.0

print("Hello there. My name is " + name + '. I am ' + str(age) + '.  My favorite number is', favoriteNumber)
