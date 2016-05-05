import random
 
dot_product = 0
 
n = int(input("Por favor, inserta el valor de n: "))
 
v = [None] * n
w = [None] * n
 
for i in range(0, n):
v[i] = random.randint(1, 100)
w[i] = random.randint(1, 100)
 
print(v)
print(w)
 
for i in range(0, n):
dot_product = dot_product + v[i] * w[i]
 
print("El producto escalar entre los 2 vectores es de " + str(dot_product))
