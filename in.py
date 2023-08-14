import os

'''separa listas com aquivos e extensoes'''
curr_dir = os.getcwd()
curr_dir
arquivos = os.listdir(curr_dir)
lista_arquivos = [i for i in arquivos if os.path.isfile(i) and '.py' not in i]
tipos = [i.split('.')[1] for i in lista_arquivos]

'''criar as pastas referentes as extensoes caso ainda não existam'''
for i in tipos:
    if not os.path.isdir(i):
        os.mkdir(i)

'''transfere os arquivos para as devidas pastas atraves de renomeação'''
for i in lista_arquivos:
    origem = os.path.join(curr_dir,i)
    destino = os.path.join(curr_dir,i.split('.')[-1],i)
    os.rename(origem,destino)
