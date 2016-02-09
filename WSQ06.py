from random import

rand_num=randint(1,100)
guess= (int(input("I'm thinking of a number from 1 to 100. Guess it --> ")))

while (guess !=rand_num):

    if (guess>rand_num):
        guess= (int(input("Number too big. Try again --> ")))

    else:
        guess= (int(input("Number too short.Try again --> ")))

else:
    print ("Congrats!! You guessed my number")
