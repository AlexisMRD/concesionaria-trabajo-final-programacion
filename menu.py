
import clientes
import vehiculos
import transacciones

def main():
    while True:
        print("\nMenu Principal")
        print("1. Gestionar Clientes")
        print("2. Gestionar Vehículos")
        print("3. Gestionar Transacciones")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_clientes()
        elif opcion == "2":
            gestionar_vehiculos()
        elif opcion == "3":
            gestionar_transacciones()
        elif opcion == "4":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def gestionar_clientes():
    while True:
        print("\nGestionar Clientes")
        print("1. Crear Cliente")
        print("2. Editar Cliente")
        print("3. Eliminar Cliente")
        print("4. Buscar Clientes")
        print("5. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clientes.crear_clientes()
        elif opcion == "2":
            clientes.editar_clientes()
        elif opcion == "3":
            clientes.eliminar_clientes()
        elif opcion == "4":
            clientes.buscar_clientes()     
        elif opcion == "5":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def gestionar_vehiculos():
    while True:
        print("\nGestionar Vehículos")
        print("1. Crear Vehículo")
        print("2. Editar Vehículo")
        print("3. Eliminar Vehículo")
        print("4. Buscar Vehículo")
        print("5. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            vehiculos.crear_vehiculos()
        elif opcion == "2":
            vehiculos.editar_vehiculos()
        elif opcion == "3":
            vehiculos.borrar_vehiculos()
        elif opcion == "4":
            vehiculos.buscar_vehiculos()      
        elif opcion == "5":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def gestionar_transacciones():
    while True:
        print("\nGestionar Transacciones")
        print("1. Registrar Compra")
        print("2. Registrar Venta")
        print("3. Listar Compras")
        print("4. Listar Ventas")
        print("5. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            transacciones.registrar_compras()
        elif opcion == "2":
            transacciones.registrar_ventas()
        elif opcion == "3":
            transacciones.listar_compras()     
        elif opcion == "4":
            transacciones.listar_ventas()       
        elif opcion == "5":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
