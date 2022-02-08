from functools import reduce

paises = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
nomes = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for pais in paises:
    print(pais)

for nome in nomes:
    print(nome)

for numero in numeros:
    print(numero)

def caixa_alta(string):
    return string.upper()
paises_caixa_alta = list(map(caixa_alta, paises))

def num_quadrado(num):
    return num ** 2
numeros_quadrado = list(map(num_quadrado, numeros))

def caixa_alta(string):
    return string.upper()
nomes_caixa_alta = list(map(caixa_alta, nomes))

def tem_land(string):
    if 'land' in string:
        return True
    return False
land_paises = list(filter(tem_land, paises))

def tem_seis_caracteres(string):
    if len(string) == 6:
        return True
    return False
paises_seis_caracteres = list(filter(tem_seis_caracteres, paises))

def tem_maisouseis_caracteres(string):
    if len(string) >= 6:
        return True
    return False
paises_seisoumais_caracteres = list(filter(tem_maisouseis_caracteres, paises))

def pais_inicia_e(string):
    if string[0] == 'E':
        return True
    return False
paises_inicia_e = list(filter(pais_inicia_e, paises))

def soma_nums(x, y):
    return int(x) + int(y)
total = reduce(soma_nums, numeros)