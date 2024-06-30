import json
import vehiculos
import clientes
import os
import sys
from datetime import datetime

def registrar_compras():

    with open("transacciones.json", "rt", encoding="utf-8" ) as archivo:
        transacciones = json.load(archivo)

    quiere_salir= False
    while quiere_salir == False:

        id_veh_nuevo = None
        while id_veh_nuevo is None:
            patente = input('Ingrese la patente del vehiculo que desea realizar la compra: ')
            with open("vehiculos.json", "rt", encoding="utf-8") as archivo_vehiculos:
                vehiculos = json.load(archivo_vehiculos)
            for vehiculo in vehiculos:
                if vehiculo['patente'] != patente:
                    id_veh_nuevo = vehiculo["id_vehiculo"]
                    break

            if id_veh_nuevo is None:
                print("Vehículo no encontrado.")
                continue

        id_cliente_nuevo= None
        while id_cliente_nuevo is None:
            cliente_input = input('Ingrese el documento del cliente de quien desea realizar la Compra: ')
            with open("clientes.json", "rt", encoding="utf-8") as archivo_clientes:
                clientes = json.load(archivo_clientes)
            for cliente in clientes:
                if cliente['documento'] == cliente_input:
                    id_cliente_nuevo = cliente["id_cliente"]
                    break
            if id_cliente_nuevo is None:
                print("Cliente no encontrado.")
                continue
       
        #id_transacciones
        id_transacciones_nuevo= transacciones[-1]["id_transaccion"] + 1
        
        # No es necesario poner el tipo de transaccion se sobreentiende en el menu, tampoco la fecha,
        # para evitar que el usuario tipee cualquier cosa
        # tipo_transaccion= input ("Ingrese la transacción: ")
        # fecha= input ("Ingrese fecha de transacción: ")
        monto= input ("Ingrese monto de transacción: ")
        observaciones= input ("Ingrese observaciones: ")
    

        transaccion = {
            'id_vehiculo': id_veh_nuevo,
            "id_cliente":id_cliente_nuevo,
            "id_transaccion":id_transacciones_nuevo ,
            "tipo_transaccion": "Compra", 
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "monto": monto,
            "Observaciones": observaciones,
        }

        opcion= input ("Escriba Si si quiere salir, o escriba SEGUIR: ")
        opcion.lower()
        if opcion== "si":
            print("Terminó la carga de compras")
        quiere_salir= True


        transacciones.append(transaccion)

    with open("transacciones.json", "wt", encoding="utf-8" ) as archivo:
        json.dump(transacciones, archivo, indent=4)

def registrar_ventas():
    with open("transacciones.json", "rt", encoding="utf-8" ) as archivo:
        transacciones = json.load(archivo)

    quiere_salir= False
    while quiere_salir == False:

        id_veh_nuevo = None
        while id_veh_nuevo is None:
            patente = input('Ingrese la patente del vehiculo que desea vender: ')
            with open("vehiculos.json", "rt", encoding="utf-8") as archivo_vehiculos:
                vehiculos = json.load(archivo_vehiculos)
            for vehiculo in vehiculos:
                if vehiculo['patente'] == patente:
                    id_veh_nuevo = vehiculo["id_vehiculo"]
                    break

            if id_veh_nuevo is None:
                print("Vehículo no encontrado.")
                continue

        id_cliente_nuevo= None
        while id_cliente_nuevo is None:
            clienteInput = input('Ingrese el documento del cliente de quien desea realizar la Venta: ')
            with open("clientes.json", "rt", encoding="utf-8") as archivo_clientes:
                clientes = json.load(archivo_clientes)
            for cliente in clientes:
                if cliente['documento'] == clienteInput:
                    id_cliente_nuevo = cliente["id_cliente"]
                    break
            if id_cliente_nuevo is None:
                print("Cliente no encontrado.")
                continue
       
        #id_transacciones
        id_transacciones_nuevo= transacciones[-1]["id_transaccion"] + 1
        
        
        # tipo_transacion= input ("Ingrese la transacción: ")
        # fecha= input ("Ingrese fecha de transacción: ")
        monto= input ("Ingrese monto de transacción: ")
        observaciones= input ("Ingrese observaciones: ")
    

        transaccion = {
            'id_vehiculo': id_veh_nuevo,
            "id_cliente":id_cliente_nuevo,
            "id_transaccion":id_transacciones_nuevo ,
            "tipo_transaccion": "Venta", 
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "monto": monto,
            "Observaciones": observaciones,
        }

        opcion= input ("Escriba Si si quiere salir, o esciba SEGUIR: ")
        opcion.lower()
        if opcion== "Si":
            print("Terminó la carga de ventas")
        
        quiere_salir= True


        transacciones.append(transaccion)

    with open("transacciones.json", "wt", encoding="utf-8" ) as archivo:
        json.dump(transacciones, archivo, indent=4)



