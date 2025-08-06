from db import *

class Museo:
    def __init__(self):
        self.departamentos = cargar_departamentos()
        self.nacionalidades = cargar_nacionalidades()
        self.obras = []

    def start(self):
        
        while True:
            
            opcion=input('''
        Bienvenido al Catálogo 
                de Arte 
-----------del Museo MetroArt---------------                         
Selecciona una opcion:                        
1-Busqueda de obras
2-Mostrar detalles de obras por ID conocido
3-Salir
                            
------------> ''')
            
            if opcion=="1":
                while True:
                    menu= input("""
                Ingresa la opcion que deseas:
                1-Ver lista de obras por Departamento
                2-Ver lista de obras por Nacionalidad de Autor
                3-Ver lista de obras por Nombre de Autor
                4-Volver al menu inicial
                ----> """)
            
                    if menu== "1":
                        self.obtener_departamentos()
                        pass
                    
                    elif menu == "2":
                        self.mostrar_obras_nacionalidad()
                
                    elif menu == "3":
                        self.mostrar_obras_autor()
                
                    elif menu == "4":
                        break
            elif opcion == "2":
                pass
            elif opcion == "3":
                print("Hasta luego!")
                break
            else:
                print(f'Opcion invalida, por favor ingresa una de las opciones disponibles: ')
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
                seleccion_id=int(input("Ingresa el ID del departamento que deseas ver o ingresa '000' para salir: "))
                if seleccion_id==000:
                    return
                
                departamento_encontrado=None
                for dep in self.departamentos:
                    if dep.id==seleccion_id:
                        departamento_encontrado=dep
                        break
                
                if departamento_encontrado:
                    self.mostrar_obras_departamento(departamento_encontrado)

                else:
                    print("ID invalido.")
            
            except ValueError:
                print("Ingresa un numero")

    #Mostrar contenido de departamento
    def mostrar_obras_departamento(self,depart_obj):
        id_objetos=obtener_id_departamento(depart_obj.id)
        if not id_objetos:
            print("No se encontraron obras")
            return

        obras_para_mostrar=id_objetos[0:10]

        for obj_id in obras_para_mostrar:
            obra=buscar_objeto_por_id(obj_id)
            if obra:
                obra.show()
            
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

    #Muestra obras segun el nombre del autor
    def mostrar_obras_autor(self):
        autor_a_buscar = input("Ingrese el nombre del autor de las obras que desea ver: ")
        obras = buscar_obra_nombre_artista(autor_a_buscar)
        if obras is not None:
                for obra in obras:
                    self.guardar_obra(obra)

