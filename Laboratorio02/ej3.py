# Luna Mariana Calatayud
import math
class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, v):
        nx = self.x + v.x
        ny = self.y + v.y
        nz = self.z + v.z
        return Vector3D(nx, ny, nz)
    def __mul__(self, r):
        nx = self.x * r
        ny = self.y * r
        nz = self.z * r
        return Vector3D(nx, ny, nz)
    def modulo(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    def normal(self):
        mod = self.modulo()
        if mod == 0:
            return Vector3D(0, 0, 0)
        nx = self.x / mod
        ny = self.y / mod
        nz = self.z / mod
        return Vector3D(nx, ny, nz)
    def productoPunto(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z
    def productoCruz(self, v):
        nx = self.y * v.z - self.z * v.y
        ny = self.z * v.x - self.x * v.z
        nz = self.x * v.y - self.y * v.x
        return Vector3D(nx, ny, nz)
    
a = Vector3D(1, 2, 3)
b = Vector3D(4, 5, 6)
c = a + b
print(f"Suma: {c.x:.3f} {c.y:.3f} {c.z:.3f}")
d = a * 2
print(f"Escalar: {d.x:.3f} {d.y:.3f} {d.z:.3f}")
print(f"Modulo a: {a.modulo():.3f}")
n = a.normal()
print(f"Normal: {n.x:.3f} {n.y:.3f} {n.z:.3f}")
print(f"Producto punto: {a.productoPunto(b):.3f}")
cruz = a.productoCruz(b)
print(f"Producto cruz: {cruz.x:.3f} {cruz.y:.3f} {cruz.z:.3f}")