def listar_compras():
    with open("transacciones.json", "rt", encoding="utf-8" ) as archivo:
        transacciones = json.load(archivo)
    id_cliente = int(input("Ingrese el ID del cliente (o 0 para todos): "))
    id_vehiculo = int(input("Ingrese el ID del vehículo (o 0 para todos): "))
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD, o deje en blanco para todas): ")
    fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD, o deje en blanco para todas): ")

    total_monto = 0
    for transaccion in transacciones:
        if transaccion['tipo_transaccion'] == "Compra":
            if (id_cliente == 0 or transaccion['id_cliente'] == id_cliente) and \
               (id_vehiculo == 0 or transaccion['id_vehiculo'] == id_vehiculo) and \
               (not fecha_inicio or datetime.strptime(transaccion['fecha'], "%Y-%m-%d") >= datetime.strptime(fecha_inicio, "%Y-%m-%d")) and \
               (not fecha_fin or datetime.strptime(transaccion['fecha'], "%Y-%m-%d") <= datetime.strptime(fecha_fin, "%Y-%m-%d")):
                print(f'\nID de la transacción: {transaccion['id_transaccion']}, \nTipo de transacción: {transaccion["tipo_transaccion"]}, \nFecha: {transaccion['fecha']}, \nMonto: {transaccion['monto']}, \nObservaciones: {transaccion["Observaciones"]}')
                total_monto += float(transaccion['monto'])
    
    print(f"Total Compras: {total_monto}")

def listar_ventas():
    with open("transacciones.json", "rt", encoding="utf-8" ) as archivo:
        transacciones = json.load(archivo)
    id_cliente = int(input("Ingrese el ID del cliente (o 0 para todos): "))
    id_vehiculo = int(input("Ingrese el ID del vehículo (o 0 para todos): "))
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD, o deje en blanco para todas): ")
    fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD, o deje en blanco para todas): ")

    total_monto = 0
    for transaccion in transacciones:
        if transaccion['tipo_transaccion'] == "Venta":
            if (id_cliente == 0 or transaccion['id_cliente'] == id_cliente) and \
               (id_vehiculo == 0 or transaccion['id_vehiculo'] == id_vehiculo) and \
               (not fecha_inicio or datetime.strptime(transaccion['fecha'], "%Y-%m-%d") >= datetime.strptime(fecha_inicio, "%Y-%m-%d")) and \
               (not fecha_fin or datetime.strptime(transaccion['fecha'], "%Y-%m-%d") <= datetime.strptime(fecha_fin, "%Y-%m-%d")):
                print(f'\nID de la transacción: {transaccion['id_transaccion']}, \nTipo de transacción: {transaccion["tipo_transaccion"]}, \nFecha: {transaccion['fecha']}, \nMonto: {transaccion['monto']}, \nObservaciones: {transaccion["Observaciones"]}')
                total_monto += float(transaccion['monto'])
    
    print(f"Total Ventas: {total_monto}")





    