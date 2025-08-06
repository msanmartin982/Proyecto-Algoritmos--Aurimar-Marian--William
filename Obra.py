class Obra:
    def __init__(self, id, titulo, nombre_autor):
        self.id = id
        self.titulo = titulo
        self.nombre_autor = nombre_autor

    def show(self):
        print(f"\nID de la Obra: {self.id}")
        print(f"Titulo de la Obra: {self.titulo}")
        print(f"Nombre del Autor de la Obra: {self.nombre_autor}")


class Detalles(Obra):
    def __init__(self, id, titulo, nombre_autor, nacionalidad, fecha_nacimiento, fecha_muerte, clasificacion, año_creacion, imagen):
        super().__init__(id, titulo, nombre_autor)
        self.nacionalidad = nacionalidad   
        self.fecha_nacimiento = fecha_nacimiento   
        self.fecha_muerte = fecha_muerte  
        self.clasificacion = clasificacion
        self.año_creacion = año_creacion
        self.imagen = imagen

    def show(self):
        super().show()
        print(f"Nacionalidad del Autor: {self.nacionalidad}")
        print(f"Fecha de Nacimiento del Autor: {self.fecha_nacimiento}")
        print(f"Fecha de Muerte del Autor: {self.fecha_muerte}")
        print(f"Clasificacion de la Obra: {self.clasificacion}")
        print(f"Año de creacion de la Obra: {self.año_creacion}")
        print(f"URL de la Imagen de la Obra: {self.imagen}")