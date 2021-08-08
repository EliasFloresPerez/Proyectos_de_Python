num=[1,2,3,4,5]
al=any([i>=4 for i in num]) #algunos
print(al)
al=all([i>=4 for i in num]) #todos
print(al)
#Listas comprimidas
even=[i < 4 for i in num]
print("Booleanos: ",even)
even=[i < 4 for i in range(10) if i%2==0]
print("En rango : ",even)