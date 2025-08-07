'''
Importamos las librerias que se permitieron utilizar en el proyecto, que son PILLOW y REQUESTS.
'''
from PIL import Image
import requests

'''
Esta clase sera importada en db, ya que es el pilar fundamental, por no decir unico y esencial que nos permitira 
realizar la muestra de las obras como una imagen, cuando se solicite la opcion numero 2 y el usuario desee visualizar 
de que tipo de obra se estan mostrando los detalles. Usualmente tenemos cierto tipo de error por asi decirlo, ya que 
no siempre obtenemos las imagenes, porque el API no las tiene todas, por lo tanto, dice que la imagen no se encuentra.
'''
class Imagen:
    '''
    Representa la imagen de la obra.
    '''

    '''
    Definimos la 'funcion mostrar imagen obra' y realizamos un chequeo de la respuesta del API en caso de tener algun tipo de codigo 
    en estado de error. Se hace un ajuste de formato y a la vez se estable el tipo de archivo que se puede abir con las diferentes
    extensiones que se establecen a continuacion. Ademas, se establece una medida estandar para la muestra de las imagenes. Y finalmente,
    un conjunto de 'except' atadas a nuestra funcion encabezada por el try, que establecen ciertas impresiones en caso de que exista
    algun error.
    '''
    def mostrar_imagen_obra(self, url, nombre_archivo):
        try:
            response = requests.get(url, stream = True)
            response.raise_for_status()

            content_type = response.headers.get("Content-Type")
            extension = ".png" # Valor por defecto
            if content_type:
                if "image/png" in content_type:
                    extension = ".png"
                elif "image/jpeg" in content_type:
                    extension = ".jpg"
                elif "image/svg+xml" in content_type:
                    extension = ".svg"

            nombre_archivo_final = f"{nombre_archivo}{extension}"

            with open(nombre_archivo_final, "wb") as archivo:
                for chunk in response.iter_content(chunk_size = 8192):
                    archivo.write(chunk)
            print(f"Imagen guardada temporalmente como '{nombre_archivo_final}'")

            '''
            Con la siguiente variable 'imagen', procedemos a guardarla y abrirla.
            '''

            imagen = Image.open(nombre_archivo_final)
            imagen.show()
            print()
            print("Cierre la ventana de la imagen para continuar")
            print()

        except requests.exceptions.RequestException as e:
            print(f"Error al descargar la imagen: {e}")
        
        except IOError as e:
            print(f"Error al guardar o abrir la imagen: {e}")

        except Exception as e:
            print(f"Ocurrió un error inesperado al mostrar la imagen: {e}")
        return nombre_archivo_final