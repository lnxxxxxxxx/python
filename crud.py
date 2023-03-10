from pathlib import Path

current_path = Path.cwd()
file_path = current_path / 'score.txt'
#file_path = current_path / 'novela.txt'

# file = open(file_path) #por default el trabajo con este archivo sera de lectura
# content = file.read()
# file.close()

try:
    #param: #r leer #a agregar #w escribir #wb #rb #ab
    with open(file_path, 'r') as file: #hace lo mismo que open() 
        score = file.read() #lee
        #file.write('\nEstamos escribiendo.')

except Exception as err:
    score = 0
    with open(file_path, 'w') as file:
        file.write(str(score))

finally:
    print(score)


