import json
import sys
import os

def crear_clientes ():
    with open("clientes.json", "rt", encoding="utf-8" ) as archivo:
        clientes = json.load(archivo)

    quiere_cargar_clientes= False

    while quiere_cargar_clientes == False:
        id_cliente_nuevo= clientes[-1]["id_cliente"] + 1
        nombre= input("Ingrese Nombre: ")
        documento=  input("Ingrese DNI: ")
        apellido= input ("Ingrese Apellido: ")
        direccion= input("Ingrese Dirección:  ")
        correo_electronico= input ("Ingrese Correo electrónico: ")
        telefono= input("Ingrese Teléfono: ")
        
        
        cliente = {
            "id_cliente": id_cliente_nuevo,
            "nombre": nombre,
            "documento":  documento,
            "apellido": apellido,
            "direccion": direccion,
            "correo_electronico": correo_electronico,
            "telefono": telefono
        }

        clientes.append(cliente)

        opcion= input ("Escriba \"si\" si quiere salir, o escriba SEGUIR: ")
        opcion.lower()
        if opcion== "si":
            print("Termino la carga de clientes")
            quiere_cargar_clientes= True

    with open("clientes.json", "wt", encoding="utf-8" ) as archivo:
        json.dump(clientes, archivo, indent=4)


def editar_clientes():
    with open("clientes.json", "rt", encoding="utf-8" ) as archivo:
        clientes = json.load(archivo)
    
    
    print(f"La lista actual de clientes es: ")
    for cliente in clientes:
        print(f'Id: {cliente['id_cliente']}, Nombre: {cliente['nombre']}, DNI {cliente['documento']}')


    cliente_a_buscar = input('Ingrese el documento del cliente que desee editar: ')
    cliente_encontrado = None
    for cliente in clientes:
        if cliente['documento'] == cliente_a_buscar:
            cliente_encontrado = cliente
            break

    if cliente_encontrado:
        cliente_encontrado['direccion'] = input('Ingrese la nueva direccion: ')
        cliente_encontrado['telefono'] = input('Ingrese nuevo teléfono de contacto: ')
        cliente_encontrado['correo_electronico'] = input('Ingrese el correo electrónico: ')
    else:
        print("No se encontro el cliente")
    with open("clientes.json", "wt", encoding="utf-8" ) as archivo:
        json.dump(clientes, archivo, indent=4)
    print('Datos actualizados')


def eliminar_clientes():
    with open("clientes.json", "rt", encoding="utf-8" ) as archivo:
        clientes = json.load(archivo)

    docu_cliente= input("Ingrese el documento del cliente a borrar, DNI: ")
    
    for cliente in clientes:
        if cliente["documento"] == docu_cliente:
            clientes.remove (cliente)
    print (f"El {cliente["documento"]} ha sido borrado de su lista")
    with open("clientes.json", "wt", encoding="utf-8" ) as archivo:
        json.dump(clientes, archivo, indent=4)
        # print (clientes)


def buscar_clientes():
    with open("clientes.json", "rt", encoding="utf-8" ) as archivo:
        clientes = json.load(archivo)

    criterio = input("Ingrese criterio de búsqueda (documento, apellido, nombre): ").lower()
    resultado = [c for c in clientes if criterio in c['documento'].lower() or criterio in c['apellido'].lower() or criterio in c['nombre'].lower()]
    
    if resultado:
        print("\nResultados de la búsqueda:")
        print(f'Nombre completo: {resultado[0]['nombre']} {resultado[0]["apellido"]}')
        print(f'DNI: {resultado[0]["documento"]}')
        print(f'Telefono: {resultado[0]["telefono"]}')
        print(f'Dirección: {resultado[0]["direccion"]}')
        print(f'Correo: {resultado[0]["correo_electronico"]}')
    else:
        print("\nNo se encontraron resultados.")