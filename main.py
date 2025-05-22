from Est_Ingen import Ingenieria
from Est_Diseno import Diseno
from TabletaGrafica import TabletaGrafica
from ComputadorPortatil import ComputadorPortatil

if __name__ == "__main__":
    ingenieros = []
    disenadores = []
    tabletas = []
    computadores = []

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. ESTUDIANTES DE INGENIERIA")
        print("2. ESTUDIANTES DE DISEÑO")
        print("3. IMPRIMIR INVENTARIO TOTAL")
        print("4. SALIR DEL PROGRAMA")

        opcion_principal = input("Seleccione una opción: ")

        if opcion_principal == "1":
            while True:
                print("\n--- ESTUDIANTES DE INGENIERIA ---")
                print("1.1 Registrar préstamo de equipo")
                print("1.2 Modificar préstamo de equipo")
                print("1.3 Devolución de equipo")
                print("1.4 Buscar equipo")
                print("1.5 Volver al menú principal")

                opcion_ingenieria = input("Seleccione una opción: ")

                if opcion_ingenieria == "1.1":
                    estudiante = Ingenieria()
                    estudiante.Ingresar_Compartidos()
                    estudiante.Ingresar_Solos()
                    estudiante.Agregar()
                    ingenieros.append(estudiante)
                    computador = ComputadorPortatil()
                    computador.ingresar_computador()
                    computador.agregar_computador()
                    computadores.append(computador)
                    print("Préstamo de equipo registrado para estudiante de ingeniería.")

                elif opcion_ingenieria == "1.2":
                    cedula_o_serial = input("Ingrese la cédula o el serial del equipo a modificar: ")
                    encontrado = False
                    for estudiante in ingenieros:
                        if estudiante.get_cedula() == cedula_o_serial or estudiante.get_serial() == cedula_o_serial:
                            print("Estudiante encontrado. Ingrese los nuevos datos:")
                            estudiante.Ingresar_Compartidos()
                            estudiante.Ingresar_Solos()
                            encontrado = True
                            break
                    if not encontrado:
                        print("No se encontró ningún estudiante con esa cédula o serial.")

                elif opcion_ingenieria == "1.3":
                    cedula_o_serial = input("Ingrese la cédula o el serial del equipo a devolver: ")
                    for estudiante in ingenieros:
                        if estudiante.get_cedula() == cedula_o_serial or estudiante.get_serial() == cedula_o_serial:
                            ingenieros.remove(estudiante)
                            print("Préstamo de equipo devuelto y registro eliminado.")
                            break
                    else:
                        print("No se encontró ningún estudiante con esa cédula o serial.")

                elif opcion_ingenieria == "1.4":
                    cedula_o_serial = input("Ingrese la cédula o el serial del equipo a buscar: ")
                    encontrado = False
                    for estudiante in ingenieros:
                        if estudiante.get_cedula() == cedula_o_serial or estudiante.get_serial() == cedula_o_serial:
                            print("Datos del estudiante:")
                            print(estudiante.mostrar())
                            encontrado = True
                            break
                    if not encontrado:
                        print("No se encontró ningún estudiante con esa cédula o serial.")

                elif opcion_ingenieria == "1.5":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")

        elif opcion_principal == "2":
            while True:
                print("\n--- ESTUDIANTES DE DISEÑO ---")
                print("2.1 Registrar préstamo de equipo")
                print("2.2 Modificar préstamo de equipo")
                print("2.3 Devolución de equipo")
                print("2.4 Buscar equipo")
                print("2.5 Volver al menú principal")

                opcion_diseno = input("Seleccione una opción: ")

                if opcion_diseno == "2.1":
                    estudiante = Diseno()
                    estudiante.Ingresar_Compartidos()
                    estudiante.Ingresar_Diseno()
                    estudiante.Agregar()
                    disenadores.append(estudiante)
                    tableta = TabletaGrafica()
                    tableta.ingresar_tableta()
                    tableta.agregar_tableta()
                    tabletas.append(tableta)
                    print("Préstamo de equipo registrado para estudiante de diseño.")

                elif opcion_diseno == "2.2":
                    cedula_o_serial = input("Ingrese la cédula o el serial del equipo a modificar: ")
                    encontrado = False
                    for estudiante in disenadores:
                        if estudiante.get_cedula() == cedula_o_serial or estudiante.get_codigo() == cedula_o_serial:
                            print("Estudiante encontrado. Ingrese los nuevos datos:")
                            estudiante.Ingresar_Compartidos()
                            estudiante.Ingresar_Diseno()
                            encontrado = True
                            break
                    if not encontrado:
                        print("No se encontró ningún estudiante con esa cédula o serial.")

                elif opcion_diseno == "2.3":
                    cedula_o_serial = input("Ingrese la cédula o el serial del equipo a devolver: ")
                    for estudiante in disenadores:
                        if estudiante.get_cedula() == cedula_o_serial or estudiante.get_codigo() == cedula_o_serial:
                            disenadores.remove(estudiante)
                            print("Préstamo de equipo devuelto y registro eliminado.")
                            break
                    else:
                        print("No se encontró ningún estudiante con esa cédula o serial.")

                elif opcion_diseno == "2.4":
                    cedula_o_serial = input("Ingrese la cédula o el serial del equipo a buscar: ")
                    encontrado = False
                    for estudiante in disenadores:
                        if estudiante.get_cedula() == cedula_o_serial or estudiante.get_codigo() == cedula_o_serial:
                            print("Datos del estudiante:")
                            print(estudiante.mostrar_diseno())
                            encontrado = True
                            break
                    if not encontrado:
                        print("No se encontró ningún estudiante con esa cédula o serial.")

                elif opcion_diseno == "2.5":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")

        elif opcion_principal == "3":
            print("\n--- INVENTARIO TOTAL ---")
            print("\n--- ESTUDIANTES DE INGENIERIA ---")
            for estudiante in ingenieros:
                print(estudiante.mostrar())
            print("\n--- ESTUDIANTES DE DISEÑO ---")
            for estudiante in disenadores:
                print(estudiante.mostrar_diseno())
            print("\n--- COMPUTADORES PORTATILES ---")
            for computador in computadores:
                print(computador.mostrar_computador())
            print("\n--- TABLETAS GRAFICAS ---")
            for tableta in tabletas:
                print(tableta.mostrar_tableta())

        elif opcion_principal == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")