from math import *
def f(x):
    return eval("x**3+3*x**2+12*x+8")

def biseccion(a,b,tol):
    m1 = a
    m = b
    k = 0
    if(f(a)*f(b)>0):
        print("La funcion no cambia de signo")
    
    while(abs(m1-m)>tol):
        m1=m
        m = (a+b)/2
        if(f(a)*f(m)<0): #Cambia de signo en [a,m]
            b = m
        if(f(m)*f(b)<0): #Cambia de signo en [m,b]
            a = m
        print("El intervalo es [",a,",",b,"]")
        k = k+1

    print("x",k,"=",m,"Es una aproximacion")

biseccion(-5,5,10**(-6))