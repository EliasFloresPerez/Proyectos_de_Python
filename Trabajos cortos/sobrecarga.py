class vector:
    def __init__(s,x,y):
        s.x = x
        s.y = y
    def __add__(primero,segundo):
        return vector (primero.x + segundo.x , primero.y + segundo.y)
primero =  vector(5,7)
segundo = vector(3,9)
resultado = primero + segundo #resultado = primero.__add__(segundo)

print(resultado.x,resultado.y)