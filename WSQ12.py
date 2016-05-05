def find (word):
    archivo = open("prueba.txt")
    text = archivo.read()
    list = text.split(" ")
    cant = 0

    for n in list:
        print (n)
        if(n.lower()==word):
            cant+= 1
    return cant

word = input("What word are you looking for? -->")
print ("repetions = ",find(word))
