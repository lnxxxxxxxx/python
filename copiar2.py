
import shutil  
from pathlib import Path

current_path = Path.cwd()

folder_path = current_path / 'archivos'

file_path = folder_path / 'score.txt'
copy_file_path = folder_path / 'copy-score.txt'


if not folder_path.exists():
    folder_path.mkdir() 

try: 
    with open(file_path, 'w') as file:
            file.write(str(0))
except:
    pass

#shutil.move()
shutil.copy(file_path, copy_file_path) 
#copy_file_path.unlink() #elimin archivo
#shutil.rmtree(folder_path) #elmina la carpeta