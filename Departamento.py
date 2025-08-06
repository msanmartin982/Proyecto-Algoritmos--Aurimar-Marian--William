class Departamento:
        def __init__(self, id, nombre_departamento):
                self.id = id
                self.nombre_departamento = nombre_departamento

        def show(self):
                print(f"ID de Departamento: {self.id}")
                print(f"Nombre de Departamento: {self.nombre_departamento}")