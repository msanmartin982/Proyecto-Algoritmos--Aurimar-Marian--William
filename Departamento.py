''' 
La definicion de esta clase permite establecer ciertos atributos de 'Departamentos' que seran importados
al archivo llamado db, donde obtendremos la informacion proveniente de la API. Es decir, este apartado sirve como un preeestablecimiento de 
ciertos atributos que desearemos en nuestro proyecto
'''

class Departamento:

        '''
        Representa un departamento con su ID y nombre del departamento
        '''

        '''
        Inicializacion de un objeto Departamento
        '''
        def __init__(self, id, nombre_departamento):
                '''
                En base a la API, el ID esta establecido como un (int)
                '''
                self.id = id 
                '''
                En base a la API, el nombre esta establecido como un (str)
                '''                                
                self.nombre_departamento = nombre_departamento

        '''
        Muestra los atributos deseados; ID y nombre del departamento
        '''
        def show(self):
                print(f"ID de Departamento: {self.id}")
                print(f"Nombre de Departamento: {self.nombre_departamento}")