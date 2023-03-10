from pathlib import Path

# Path('/mnt/c/users/pachi/desktop/proyectos/python/pathPy')
# print(Path.cwd())

current_directory = Path.cwd() # Permite conocer el directorio actual
current_path = Path(current_directory) #Instanciar un objeto path

if current_path.is_dir():
    for dir in current_path.iterdir():
        print(dir.name)

