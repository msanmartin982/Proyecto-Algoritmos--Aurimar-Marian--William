'''
Esta clase permite establecer ciertos atributos que desearemos plasmar mas adelante en nuestro codigo.
Se importara a nuestra db, y utilizara en la debida obtencion de la informacion proveniente de la API.
'''

class Nacionalidad:

    '''
    Representa una nacionalidad para los autores.
    '''

    def __init__(self, nombre):
        '''
        Inicializacion de un objeto Nacionalidad.

        Args:
            nombre(str)= nombre de la nacionalidad.
        '''
        self.nombre = nombre


