import numpy as np
import sys

def main(filename):
    # remoção fim de cada linha
    separated = []
    with open(filename, "r") as file:
        for line in file:
            separated.append(line.split(':')[0])

    # algumas variantes tem mais de um hifen
    content = []
    for element in separated:
        content.append(element.replace('-','.',1))

    # leitura do dado
    data = np.loadtxt(content, delimiter='.', dtype=str , usecols=(1,2,3,4))

    # junção do dado para impressao
    content = []
    for element in data:
        content.append(','.join(element))

    # Geração do arquivo de saida
    file = open("T1p1b.txt", "w") 
    file.write('\n'.join(map(str, content)))
    file.close() 


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename = filename)