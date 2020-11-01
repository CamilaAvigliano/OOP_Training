"""Ejercicio 1:
Vamos a crear un Cliente. Sus atributos son: nombre, edad y DNI.
*Construir los siguientes métodos para la clase:
*Un constructor, donde los datos pueden estar vacíos.
-Muestra los datos de la persona.
-Devuelve un valor lógico indicando si es mayor de edad."""

class Persona:
    def __init__(self, nombre="", edad="", dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        print(f"""Nombre: {self.nombre}
    Edad: {self.edad}
    DNI: {self.dni}""")

    def esMayorDeEdad(self):
        if int(self.edad) >= 18:
            print(f"{self.nombre} es mayor de edad")
            return True




"""
Ejercicio 2:
Crea una Cuenta que tendrá los siguientes atributos: 
*Titular y cantidad (puede tener decimales). 
*El titular será obligatorio y la cantidad es opcional. 
*Construir los siguientes métodos para la clase:
    Un constructor, donde los datos pueden estar vacíos.
    El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
    -Muestra los datos de la cuenta.
    -Ingresa una cantidad a la cuenta.
    -Si la cantidad introducida es negativa, no se hará nada.
    -Se retira una cantidad a la cuenta. 
    **La cuenta puede estar en números rojos.
"""


class Cuenta:
    def __init__(self, titular=Persona(), cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f"""Titular de la cuenta: {self.titular}
Cantidad de dinero disponible: {self.cantidad}""")

    def ingresar(self):
        monto_i = float(input("Ingrese la cantidad de dinero: "))
        if monto_i >= 0:
            self.cantidad += monto_i

    def retirar(self):
        monto_r = float(input("Retire la cantidad de dinero: "))
        self.cantidad -= monto_r


"""
Ejercicio 3:
Vamos a definir ahora una “Cuenta Joven”:
-Deriva de la anterior. 
Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. 
Construir los siguientes métodos para la clase:
    Un constructor.
    -En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad pero menor de 25 años 
    -Además la retirada de dinero sólo se podrá hacer si el titular es válido.
    -Debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
    Pensar los métodos heredados de la clase madre que hay que reescribir.
"""


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def esTitularValido(self):
        if self.titular.esMayorDeEdad() and self.titular.edad < 25:
            return True
        else:
            return False

    def retirar(self):
        validez = self.esTitularValido()
        if validez:
            print("Puede retirar dinero.")
            retiro = float(input("Retire dinero o presione 0 para salir: "))
            if retiro != 0:
                self.cantidad -= retiro
            print(f"En su cuenta quedan: $ {self.cantidad} ")
        else:
            print("Debes presentar autorización para retirar dinero")


    def mostrar(self):
        print("Cuenta Joven:")
        print(f"Bonificación -> {self.bonificacion}%")



user = Persona("Camila Avigliano", 23 , 40567432)
print(user.esMayorDeEdad())
print(user.mostrar())

userAccount = Cuenta( user.nombre, 5000)
print(userAccount.ingresar())
print(userAccount.retirar())
print(userAccount.mostrar())


cta_joven = CuentaJoven(user, userAccount.cantidad, 50)
print(cta_joven.esTitularValido())
cta_joven.retirar()
cta_joven.mostrar()
