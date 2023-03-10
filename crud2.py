from pathlib import Path

current_path = Path.cwd()
file_path = current_path / 'score.txt'

try:
    #param: #r leer #a agregar #w escribir #wb #rb #ab
    scores = []
    with open(file_path, 'r') as file: 
        for line in file.readlines():
            scores.append(int(line))
            
    scores.sort()
    print(scores[::-1])

except Exception as err:
   pass

finally:
    print(scores)
