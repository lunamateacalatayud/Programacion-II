# ejercicio 2
# Luna Mariana Calatayud
import random

class Juego:
    def __init__(self, vidas):
        self.numeroDeVidas = vidas
        self.record = 0

    def reiniciaPartida(self):
        print("\n Partida reiniciada")

    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
            print(f"Nuevo récord: {self.record}")

    def quitaVida(self):
        self.numeroDeVidas = self.numeroDeVidas - 1
        print(f"Quedan {self.numeroDeVidas} vidas")
        return self.numeroDeVidas > 0


class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0

    def validaNumero(self, n):
        if n >= 0 and n <= 10:
            return True
        else:
            return False

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivine un número entre 0 y 10")

        while True:
            intento = int(input("Ingresa el número: "))
            if self.validaNumero(intento) == False:
                print("Número inválido")
            if intento == self.numeroAAdivinar:
                print("Acertaste!!!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if intento < self.numeroAAdivinar:
                        print("El número es mayor")
                    else:
                        print("El número es menor")
                else:
                    print(f"Perdiste, el número era {self.numeroAAdivinar}")
                    break

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, n):
        if n < 0 or n > 10:
            return False
        if n % 2 != 0:
            print("El número no es par")
            return False
        return True

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, n):
        if n < 0 or n > 10:
            return False
        if n % 2 == 0:
            print("El número no es impar")
            return False
        return True

class Aplicacion:
    def main(self):
        print(" Juego para adivinar números")
        j1 = JuegoAdivinaNumero(3)
        j1.juega()

        print("\n Juego para adivinar números pares")
        j2 = JuegoAdivinaPar(3)
        j2.juega()

        print("\n Juego para adivinar números impares")
        j3 = JuegoAdivinaImpar(3)
        j3.juega()

app = Aplicacion()
app.main()
