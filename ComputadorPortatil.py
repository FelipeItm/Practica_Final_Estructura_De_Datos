class ComputadorPortatil:
    def __init__(self, serial="", marca="", tamano=0.0, precio=0.0, sistema_operativo="", procesador=""):
        self._serial = serial
        self._marca = marca
        self._tamano = tamano
        self._precio = precio
        self._sistema_operativo = sistema_operativo
        self._procesador = procesador
        self.cantidad_computadores = []

    # Métodos Get
    def get_serial(self):
        return self._serial

    def get_marca(self):
        return self._marca

    def get_tamano(self):
        return self._tamano

    def get_precio(self):
        return self._precio

    def get_sistema_operativo(self):
        return self._sistema_operativo

    def get_procesador(self):
        return self._procesador

    # Métodos Set
    def set_serial(self, serial):
        self._serial = serial

    def set_marca(self, marca):
        self._marca = marca

    def set_tamano(self, tamano):
        self._tamano = tamano

    def set_precio(self, precio):
        self._precio = precio

    def set_sistema_operativo(self, sistema_operativo):
        self._sistema_operativo = sistema_operativo

    def set_procesador(self, procesador):
        self._procesador = procesador

    def ingresar_computador(self):
        # Validación para el serial
        while True:
            serial = input("Digite el serial del computador portátil: ")
            if serial.isalnum():
                self.set_serial(serial)
                break
            else:
                print("El serial solo debe contener letras y numeros")

        # Validación para la marca
        while True:
            marca = input("Digite la marca del computador portátil: ")
            if marca.isalpha():
                self.set_marca(marca)
                break
            else:
                print("La marca solo debe contener letras")

        # Validación para el tamaño
        while True:
            try:
                tamano = float(input("Digite el tamaño del computador portátil en pulgadas: "))
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
                precio = float(input("Digite el precio del computador portátil: "))
                if precio <= 0:
                    print("El precio debe ser un número positivo")
                else:
                    self.set_precio(precio)
                    break
            except ValueError:
                print("Dato inválido, debe ser un número")

        # Submenú para el sistema operativo
        while True:
            print("Seleccione el sistema operativo:")
            print("1. Windows 7")
            print("2. Windows 10")
            print("3. Windows 11")
            opcion = input("Ingrese el número de la opción: ")
            if opcion == "1":
                self.set_sistema_operativo("Windows 7")
                break
            elif opcion == "2":
                self.set_sistema_operativo("Windows 10")
                break
            elif opcion == "3":
                self.set_sistema_operativo("Windows 11")
                break
            else:
                print("Opción inválida")

        # Submenú para el procesador
        while True:
            print("Seleccione el procesador:")
            print("1. AMD Ryzen")
            print("2. Intel Core i5")
            opcion = input("Ingrese el número de la opción: ")
            if opcion == "1":
                self.set_procesador("AMD Ryzen")
                break
            elif opcion == "2":
                self.set_procesador("Intel Core i5")
                break
            else:
                print("Opción inválida")

    def agregar_computador(self):
        computador = {"Serial": self.get_serial(), "Marca": self.get_marca(), "Tamaño": self.get_tamano(),
                      "Precio": self.get_precio(), "Sistema Operativo": self.get_sistema_operativo(),
                      "Procesador": self.get_procesador()}
        self.cantidad_computadores.append(computador)

    def mostrar_computador(self):
        return self.cantidad_computadores