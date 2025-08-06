from db import *

class Museo:
    def __init__(self):
        self.departamentos = cargar_departamentos()
        self.nacionalidades = cargar_nacionalidades()
        self.obras = []

    def start(self):
        
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
                        self.mostrar_obras_nacionalidad()
                
                    elif menu == "3":
                        pass
                
                    elif menu == "4":
                        break
            elif opcion == "2":
                pass
            elif opcion == "3":
                print("Hasta luego!")
            else:
                print(f'Opcion invalida, por favor ingresa una de las opciones disponibles')
                break
                
    #Se guarda las obra revisando que no se guarde duplicada         
    def guardar_obra(self, obra_a_guardar):
        for obra in self.obras:
            if obra_a_guardar.id == obra.id:
                pass
            else:
                self.obras.append(obra_a_guardar)

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

#    Mostrar contenido de departamento
    def mostrar_obras_departamento(self,depart_id):
        self.departamentos = obtener_id_departamento()
        self.detalles_obras=obtener_detalles_obras()
        id_objetos= self.departamentos(depart_id)
        if not obj_id:
            print("No se encontraron obras")
            return
        print(f"Obras en el Departamento{depart_id}")

        for obj_id in id_objetos:
            obra=self.detalles_obras(obj_id)
            if obra:
                print(f"Id: {obra.id}, Titulo {obra.titulo}, Autor: {obra.autor}")
            
            else:
                print("No se pudieron obtener las obras")
                
    #Muestra obras segun su nacionalidad
    def mostrar_obras_nacionalidad(self):
        while True:
            i = 1
            for nacionalidad in self.nacionalidades:
                print(f"{i} - {nacionalidad.nombre}")
                i += 1
            while True:
                nacionalidad_a_buscar = input("Ingrese la nacionalidad de las obras que desea ver: ")
                encontrada = False
                for nacionalidad in self.nacionalidades:
                    if nacionalidad_a_buscar == nacionalidad.nombre:
                        encontrada = True
                if encontrada == True:
                    obras = buscar_obra_nacionalidad(nacionalidad_a_buscar)
                    if obras is not None:
                        for obra in obras:
                            self.guardar_obra(obra)
                    break
                else:
                    print("Ingrese una nacionalidad válida.")
            break
