import numpy as np
import sys

def main(filename):
    # Leitura do arquivo de entrada
    data = np.loadtxt(filename, dtype=str , delimiter=":", skiprows=1, usecols=2)
    clean = (line.replace('-',',') for line in data)
    clean = (line.split('.', 1)[-1] for line in clean)
    new_data = np.loadtxt(clean, dtype=str)

    # Geração do arquivo de saida
    file = open("T1p1a.txt", "w") 
    sorted = np.sort(new_data)
    file.write('\n'.join(map(str, sorted)))
    file.close() 

if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename = filename)