

class Museo:
    def __init__(self):
        self.departamentos = []

    def start(self):

        print('''   
        Bienvenido al Catálogo 
                    de la 
            Colección de Arte del 
        Museo Metropolitano de Arte
        ''')

        nombre=(input('Ingresa tu nombre: '))

        print(f'''Bienvenido {nombre}, ingresa una opcion valida,
            para la busqueda de obras de arte:

            1-Por Departamento
            2-Por Nacionalidad de Autor
            3-Por Nombre de Autor
            4-Salir del sistema
            ''')
        option=(input('Ingresa una opcion: '))

        while True:
        
            if option== "1":
                pass
                
            elif option == "2":
                pass
            
            elif option == "3":
                pass
            
            elif option == "4":
                print(f'Gracias por visitarnos {nombre}, hasta luego.')
                break
            
            else:
                print(f'Opcion invalida, por favor ingresa una de las opciones disponibles {nombre}')
                break
            

        

