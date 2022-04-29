import requests

req = requests.get("https://google.com")
print(req)

cabecalho = {"User-Agent": "Windows 11"}
cookies = {"Last-Visit": "101020"}
data = {"Username": "admin",
        "Password": "admin"}

req = requests.post("https://google.com", headers=cabecalho, cookies=cookies, data=data)
print(req)




