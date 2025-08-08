'''
Importamos todo el archivo db, que es nuestra base de datos, e importamos el archivo que nos va a permitir ver las imagenes.
'''
from db import *
from Imagen import Imagen

'''
Esta clase hara funcionar todo nuestro catalogo del Museo de Arte. Es la ejecucion de nuestro sistema.
'''
class Museo:
    def __init__(self):
        self.departamentos = cargar_departamentos()
        self.nacionalidades = cargar_nacionalidades()
        self.imagen = Imagen()
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
            
            if opcion == "1":

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
                    
                    elif menu == "2":
                        self.mostrar_obras_nacionalidad()
                
                    elif menu == "3":
                        self.mostrar_obras_autor()
                
                    elif menu == "4":
                        break

            elif opcion == "2":
                self.mostrar_detalles_obras()

            elif opcion == "3":
                print()
                print("Hasta luego!")
                break

            else:
                print(f'Opcion invalida, por favor ingresa una de las opciones disponibles: ')
                break
                
    '''
    Se guarda la obra revisando que no se guarde duplicada.
    '''         
    def guardar_obra(self, obra_a_guardar):
        for obra in self.obras:
            if obra_a_guardar.id == obra.id:
                pass
            else:
                self.obras.append(obra_a_guardar)

    '''
    Iniciamos el desarrollo de la opcion de obtener los departamentos.
    '''
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

    '''
    Mostrar contenido de departamento.
    '''
    def mostrar_obras_departamento(self,depart_obj):
        id_objetos=obtener_id_departamento(depart_obj.id)
        if not id_objetos:
            print("No se encontraron obras")
            return

        '''
        Proceso de control de cantidad de obras a mostrar por departamento, estableceremos grupos de 10 en 10.
        '''
        total_obras=len(id_objetos)
        numero=0
        cantidad=10

        while True:
            if numero >= total_obras:
                print("No hay mas obras que mostrar para este departamento")
                break
            obras_para_mostrar=id_objetos[numero:numero+cantidad]
        
            for obj_id in obras_para_mostrar:
                obra=buscar_objeto_por_id(obj_id)
                if obra:
                    obra.show()
            
                else:
                    print("No se pudieron obtener las obras")
        
            numero += cantidad

            if numero< total_obras:
                respuesta= input("Si deseas ver mas obras ingresa 'si', de lo contrario 'no': ").lower()
                if respuesta != 'si':
                    break
            else:
                print("Todas las obras de este departamento han sido mostradas")
                break

                
    '''
    Muestra obras segun su nacionalidad.
    '''
    def mostrar_obras_nacionalidad(self):
        while True:
            i = 1
            for nacionalidad in self.nacionalidades:
                print(f"{i} - {nacionalidad.nombre}")
                i += 1
            while True:
                nacionalidad_a_buscar = input("Ingrese la nacionalidad de las obras que desea ver: ").capitalize()
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


    '''
    Muestra obras segun el nombre del autor.
    '''
    def mostrar_obras_autor(self):
        autor_a_buscar = input("Ingrese el nombre del autor de las obras que desea ver: ")
        obras = buscar_obra_nombre_artista(autor_a_buscar)
        if obras is not None:
                for obra in obras:
                    self.guardar_obra(obra)


    '''
    Muestra los detalles de las obras segun el ID.
    '''
    def mostrar_detalles_obras(self):
        while True:
            try:
                seleccion_id_objeto = int(input("Ingresa el ID de la obra para ver sus detalles o ingresa '000' para salir: "))
                if seleccion_id_objeto == 000:
                    return
                break

            except ValueError:
                print("Opcion Invalida. Ingresa un numero: ")

        obra = obtener_detalles_obras(seleccion_id_objeto)

        if obra:
            print()
            print("Detalles de la Obra: ")
            print()
            obra.show()

            if obra.imagen:
                ver_imagen = input("¿Desea ver la imagen de la obra? Si deseas verla ingresa 'si', de lo contrario ingresa 'no': ").lower()
                if ver_imagen == 'si':
                    self.imagen.mostrar_imagen_obra(obra.imagen, f"obra_{obra.id}")
                
                else: 
                    print("No hay una imagen disponible para esta obra. ")

            else:
                print(f"No se pudo encontrar la imagen de la obra con ID '{seleccion_id_objeto}' o hubo un error al obtener los detalles de la obra. ")