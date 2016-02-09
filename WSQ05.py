f=int(input("Enter a Temperature in Fahrenheit -> "))
c=((5*f)-32)/9
print (f, "Fahrenheit =", c,  "Celsius")

if (c>100):
    print ("Water boils at this Temperature (under typical conditions).")
else:
    print ("Water does NOT boils at this Temperature (under typical conditions).")
