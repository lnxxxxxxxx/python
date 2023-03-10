from pathlib import Path

# Path('/mnt/c/users/pachi/desktop/proyectos/python/pathPy')
# print(Path.cwd())
def show_content_file(path_file):
    if path_file.is_file() and path_file.exists(): #si el archivo es un file y existe
        return path_file.read_text() # Retorna un string con el contenido del archivo
    
current_directory = Path.cwd() # Permite conocer el directorio actual
path = Path(current_directory) #Instanciar un objeto path

path_folder = path / 'archivos'

if not path_folder.exists():
    path_folder.mkdir() #si la carpeta no existe procede a crear

# iteramos osbnre los directorios de la carpeta - archivos    
# for dir in path_folder.iterdir():
#     if dir.is_file() and dir.suffix == '.txt':
#         print(dir.name)

# Mostramos el contenido del archivo - carpeta   
file = input('Ingresa el nombre del archivo: ') 
content = show_content_file(path_folder / file ) 
print(content)

