from Est_Ingen import Ingenieria
from Est_Diseno import Diseno

class TabletaGrafica:
    def __init__(self, serial="", marca="", tamano=0.0, precio=0.0, almacenamiento="", peso=0.0):
        self._serial = serial
        self._marca = marca
        self._tamano = tamano
        self._precio = precio
        self._almacenamiento = almacenamiento
        self._peso = peso
        self.cantidad_tabletas = []

    # Métodos Get
    def get_serial(self):
        return self._serial

    def get_marca(self):
        return self._marca

    def get_tamano(self):
        return self._tamano

    def get_precio(self):
        return self._precio

    def get_almacenamiento(self):
        return self._almacenamiento

    def get_peso(self):
        return self._peso

    # Métodos Set
    def set_serial(self, serial):
        self._serial = serial

    def set_marca(self, marca):
        self._marca = marca

    def set_tamano(self, tamano):
        self._tamano = tamano

    def set_precio(self, precio):
        self._precio = precio

    def set_almacenamiento(self, almacenamiento):
        self._almacenamiento = almacenamiento

    def set_peso(self, peso):
        self._peso = peso

    def ingresar_tableta(self):
        # Validación para el serial
        while True:
            serial = input("Digite el serial de la tableta grafica: ")
            if serial.isalnum():
                self.set_serial(serial)
                break
            else:
                print("El serial solo debe contener letras y numeros")

        # Validación para la marca
        while True:
            marca = input("Digite la marca de la tableta grafica: ")
            if marca.isalpha():
                self.set_marca(marca)
                break
            else:
                print("La marca solo debe contener letras")

        # Validación para el tamaño
        while True:
            try:
                tamano = float(input("Digite el tamaño de la tableta grafica en pulgadas: "))
                if tamano <= 0:
                    print("El tamaño debe ser un número positivo")
                else:
                    self.set_tamano(tamano)
                    break
            except ValueError:
                print("Dato inválido, debe ser un número")

        # Validación para el precio
        while True:
            try:
                precio = float(input("Digite el precio de la tableta grafica: "))
                if precio <= 0:
                    print("El precio debe ser un número positivo")
                else:
                    self.set_precio(precio)
                    break
            except ValueError:
                print("Dato inválido, debe ser un número")

        # Submenú para el almacenamiento
        while True:
            print("Seleccione el almacenamiento:")
            print("1. 256 GB")
            print("2. 512 GB")
            print("3. 1 TB")
            opcion = input("Ingrese el número de la opción: ")
            if opcion == "1":
                self.set_almacenamiento("256 GB")
                break
            elif opcion == "2":
                self.set_almacenamiento("512 GB")
                break
            elif opcion == "3":
                self.set_almacenamiento("1 TB")
                break
            else:
                print("Opción inválida")

        # Validación para el peso
        while True:
            try:
                peso = float(input("Digite el peso de la tableta grafica en kg: "))
                if peso <= 0:
                    print("El peso debe ser un número positivo")
                else:
                    self.set_peso(peso)
                    break
            except ValueError:
                print("Dato inválido, debe ser un número")

    def agregar_tableta(self):
        tableta = {"Serial": self.get_serial(), "Marca": self.get_marca(), "Tamaño": self.get_tamano(),
                   "Precio": self.get_precio(), "Almacenamiento": self.get_almacenamiento(), "Peso": self.get_peso()}
        self.cantidad_tabletas.append(tableta)

    def mostrar_tableta(self):
        return self.cantidad_tabletas