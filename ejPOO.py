"""Ejercicio único POO:
● Crear una clase llamada Punto con sus dos coordenadas X e Y.
● Añadir un método constructor para crear puntos fácilmente. Si no se recibe una
coordenada, su valor será cero.
● Sobreescribir el método string, para que al imprimir por pantalla un punto
aparezca en formato (X,Y)
● Añadir un método llamado cuadrante que indique a qué cuadrante pertenece el
punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0
e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
● Añadir un método llamado vector, que tome otro punto y calcule el vector
resultante entre los dos puntos.
● (Optativo) Añadir un método llamado distancia, que tome otro punto y calcule la
distancia entre los dos puntos y la muestre por pantalla. La fórmula es la
siguiente:"""

import math

class Punto :
    def __init__(self, x = 0, y = 0):
        self.coordenadaX = x
        self.coordenadaY = y


    def __str__(self):
        return f"({self.coordenadaX}, {self.coordenadaY})"


    def cuadrante (self):
        if self.coordenadaX != 0 & self.coordenadaY != 0:
            if self.coordenadaX > 0 & self.coordenadaY > 0:
                print(f"{self} se encuentra en el 1° Cuadrante")
            elif self.coordenadaX < 0 & self.coordenadaY > 0:
                print(f"{self} se encuentra en el 2° Cuadrante")
            elif self.coordenadaX < 0 & self.coordenadaY < 0:
                print(f"{self} se encuentra en el 3° Cuadrante")
            else:
                print(f"{self} se encuentra en el 4° Cuadrante")

        if self.coordenadaX == 0 & self.coordenadaY != 0:
            if self.coordenadaY > 0:
                print(f"{self} se encuentra sobre el lado positivo del Eje Y")
            else:
                print(f"{self} se encuentra sobre el lado negativo del Eje Y")

        if self.coordenadaX != 0 & self.coordenadaY == 0:
            if self.coordenadaX > 0:
                print(f"{self} se encuentra sobre el lado positivo del Eje X")
            else:
                print(f"{self} se encuentra sobre el lado negativo del Eje X")

        if self.coordenadaX == 0 & self.coordenadaY == 0:
            print(f"{self} se encuentra sobre el Origen")

    def vector (self, p):
        print(f"El vector entre {self} y {p} es ({p.coordenadaX - self.coordenadaX}, {p.coordenadaY - self.coordenadaY})")


    def distancia (self, p):
        d = math.sqrt ((p.coordenadaX - self.coordenadaX)** 2 + (p.coordenadaY - self.coordenadaY)** 2)
        print(f"La distancia entre {self} y {p} es ({d})")


"""Crear una clase llamada Rectángulo con dos puntos (inicial y final) que
formarán la diagonal del rectángulo.
● Añadir un método constructor para crear ambos puntos fácilmente, si no se
envían se crearán dos puntos en el origen por defecto.
● Añadir al rectángulo un método llamado base que muestre la base.
● Añadir al rectángulo un método llamado altura que muestre la altura.
● Añadir al rectángulo un método llamado area que muestre el area."""

class Rectángulo :
    def __init__(self , pInicial=Punto() , pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal

        self.vBase = abs(self.pFinal.coordenadaX - self.pInicial.coordenadaX)
        self.vAltura = abs(self.pFinal.coordenadaY - self.pInicial.coordenadaY)
        self.vArea = self.vBase * self.vAltura

    def base (self):
        print(f"La base del Réctangulo es {self.vBase}")


    def altura (self):
        print(f"La Altura del Réctangulo es {self.vAltura}")


    def area (self):
        print(f"El Área del Réctangulo es {self.vArea}")


"""Experimentación

● Crear los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
● Consultar a qué cuadrante pertenecen el punto A, C y D.
● Consultar los vectores AB y BA.
● (Optativo) Consultar la distancia entre los puntos 'A y B' y 'B y A'."""

A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

print(A)
print(B)
print(C)
print(D)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)







