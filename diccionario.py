diccionario = {
    1:"apple",
    "orange": [2,3,4],
    True: False,
    None:"True",
}
print(diccionario.get("orange"))#Devuelve la lista
print(diccionario.get(None))#Devuelve true
print(diccionario.get("ora"))#Devuelve none
print(diccionario.get(True))#Devuelve false
print(diccionario.get("orang","This is invalid"))#Devuelve lo del segundo argumentoHasta valores int
