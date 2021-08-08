import numpy as np
def f(x):
    return eval("x**3+3*x**2+12*x+8")

def regla_falsa(a,b,total):
    m_1 = a
    m_2 = b
    error = total
    seg=abs(m_2-m_1)
    #Procedimiento
    while not(seg<=error):
        fa = f(m_1)
        fb = f(m_2)
        c = m_2 - fb*(m_1-m_2)/(fa-fb)
        fc = f(c)
        
        cambio =  np.sign(fa)*np.sign(fc)
        
        if cambio>0:
            seg = abs(c-m_1)
            m_1 = c
        else:
            seg = abs(c-m_2)
            m_2 = c
        print("El intervalo es [",m_1,",",m_2,"]")
    print(c)
   

regla_falsa(-5,5,10**(-6))