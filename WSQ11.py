def reverse_num(number):
    number = str(number)
    reverse = number[::-1]
    return(int(reverse))

def is_paly(m):
    if(m == reverse_num(m)):
        return False
    else:
        return True

def loopy(n):
    suma = 0
    for i in range(31):
        suma  = suma + n
        n = reverse_num(suma)
        result = is_paly(suma)
        if(result == False):
            return(result)
            exit()
    return(result)

def is_lychrel():
    for lyc in range(low,up + 1):
        if(loopy(lyc) == True):
            print("Found Lychrel number - ", lyc)
    print("")

def is_naturalpaly():
    natural = 0
    for paly in range(low,up + 1):
        paly = str(paly)
        if(paly == paly[::-1]):
            natural = natural + 1
    return(natural)

def is_nonLychrel():
    is_naturalpaly()
    counter = 0
    for lyc in range(low, up + 1):
        if(loopy(lyc) == False):
            counter = counter + 1
    print("Number of non-Lycherel numbers - ", counter - is_naturalpaly())

def is_candidate():
    counter = 0
    for lyc in range(low,up + 1):
        if(loopy(lyc) == True):
            counter = counter + 1
    print("Number of Lychrel candidates - ", counter)


low = int(input("Give me the lower bound -  "))
up = int(input("Give me the upper bound -  "))

is_lychrel()
print("Number of natural palindromes is:", is_naturalpaly())
is_nonLychrel()
is_candidate()
