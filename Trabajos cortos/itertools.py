from itertools import accumulate , takewhile, count , cycle , repeat ,chain
num = [5,4,3,2,1]
#Acumalete acumula con el anterior
nums = list(accumulate(num))
print(nums)
#Mientras una funcion sea verdadera mostrara el valor como filter
print(list(takewhile(lambda x: x<=10,nums)))
#count " repite infinitamente desde el punto el segundo valor los saltos"
def reversa():
    for i in count(30,-3):
        if i <= 0:
            break
        yield i
for i in reversa():
    print(i)
#Repeat Repite algo un numeor de veces "iterable"
print(list(repeat("Elias",5)))
#Cycle Repite algo iterable infinitamente
fin = 0
for i in cycle("Elias"):
    if fin == 5:
        break
    else:
        print(i)
        fin += 1

#chain Combina iterables
print(list(chain([5,4,3],[2,1,0],[-1,-2])))