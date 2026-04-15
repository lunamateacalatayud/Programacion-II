# Luna Mariana Calatayud
import math
class AlgebraVectorial:
    def __init__(self, ax=0, ay=0, bx=0, by=0):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
    def moduloA(self):
        return math.sqrt(self.ax * self.ax + self.ay * self.ay)
    def moduloB(self):
        return math.sqrt(self.bx * self.bx + self.by * self.by)
    def productoPunto(self):
        return self.ax * self.bx + self.ay * self.by
    def productoCruz(self):
        return self.ax * self.by - self.ay * self.bx
    def perpendicular1(self):
        sumax = self.ax + self.bx
        sumay = self.ay + self.by
        restax = self.ax - self.bx
        restay = self.ay - self.by
        modSuma = math.sqrt(sumax * sumax + sumay * sumay)
        modResta = math.sqrt(restax * restax + restay * restay)
        return modSuma == modResta
    def perpendicular2(self):
        resta1x = self.ax - self.bx
        resta1y = self.ay - self.by
        resta2x = self.bx - self.ax
        resta2y = self.by - self.ay
        mod1 = math.sqrt(resta1x * resta1x + resta1y * resta1y)
        mod2 = math.sqrt(resta2x * resta2x + resta2y * resta2y)
        return mod1 == mod2
    def perpendicular3(self):
        return self.productoPunto() == 0
    def perpendicular4(self):
        sumax = self.ax + self.bx
        sumay = self.ay + self.by
        lado1 = sumax * sumax + sumay * sumay
        lado2 = self.ax * self.ax + self.ay * self.ay + self.bx * self.bx + self.by * self.by
        return lado1 == lado2
    def paralela1(self):
        if self.bx != 0:
            r = self.ax / self.bx
            return self.ay == r * self.by
        return False
    def paralela2(self):
        return self.productoCruz() == 0
    def proyeccion(self):
        punto = self.productoPunto()
        modb = self.moduloB()
        if modb == 0:
            return (0, 0)
        escalar = punto / (modb * modb)
        px = escalar * self.bx
        py = escalar * self.by
        return (px, py)
    def componente(self):
        punto = self.productoPunto()
        modb = self.moduloB()
        if modb == 0:
            return 0
        return punto / modb
    
v = AlgebraVectorial(3, 4, 4, -3)
print("Perpendicular (producto punto):", v.perpendicular3())
print("Paralela (producto cruz):", v.paralela2())
px, py = v.proyeccion()
print("Proyeccion:", px, py)
print("Componente:", v.componente())