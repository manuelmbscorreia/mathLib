import numpy as np

x = None
n = None


def input_data():
    global n

    n = input("Insira números separados por espaço (para colocar décimas utilize o '.' ")
    n = n.split()
    n = np.array(n)
    n = n.astype(float)

    global x

    x = n

    print(f"Array x = {x}")
    return

# retorna o máximo de todos os valores do array x
def max_array(x):
    max_value = float(np.max(x))
    print(f"Valor Máximo = {max_value}")
    return max_value

# retorna o mínimo de todos os valores do array x
def min_array(x):
    min_value = float(np.min(x))
    print(f"Valor Minimo = {min_value}")
    return min_value

# retorna a média de todos os valores do array x
def avg_array(x):
    avg_value = float(np.average(x))
    print(f"Valor Médio = {avg_value}")
    return avg_value

# retorna o desvio padrão de todos os valores do array x
def std_array(x):
    std_value = float(np.std(x))
    print(f"Desvio Padrão = {std_value}")
    return std_value

# retorna o tamanho do array x
def size_array(x):
    size = int(len(x))
    print(f"Tamanho do Array = {size}")
    return size

# retorna o reverso do array x
def reverse_array(x):
    x = x[::-1]
    print(f"Array em Reverse = {x}")

    return x

# retorna o array x ordenado de acordo com o tipo de ordenação

# asc
def asc_array(x):
    x = sorted(x)
    print(f"Array Ordenado ASC = {x}")

    return x

# desc
def desc_array(x):
    x = sorted(x)
    x = x[::-1]
    print(f"Array Ordenado DESC = {x}")

    return x

