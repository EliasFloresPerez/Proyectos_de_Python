def imc(a,b):
    if a<1 or a>2.5 or b<20 or b>200:
        return "Datos no validos"
    else:    
        return round(b/pow(a,2),2)

altura = float(input("Deme su altura en metros : "))
peso = float(input("Deme su peso en Kilogramos : "))

print(imc(altura,peso))