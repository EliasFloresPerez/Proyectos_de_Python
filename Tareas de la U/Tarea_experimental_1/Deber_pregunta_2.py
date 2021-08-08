# ingreso ciudadaon !> a 35k ; impuesto igual a 12% menos 399 dolares y 2 centavos
# ingreso > 35k ; impuesto 24% (del excedente) mas 3500 y 2 centavos

#Input: float
#Output: redondeado
#impuesto no puede ser menor a cero

#Codigo 

def impuesto(ingreso):

    impuesto = 0
    #Extencion fiscal
    if ingreso <= 35000:
        impuesto = (ingreso*0.12)-399.2
        
    
    if ingreso > 35000:
        impuesto = ((ingreso - 35000)*0.24)+3500.2
    
    
    if impuesto < 0:
        impuesto = 0
    return float(round(impuesto))

ingreso =  float(input("Dame el ingreso anual: "))
print("El impuesto es: $",impuesto(ingreso)," dólares")