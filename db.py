import requests 
from Departamentos import Departamento


def cargar_departamentos():
        departamentos = []
        url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        response = requests.get(url)
        data = response.json()
        for departamento in data["departments"]:
                departamentos.append(Departamento(departamento['departmentId'], departamento['displayName']))
        return departamentos
