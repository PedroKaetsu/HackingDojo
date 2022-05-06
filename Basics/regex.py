import re

string = "My CPF is 418.657.983-02"

pattern = re.search(
    r"([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})", 
    string)

if pattern:
    print(pattern.group())
else:
    print("Padrão não encontrado")