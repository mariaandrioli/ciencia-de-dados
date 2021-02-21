from types import new_class
import numpy as np
import sys


def main(file1, file2):
    #remoção fim de cada linha
    separated = []
    with open(file1, "r") as file:
        for i in range(17):
            next(file)
        for line in file:
            if line[0] == '#':
                separated.append(line.split('#', 1)[-1].split('('))
            else:
                separated.append(line.split('('))

    without_empty = []
    for element in separated:
        without_empty.append([string for string in element if string != ""])     

    separated = []
    for element in without_empty:
        separated.append([string for string in element if string != "\n"])   

    final = []
    for element in separated:
        if len(element) > 0:
            final.append(element[0].split(' '))

    #print(*final, sep='\n')
    
    #data = np.loadtxt(without_empty, dtype=str , usecols=(1,6,23))

    # Geração do arquivo de saida
    # file = open("T1p1a.txt", "w") 
    # sorted = np.sort(new_data)
    # file.write('\n'.join(map(str, sorted)))
    # file.close() 

if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    main(file1 = file1, file2 = file2)