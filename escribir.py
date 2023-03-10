from pathlib import Path

def show_content_file(path_file):
    if path_file.is_file() and path_file.exists(): #si el archivo es un file y existe
        return path_file.read_text() # Retorna un string con el contenido del archivo
    
current_directory = Path.cwd() # Permite conocer el directorio actual
path = Path(current_directory) #Instanciar un objeto path

path_folder = path / 'archivos'

if not path_folder.exists():
    path_folder.mkdir() #si la carpeta no existe procede a crear

path_file = path_folder / 'score.txt'

content = ''
if path_file.exists():
    content = show_content_file(path_file)

score = input('Ingresa tu puntaje: ')
content = content + '\n' + str(score)
path_file.write_text(content)
#path_file.write_text('se elimina todo el contenido.') #texto
#path_file.write_text(str(score)) #numero



