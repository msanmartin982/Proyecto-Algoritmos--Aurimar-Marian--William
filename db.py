import requests 
from Departamento import Departamento
from Nacionalidad import Nacionalidad
from Obra import Obra, Detalles
from utils import *

#Carga los departamentos en el sistema
def cargar_departamentos():
        departamentos = []
        url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        response = requests.get(url)
        data = response.json()
        for departamento in data["departments"]:
                departamentos.append(Departamento(departamento['departmentId'], departamento['displayName']))
        return departamentos

def obtener_id_departamento(id_departamento):

        url= (f"https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId={id_departamento}&q=a")
        try:
                response=requests.get(url)
                response.raise_for_status()
                data=response.json()
                return data.get(("objectIDs"),[])
        except requests.exceptions.RequestException as e:
                print(f"Error al obtener IDs de objectos por departamento: {e}")
        return[]

def obtener_detalles_obras(obj_id):
        url= f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}"
        response=requests.get(url)
        if response.status_code==200:
                data=response.json()
                obras=Detalles(id=data.get("objectID"),titulo=data.get("title"),autor=data.get("artistDisplayName"),nacionalidad=data.get("artistNationality"),nacimiento=data.get("artistBeginDate"),muerte=data.get("artistEndDate"),tipo=data.get("classification"),creacion=data.get("objectDate"),imagen=data.get("primaryImage"))
                return obras
        else:
                print("Error", response.status_code)

# Carga las nacionalidades en el sistema
def cargar_nacionalidades():
        nacionalidades = []
        with open('nacionalidades.txt', 'r') as file:
                lineas = file.readlines()
        for nacionalidad in lineas:
                nacionalidades.append(Nacionalidad(nacionalidad.strip()))
        return nacionalidades

# Busca objeto en la API segun el ID
def buscar_objeto_por_id(id_objeto):
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id_objeto}"
        response = requests.get(url)
        data = response.json()
        return Obra(data['objectID'], data['title'], data['artistDisplayName'])

# Busca obra segun su nacionalidad
def buscar_obra_nacionalidad(nacionalidad):
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nacionalidad}"
        response = requests.get(url)
        data = response.json()
        id_obras = data['objectIDs']

        obras_encontradas = []
        if id_obras is not None:

                #Intento evitar que la API deje de responder haciendo requests de 10 en 10, igual si se hace muy rapido puede colapsar.
                if len(id_obras) > 10:
                        limite_sup = 10
                        limite_inf = limite_sup - 10
                        while True:
                                print(f"OBRAS DE LA NACIONALIDAD: {nacionalidad}")
                                for id_obra in id_obras[limite_inf:limite_sup]:
                                        obras_encontradas.append(buscar_objeto_por_id(id_obra))
                                for obra in obras_encontradas:
                                        obra.show()
                                continuar = valid_continue("Hay mas obras disponibles, ¿desea seguir viendo? (y/n):")
                                if continuar=='y':
                                        limite_sup += 10
                                elif continuar == "n":
                                        break
                else:
                        print(f"OBRAS DE LA NACIONALIDAD: {nacionalidad}")
                        for id_obra in id_obras:
                                obras_encontradas.append(buscar_objeto_por_id(id_obra))
                        for obra in obras_encontradas:
                                obra.show()
        else:
                print("No existen obras para la nacionalidad ingresada.")
                return None
        return obras_encontradas