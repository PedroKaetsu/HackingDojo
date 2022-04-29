def openFile():
    try:
        open("file.txt", "r")
        return True
    except:
        print("Não foi possível abrir o arquivo")
        return False

while not openFile():
    print("Tentando abrir o arquivo")

print("Arquivo aberto")

