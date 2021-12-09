from _typeshed import Self
import math
class Vecteur:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def norme():
        n=math.sqrt(Self.x**2+Self.y**2)
        return n
