import requests
import json

def request(title):
    try:
        req = requests.get("https://www.omdbapi.com/?apikey=822cf0ce&t=" + title)
        dict = json.loads(req.text)
        return dict

    except:
        print("Erro na Conexão")
        return None

dict = request("Matrix")

print("Título: ", dict["Title"])
print("Lançamento: ", dict["Released"])
print("Gênero: ", dict["Genre"])