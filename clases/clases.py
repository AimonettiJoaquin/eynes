import math
import turtle
class Circle:
    """
    Test de Circle
    >>> r = 4
    >>> obj = Circle(r)
    >>> round(obj.area(),2)
    50.27
    >>> round(obj.perimeter(),2)
    25.13
    """
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        area = math.pi *(self.radius**2)
        return area
    def perimeter(self):
        perimeter = 2* math.pi * self.radius
        return perimeter

r = int(input("Ingrese el radio del circulo: "))
if(r<=0):
    print("Ingrese un radio mayor a 0")
else:
    obj = Circle(r)
    print("El area del circulo: ", round(obj.area(),2))
    print("El perimetro del circulo: ", round(obj.perimeter(),2))     
    turtle.circle(r)
    

if __name__=="__main__":
    import doctest
    doctest.testmod()
    