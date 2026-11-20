import os

inscritos = ["Maria Silva Advogada", "Vitor Silva Professor"]
with open("inscritos.txt", "w", newline='') as t:
    for line in inscritos:
        t.write(line + os.linesep)