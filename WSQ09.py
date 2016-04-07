def calc():
    while True:
        try:
            n = int(input("Give me a positive integer (not 0)-> "))
            if (n <= 0):
                print("NEGATIVE NUMBER - INVALID ENTRY")
            else:
                break
        except ValueError:
            print("INVALID ENTRY")

    factorial = 1

    for x in range(n):
        factorial = factorial * n
        n = n - 1
    print ("Factorial -> ", factorial)

calc()

while True:
    again= input("Do you want to try again? y/n -> ")
    if(again == "y"):
        again = input("Are you sure? ")
        if (again == "y"):
            calc()
        elif (again == "n"):
            print ("Ok! Have a nice day.")
            break
    elif (again == "n"):
        print ("Ok! Have a nice day.")
        break
