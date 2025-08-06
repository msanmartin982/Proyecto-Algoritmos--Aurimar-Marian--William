import requests 
from Departamentos import Departamento
from Obras import Obras,Detalles


def cargar_departamentos():
        departamentos = []
        url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        response = requests.get(url)
        data = response.json()
        for departamento in data["departments"]:
                departamentos.append(Departamento(departamento['departmentId'], departamento['displayName']))
        return departamentos

def obtener_id_departamento(id_departamento):

        url= (f"https://collectionapi.metmuseum.org/public/collection/v1/bjects?departmentIds={id_departamento}")
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
        response.raise_for_status()
        data=response.json()

        obras=Detalles(id=data.get("objectID"),titulo=data.get("title"),autor=data.get("artistDisplayName"),nacionalidad=data.get("artistNationality"),nacimiento=data.get("artistBeginDate"),muerte=data.get("artistEndDate"),tipo=data.get("classification"),creacion=data.get("objectDate"),imagen=data.get("primaryImage"))
        return obras
