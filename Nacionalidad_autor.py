import requests

class Nacionalidad:
        def nationality():
            nat= requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
            return nat.json()
