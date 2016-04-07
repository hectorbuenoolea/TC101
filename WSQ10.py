from statistics import *
print ("Ill ask you for 10 numbers...")

list = [float(input("1st - ")), float(input("2nd - ")),
        float(input("3rd - ")), float(input("4th - ")),
        float(input("5th - ")), float(input("6th - ")),
        float(input("7th - ")), float(input("8th - ")),
        float(input("9th  ")), float(input("10th - "))]

print ("The sum of the numbers you gave is -  ", sum(list))
print ("The mean of the list is -  ",mean (list))
print ("The average deviations is -  ", pstdev (list))
