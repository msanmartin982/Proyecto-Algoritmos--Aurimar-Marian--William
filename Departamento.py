''' 
La definicion de esta clase permite establecer ciertos atributos de 'Departamentos' que seran importados
al archivo llamado db, donde obtendremos la informacion proveniente de la API. Es decir, este apartado sirve 
como un preeestablecimiento de ciertos atributos que desearemos en nuestro proyecto.
'''

class Departamento:

        '''
        Representa un departamento con su ID y nombre del departamento.
        '''

        def __init__(self, id, nombre_departamento):
                '''
                Inicializacion de un objeto Departamento.

                Args: 
                        id (int): El ID del departamento.
                        nombre (str): El nombre del departamento.

                Show: 
                        Muestra los atributos deseados; ID y nombre del departamento.
                '''
                self.id = id                            
                self.nombre_departamento = nombre_departamento

        def show(self):
                print(f"ID de Departamento: {self.id}")
                print(f"Nombre de Departamento: {self.nombre_departamento}")

                