a = int(input("Give me a number --> "))
b = int(input("Give me another numer -->"))

def sumab(a,b):
    c = a + b
    return (c)

def subs(a,b):
    c = a - b
    return (c)

def div(a,b):
    c = a // b
    return (c)

def res(a,b):
    c = a % b
    return (c)

print (a, "+", b, "=", sumab(a,b))
print (a, "-", b, "=", subs(a,b))
print (a, "/", b, "=", div(a,b))
print (a, "%", b, "=", res(a,b))
