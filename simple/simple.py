from random import randrange
import operator

def dicc():
    mydicc = {}   
    for i in range(10):
        mydicc['id '+str(i+1)] = randrange(100)
    return mydicc



def ordenar(x):
    myOrden = (sorted(x.items(), key=operator.itemgetter(1), reverse=True))
    return myOrden


diccionario = dicc()
orden = ordenar(diccionario)

print(orden[0], orden[-1])