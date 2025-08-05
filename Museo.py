from db import *

class Museo:
    def __init__(self):
        self.departamentos = []

    def start(self):
        self.departamentos = cargar_departamentos()
        print(self.departamentos)


        while True:
            
            opcion=input('''
        Bienvenido al catalogo 
                de Arte 
-----------del Museo MetroArt---------------                         
Selecciona una opcion                        
1-Busqueda de obras
2-Mostrar detalles de obras por ID conocido
3-Salir
                              
------------> ''')
            
            if opcion=="1":
                while True:
                    menu= input("""
                Ingresa la opcion que deseas:
                1-Ver lista de obras por departamento
                2-Ver lista de obras por nacionalidad de Autor
                3-ver lista de obras por nombre de autor
                4-Volver al menu inicial
                ----> """)
            
                    if menu== "1":
                        self.obtener_departamentos()
                        pass
                    
                    elif menu == "2":
                        pass
                
                    elif menu == "3":
                        pass
                
                    elif menu == "4":
                        break
                
            else:
                print(f'Opcion invalida, por favor ingresa una de las opciones disponibles')
                break
                

            

#Iniciamos el desarrollo de la opcion de obtener los departamentos
    def obtener_departamentos(self):
        self.departamentos = cargar_departamentos()

        if not self.departamentos:
            print("Error al cargar los departamentos")
            return
        
        print("Departamentos del Museo:")
        for dep in self.departamentos:
            dep.show()

        
        while True:
            try:
                seleccion_id=int(input("Ingreesa el ID del departamento que deseas ver o ingresa '000' para salir"))
                if seleccion_id==000:
                    return
                
                if any(dep.depatmentId== seleccion_id for dep in self.departamentos):
                    self.mostrar_obras_departamento(seleccion_id)
                    break

                else:
                    print("ID invalido.")
            
            except ValueError:
                print("Ingresa un numero")

#Mostrar contenido de departamento
    def mostrar_obras_departamento(self, department_id):
        pass
