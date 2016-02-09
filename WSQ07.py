while True:
    try:
        print("-- Give me a Range --")
        a = int(input("A --> "))
        b = int(input("B --> "))

        if (a > b):
            print("A needs to be smaller than B")

        elif(a == b):
            print("A needs to be smaller than B")

        else:
            incl = 0
            for n in range(a,b+1):
                incl= incl + n

            print ("The inclusive sum of the numbers you gave me is", incl)
            break

    except ValueError:
        print("That is not a number.")
