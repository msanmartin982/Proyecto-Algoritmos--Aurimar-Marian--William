''' 
La definicion de esta clase permite establecer ciertos atributos de 'Autor', que estara a su vez
inmerso en los detalles de las obras, es decir, cuando el usuario opte por la opcion numero 2 en nuestro menu,
se procedera a la utilizacion de ciertas inicializaciones que dejamos plasmadas en este archivo.
'''
class Autor:
        '''
        Representa el autor con sus detalles relevantes.
        '''
        '''
        Inicializacion del objeto Autor.
        '''
        def __init__(self, nombre, nacionalidad, fecha_nacimiento, fecha_muerte):
                self.nombre = nombre
                self.nacionalidad = nacionalidad
                self.fecha_nacimiento = fecha_nacimiento
                self.fecha_muerte = fecha_muerte
        '''
        Muestra los atributos deseados; nombre, nacionalidad, nacimiento y muerte del autor.
        '''
        def show(self):
                print(f"Nombre del autor: {self.nombre}")
                print(f"Nacionalidad: {self.nacionalidad}")
                print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
                print(f"Fecha de muerte: {self.fecha_muerte}")