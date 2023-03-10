import shutil  
from pathlib import Path

current_path = Path.cwd()
folder_path = current_path / 'archivos'

file_path = folder_path / 'score.txt'
new_file_path = folder_path / 'puntajes.txt'
copy_file_path = folder_path / 'copia-puntajes.txt'


if not folder_path.exists():
    folder_path.mkdir() #sino existe se crea

#para mover archivo a otro lado
# Origen - Destino => permite mover o renombrar archivos
# shutil.move => argumentos de tipo string
shutil.copy(new_file_path, copy_file_path) 