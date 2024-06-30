import json
import sys
import os


def listar_vehiculos():
    archivos_vehiculos= open("vehiculos.json", "rt", encoding="utf-8")
    vehiculos= archivos_vehiculos.read()
    print("La lista: ", vehiculos)


def crear_vehiculos ():
    
    with open("vehiculos.json", "rt", encoding="utf-8" ) as archivo:
        vehiculos = json.load(archivo)

    print(f"La cantidad actual de vehiculos en Automotores Milenio es: {len(vehiculos)}")   
    
    quiere_salir= False

    while quiere_salir == False:
        id_veh_nuevo= vehiculos[-1]["id_vehiculo"] + 1
        patente= input ("Ingrese patente: ")
        marca=  input("Ingrese marca: ")
        modelo= input("Ingrese el modelo: ")
        tipo= input("Ingrese una opcion sedan, hatchback, suv, pick up, otros:  ")
        anio= int(input ("Ingrese año: "))
        kilometraje= int(input("Ingrese kilometraje: "))
        precio_de_compra= int(input ("Ingrese precio pagado:$ "))
        precio_de_venta= int(input ("Ingrese precio de venta:$ "))
        estado= input ("Ingrese el estado del vehiculo: disponible, reservado, vendido: ")    

        vehiculo = {
            'id_vehiculo': id_veh_nuevo,
            "patente": patente,
            'marca': marca,
            "modelo": modelo,
            "tipo": tipo,
            "año": anio,
            "kilometraje": kilometraje,
            "precio_de_compra": precio_de_compra,
            "precio_de_venta": precio_de_venta,
            "estado": estado
        }

        vehiculos.append(vehiculo)

        opcion= input ("Escriba \"si\" si quiere salir, o escriba SEGUIR: ")
        opcion.lower()
        if opcion== "si":
            print("Terminó la carga de vehículos")
            quiere_salir= True

    with open("vehiculos.json", "wt", encoding="utf-8" ) as archivo:
        json.dump(vehiculos, archivo, indent=4)


def editar_vehiculos():
    with open("vehiculos.json", "rt", encoding="utf-8" ) as archivo:
        vehiculos = json.load(archivo)

    print(f"La lista actual de vehiculos es: {vehiculos} ")
    

    print(f"La lista actual de vehiculos es: ")
    for vehiculo in vehiculos:
        print(f'Id: {vehiculo['id_vehiculo']}, Nombre: {vehiculo['marca']}, DNI {vehiculo['modelo']}')

    patente_a_buscar = input('Ingrese la patente: ')
    vehiculo_encontrado = None
    for vehiculo in vehiculos:
        if vehiculo['patente'] == patente_a_buscar:
            vehiculo_encontrado = vehiculo
            break
    if vehiculo_encontrado:
        vehiculo_encontrado['kilometraje'] = input('Ingrese el nuevo kilometraje: ')
        vehiculo_encontrado['precio_de_compra'] = input('Ingrese el precio de compra: ')
        vehiculo_encontrado['precio_de_venta'] = input('Ingrese el precio de venta: ')
        vehiculo_encontrado['estado'] = input('Ingrese el estado de la unidad: ')
    else:
        print(f'No se encontro el vehiculo con la patente {patente_a_buscar}')
    with open("vehiculos.json", "wt", encoding="utf-8" ) as archivo:
        json.dump(vehiculos, archivo, indent=4)
    print("Vehiculo editado")
    

def borrar_vehiculos():
    with open("vehiculos.json", "rt", encoding="utf-8" ) as archivo:
        vehiculos = json.load(archivo)

    patente_vehiculo= input("Ingrese la patente del vehiculo a borrar, Patente: ")
    
    for vehiculo in vehiculos:
        if vehiculo["patente"] == patente_vehiculo:
            vehiculos.remove (vehiculo)
    print (f"El {vehiculo["patente"]} ha sido borrado de su lista")
    with open("vehiculos.json", "wt", encoding="utf-8" ) as archivo:
        json.dump(vehiculos, archivo, indent=4)
        # print (vehiculos)


def buscar_vehiculos():
    with open("vehiculos.json", "rt", encoding="utf-8" ) as archivo:
        vehiculos = json.load(archivo)

    criterio = input("Ingrese criterio de búsqueda (patente, marca, modelo, precio): ").lower()
    resultado = [v for v in vehiculos if criterio in v['patente'].lower() or criterio in v['marca'].lower() or criterio in v['modelo'].lower() or criterio in str(v['precio_de_compra']) or criterio in str(v['precio_de_venta'])]

    if resultado:
        print("\nResultados de la búsqueda:")
        print(f'Patente: {resultado[0]["patente"]}')
        print(f'Marca: {resultado[0]["marca"]}')
        print(f'Modelo: {resultado[0]["modelo"]}')
        print(f'Tipo: {resultado[0]["tipo"]}')
        print(f'Año: {resultado[0]["año"]}')
        print(f'Precio de compra: {resultado[0]["precio_de_compra"]}')
        print(f'Precio de venta: {resultado[0]["precio_de_venta"]}')
        print(f'Estado: {resultado[0]["estado"]}')
    else:
        print("\nNo se encontraron resultados.")








#listados de busqueda:
'''def buscar_vehiculos_por_patente ():
     with open("vehiculos.json", "rt", encoding="utf-8" ) as archivo:
        vehiculos = json.load(archivo) 
     vehiculos_a_buscar= input("ingrese el patente del vehiculo a buscar: ")
     vehiculo_encontrado= False
     for vehiculo in vehiculos:
         if vehiculos["patente"] == vehiculos_a_buscar:
             vehiculo_encontrado= True
             print (vehiculo_encontrado)
     if vehiculos_a_buscar==False:
         print ("Vehiculo no encontrado")

#listado de busqueda: marca
def buscar_marcas ():
    with open("vehiculos.json", "rt", encoding="utf-8" ) as archivo:
        vehiculos = json.load(archivo) 
    marcas_a_buscar= input("ingrese la MARCA del vehiculo a buscar: ")
    marcas_encontrada= False
    for marcas in vehiculos:
        if vehiculos["marcas"] == marcas_a_buscar:
             marcas_encontrada= True
             print (marcas_encontrada)
    if marcas_encontrada==False:
         print ("Vehiculo no encontrada")

#listado de busqueda: modelo
def buscar_modelos ():
    with open("vehiculos.json", "rt", encoding="utf-8" ) as archivo:
        vehiculos = json.load(archivo)  
    modelos_a_buscar= input("ingrese el modelo del vehiculo a buscar: ")
    modelo_encontrado= False
    for modelos in vehiculos:
        if vehiculos["modelo"] == modelos_a_buscar:
             modelo_encontrado= True
             print (modelo_encontrado)
    if modelo_encontrado==False:
         print ("Vehiculo no encontrada")

#Listado por precio:


'''