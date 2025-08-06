from PIL import Image
import requests

class Imagen:
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

        except requests.exceptions.RequestException as e:
            print(f"Error al descargar la imagen: {e}")
        
        except IOError as e:
            print(f"Error al guardar o abrir la imagen: {e}")

        except Exception as e:
            print(f"Ocurrió un error inesperado al mostrar la imagen: {e}")
        return nombre_archivo_final
    
    # nombre_archivo_destino = 
    # imagen = Image.open(nombre_archivo_final)
    # imagen.show()
    # print("Cierre la ventana de la imagen para continuar")