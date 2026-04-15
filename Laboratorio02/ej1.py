# Luna Mariana Calatayud
import math
class MiPunto:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distancia(self, punto):
        dx = self.__x - punto.getX()
        dy = self.__y - punto.getY()
        return math.sqrt(dx * dx + dy * dy)

    def distanciaXY(self, x, y):
        dx = self.__x - x
        dy = self.__y - y
        return math.sqrt(dx * dx + dy * dy)
    
p1 = MiPunto()
p2 = MiPunto(10, 30.5)
dist = p1.distancia(p2)
print(f"Distancia: {dist:.3f}")