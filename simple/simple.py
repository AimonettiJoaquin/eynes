import random
import operator

def dicc():
    
    """
    Test de diccionario
    >>> random.seed(1)
    >>> dicc()
    {'id 1': 17, 'id 2': 72, 'id 3': 97, 'id 4': 8, 'id 5': 32, 'id 6': 15, 'id 7': 63, 'id 8': 97, 'id 9': 57, 'id 10': 60}
    """
    mydicc = {}   
    for i in range(10):
        mydicc['id '+str(i+1)] = random.randrange(100)
    return mydicc



def ordenar(x):
    """
    Test Ordenar
    >>> ordenar(diccionario)
    [('id 10', 97), ('id 1', 83), ('id 9', 77), ('id 5', 62), ('id 8', 55), ('id 7', 49), ('id 2', 48), ('id 3', 26), ('id 4', 12), ('id 6', 3)]
    """
    myOrden = (sorted(x.items(), key=operator.itemgetter(1), reverse=True))
    return myOrden


diccionario = dicc()
orden = ordenar(diccionario)



if __name__=="__main__":
    import doctest
    doctest.testmod()
    print(orden[0], orden[-1])