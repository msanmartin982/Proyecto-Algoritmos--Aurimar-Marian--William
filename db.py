'''
Importamos todos los archivos de relevancia que nos ayudaran a ejecutar todas las funciones que definimos en nuestra aplicacion. 
'''
import requests 
from Departamento import Departamento
from Nacionalidad import Nacionalidad
from Obra import Obra, Detalles
from utils import *


'''
Cargamos los departamentos en el sistema y creamos una lista "departamentos" donde estaran almacenados.
La extraemos del link, validamos su respuesta y la transformamos a lo requerido.
'''
def cargar_departamentos():
        departamentos = []
        url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        response = requests.get(url)
        data = response.json()
        for departamento in data["departments"]:
                departamentos.append(Departamento(departamento['departmentId'], departamento['displayName']))
        return departamentos


'''
Obtenemos los ID de los departamentos y modificamos el "url" con "id_departamento" y un agregado para que no tenga error, 
lo que permite que el programa corra. Si la respuesta es positiva se almacena en data la informacion, se intenta obtener el valor 
de "objectIDs".
''' 
def obtener_id_departamento(id_departamento):
        url= (f"https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId={id_departamento}&q=a")
        response=requests.get(url)
        if response.status_code==200:
                data=response.json()
                return data.get("objectIDs")
        else:
                print("Error", response.status_code)   
                return[]


'''
Se realiza la carga de las nacionalidades en el sistema, se crea una lista de nacionalidades vacia, se lee el archivo "txt" y estas se agregan.
'''
def cargar_nacionalidades():
        nacionalidades = []
        with open('nacionalidades.txt', 'r') as file:
                lineas = file.readlines()
        for nacionalidad in lineas:
                nacionalidades.append(Nacionalidad(nacionalidad.strip()))
        return nacionalidades


'''
Realizamos la busqueda del objeto en la API segun el ID ingresado.
'''
def buscar_objeto_por_id(id_objeto):
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id_objeto}"
        response = requests.get(url)
        data = response.json()
        if 'message' in data:
                return
        return Obra(data['objectID'], data['title'], data['artistDisplayName'])


'''
Buscamos la obra segun su nacionalidad.
'''
def buscar_obra_nacionalidad(nacionalidad):
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nacionalidad}"
        response = requests.get(url)
        data = response.json()
        id_obras = data['objectIDs']

        obras_encontradas = []
        if id_obras is not None:

                '''
                Intentamos evitar que la API deje de responder haciendo requests de 10 en 10, igual si se hace muy rapido puede colapsar.
                '''
                if len(id_obras) > 10:
                        limite_sup = 10
                        limite_inf = limite_sup - 10
                        while True:
                                print(f"OBRAS DE LA NACIONALIDAD: {nacionalidad}")
                                for id_obra in id_obras[limite_inf:limite_sup]:
                                        obras_encontradas.append(buscar_objeto_por_id(id_obra))
                                for obra in obras_encontradas:
                                        if obra is not None:
                                                obra.show()
                                continuar = valid_continue("Hay mas obras disponibles, ¿desea seguir viendo? ingresa 'si', de lo contrario 'no': ").lower()
                                if continuar=='si':
                                        limite_sup += 10
                                elif continuar == "no":
                                        break
                else:
                        print(f"OBRAS DE LA NACIONALIDAD: {nacionalidad}")
                        for id_obra in id_obras:
                                obras_encontradas.append(buscar_objeto_por_id(id_obra))
                        for obra in obras_encontradas:
                                if obra is not None:
                                        obra.show()
        else:
                print("No existen obras para la nacionalidad ingresada.")
                return None
        return obras_encontradas


'''
Buscamos obras por nombre del autor.
'''
def buscar_obra_nombre_artista(nombre_artista):
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nombre_artista}"
        response = requests.get(url)
        data = response.json()
        id_obras = data['objectIDs']

        obras_encontradas = []
        if id_obras is not None:
                '''
                Intento evitar que la API deje de responder haciendo requests de 10 en 10, igual si se hace muy rapido puede colapsar.
                '''
                if len(id_obras) > 10:
                        limite_sup = 10
                        limite_inf = limite_sup - 10
                        while True:
                                print(f"OBRAS DEL ARTISTA: {nombre_artista}")
                                for id_obra in id_obras[limite_inf:limite_sup]:
                                        obras_encontradas.append(buscar_objeto_por_id(id_obra))
                                for obra in obras_encontradas:
                                        if obra is not None:
                                                obra.show()
                                continuar = valid_continue("Hay mas obras disponibles, ¿desea seguir viendo? ingresa 'si', de lo contrario 'no': ").lower()
                                if continuar=='si':
                                        limite_sup += 10
                                elif continuar == "no":
                                        break
                else:
                        print(f"OBRAS DEL ARTISTA: {nombre_artista}")
                        for id_obra in id_obras:
                                obras_encontradas.append(buscar_objeto_por_id(id_obra))
                        for obra in obras_encontradas:
                                if obra is not None:
                                        obra.show()
        else:
                print("No existen obras para el autor ingresado.")
                return None
        return obras_encontradas


'''
Obtenemos los detalles de las obras.
'''
def obtener_detalles_obras(obj_id):
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}"
        response = requests.get(url)
        if response.status_code == 200:
                data = response.json()
                obra = Detalles(id=data.get("objectID"),titulo=data.get("title"),nombre_autor=data.get("artistDisplayName"),nacionalidad=data.get("artistNationality"),fecha_nacimiento=data.get("artistBeginDate"),fecha_muerte=data.get("artistEndDate"),clasificacion=data.get("classification"),año_creacion=data.get("objectDate"),imagen=data.get("primaryImage"))
                return obra
        else:
                print("Error", response.status_code)