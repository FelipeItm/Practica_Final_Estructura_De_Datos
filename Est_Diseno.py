from Est_Ingen import Ingenieria

class Diseno(Ingenieria):
    def __init__(self, cedula="", nombre="", apellido="", telefono="", serial="", modalidad="", materias=0, codigo=0):
        super().__init__(cedula, nombre, apellido, telefono)
        self._modalidad = modalidad
        self._materias = materias
        self._codigo = codigo

    def get_modalidad(self):
        return self._modalidad

    def get_materias(self):
        return self._materias

    def get_codigo(self):
        return self._codigo

    def set_modalidad(self, modalidad):
        self._modalidad = modalidad

    def set_materias(self, materias):
        self._materias = materias

    def set_codigo(self, codigo):
        self._codigo = codigo

    def Ingresar_Diseno(self):
        while True:
            metodo = input("Digite el metodo de estudio del estudiante: ")
            if metodo.isalpha():
                if metodo.lower() == "virtual" or metodo.lower() == "presencial":
                    self.set_modalidad(metodo)
                    break
                else:
                    print("Error, palabra incorrecta")
            else:
                print("Los caracteres solo deben ser letras")

        while True:
            try:
                asignaturas = int(input("Digite el numero de asignaturas que esta viendo: "))
                if asignaturas < 1 or asignaturas > 10:
                    print("Dato erroneo, revisar numero de asignaturas")
                else:
                    self.set_materias(asignaturas)
                    break
            except ValueError:
                print("Error el dato ingresado debe ser un numero entero")

        while True:
            prestamo = input("Digite el serial: ")
            if prestamo.isnumeric():
                if len(prestamo) > 8:
                    print("Error, serial demaciado largo maximo numero de caracteres permitidos 8")
                else:
                    self.set_codigo(prestamo)
                    break
            else:
                print("Error, el codigo solo deben ser numeros")

        Est_Diseno = {"Cedula": self.get_cedula(), "Nombre": self.get_nombre(), "Apellido": self.get_apellido(),
                      "Telefono": self.get_telefono(), "Modalidad": self.get_modalidad(),
                      "Cantidad de materias": self.get_materias(), "Serial": self.get_codigo()}
        self.cantidad.append(Est_Diseno)

    def mostrar(self):
        return super().mostrar()
