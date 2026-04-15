# ejercicio 1
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

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        print("Adivine un número entre 0 y 10")

        while True:
            intento = int(input("Ingresa el número: "))

            if intento<0 or intento>10:
                print("número invalido")

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


class Aplicacion:
    def main(self):
        juego = JuegoAdivinaNumero(3)
        juego.juega()


app = Aplicacion()
app.main()
