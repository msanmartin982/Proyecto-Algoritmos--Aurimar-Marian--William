import requests 
def get_departments():
        url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        response = requests.get(url)
        data = response.json()
        return data["departments"]

