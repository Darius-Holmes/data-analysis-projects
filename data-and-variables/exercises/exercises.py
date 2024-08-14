# 1. Declare and assign the variables here:

ShuttleName = 'Determination'
Speed = 17500
ToMars = 225000000
ToMoon = 384400
MilesPerKM = 0.621


# 2. Use print() to print the 'type' each variable. Print one item per line.

print(type(ShuttleName))
print(type(Speed))
print(type(ToMars))
print(type(ToMoon))
print(type(MilesPerKM))


# Code your solution to exercises 3 and 4 here:

MilesToMars = ToMars * MilesPerKM
HoursToMars = ToMars / Speed
DaysToMars = HoursToMars / 24


# Code your solution to exercise 5 here

print(ShuttleName, 'will take', DaysToMars, 'days to reach Mars')

print(ShuttleName, 'will take', ToMoon, 'days to reach the Moon')