class Ingenieria:
    def __init__(self, cedula="", nombre="", apellido="", telefono="", semestre=0, promedio=0.0, serial=""):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._telefono = telefono
        self._semestre = semestre
        self._promedio = promedio
        self._serial = serial
        self.cantidad = []

    # Metodos gett
    def get_cedula(self):
        return self._cedula

    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido

    def get_telefono(self):
        return self._telefono

    def get_semestre(self):
        return self._semestre

    def get_promedio(self):
        return self._promedio

    def get_serial(self):
        return self._serial

    # Metodos Sett
    def set_cedula(self, cedula):
        self._cedula = cedula

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_apellido(self, apellido):
        self._apellido = apellido

    def set_telefono(self, telefono):
        self._telefono = telefono

    def set_semestre(self, semestre):
        self._semestre = semestre

    def set_promedio(self, promedio):
        self._promedio = promedio

    def set_serial(self, serial):
        self._serial = serial

    def Ingresar_Compartidos(self):
        # validacion para la cedula
        while True:
            cc = input("Digite la cedula del estudiante: ")
            if cc.isnumeric():
                self.set_cedula(cc)
                break
            else:
                print("La cedula deben ser numeros")

        # validacion para el nombre
        while True:
            name = input("Digite el nombre del estudiante: ")
            if name.isalpha():
                self.set_nombre(name)
                break
            else:
                print("Solo debe contener letras")

        # Validacion para el apellido
        while True:
            Last_Name = input("Digite el apeliido del estudiante: ")
            if Last_Name.isalpha():
                self.set_apellido(Last_Name)
                break
            else:
                print("Solo debe contener letras")

        # validacion para el telefono
        while True:
            number = input("Digite el telefono del estudiante: ")
            if number.isalnum():
                self.set_telefono(number)
                break
            else:
                print("El telefono no debe tener caracteres especiales ni espacios")

    def Ingresar_Solos(self):
        # validacion para numero de semestre
        while True:
            try:
                n_semestre = int(input("Digite el numero del semestre: "))
                if n_semestre < 1 or n_semestre > 10:
                    print("Error digite un numero de senestre valido")
                else:
                    self.set_semestre(n_semestre)
                    break
            except ValueError:
                print("Dato invalido debe ser un numero")

        # validacion para numero de promedio
        while True:
            try:
                prom = float(input("Digite el promedio acumulado: "))
                if prom < 0 or prom > 10:
                    print("Error digite un numero de senestre valido")
                else:
                    self.set_promedio(prom)
                    break
            except ValueError:
                print("Dato invalido debe ser un numero")

        # validacion para el serial
        while True:
            serial = input("Digite el serial del estudiante: ")
            if serial.isalnum():
                self.set_serial(serial)
                break
            else:
                print("Solo debe contener letras y numeros")

    def Agregar(self):
        Estud_Ingenieria = {"Cedula": self.get_cedula(), "Nombre": self.get_nombre(), "Apellido": self.get_apellido(),
                            "Telefono": self.get_telefono(), "Semestre": self.get_semestre(),
                            "Promedio": self.get_promedio(), "Serial": self.get_serial()}
        self.cantidad.append(Estud_Ingenieria)

    def mostrar(self):
        return self.cantidad
