from decimal import Decimal

def total(resultado,aprox):
  #Variables
  contador = 0
  contador_decimal = 0
  auxiliar = 0

  resultado = str(resultado)
  aprox =  str(aprox)

  
  #Funcion
  for x in range(len(aprox)):
      try:
        if resultado[x] == ".":
          auxiliar = 1
          continue
      except:
        continue

      if auxiliar == 0:
        if int(resultado[x])<=0.5:
          contador = contador + 1
      else:
        if int(resultado[x])<=0.5:
          contador_decimal = contador_decimal + 1
  print("Numeros exactos")
  for x in range(contador_decimal+contador+auxiliar):
    print(aprox[x],end="")    

  print("\nHay ",contador," cifras exactas y hay ", contador_decimal," de cifras decimales exactas")      
            
    

def cifras_exactas(exacta, aproximado):
  
  resultado=abs(exacta-aproximado)
  print("error absoluto --> ",resultado)
  
  total(resultado,aproximado)



cifras_exactas(Decimal('4'),Decimal('3.52'))