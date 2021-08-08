x = 0
while(x==0):
    x = float(input("Dame el valor de x :"))
    if x == 0:
        print("No existe la division entre  0 ingrese un valor valido")

total = 1/(x+1/(x+1/(x+1/x)))
print(total)
