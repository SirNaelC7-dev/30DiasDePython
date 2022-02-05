def soma(num1, num2):
    return num1 + num2

def area_do_circulo (r):
    pi = 3.14
    area = pi * r ** 2
    return area

def soma_nums(*nums):
    total = 0
    for num in nums:
        total+=num
    return total

def conversor_fahrenheit(g_celsius):
    g_farenheit = (g_celsius * 9/5) + 32
    return g_farenheit

def verificar_estacao(mes):
    if mes == 'setembro' or 'outubro' or 'novembro':
        return 'A estação do mês é outono!'
    elif mes == 'dezembro'or 'janeiro'or 'fevereiro':
        return 'A estação do mês é inverno!'
    elif mes == 'março' or 'marco' or 'abril' or 'maio':
        return 'A estação do mŝ é primavera!'
    elif mes == 'junho' or 'julho' or 'agosto':
        return 'A estação do ano é verão!'
    else:
        return 'A forma que você informou o mês está fora do formarto!'

def imprime_lista(lista=[]):
    for elemento in lista:
        print(elemento)
    return 'Todos os elementos foram impressos!'

def reverter_lista(lista=[]):
    lista_revertida = []
    for i in range(len(lista)-1, -1, -1):
        lista_revertida.append(lista[i])
    return lista_revertida

def capitalizar(lista=[]):
    lista_capitalizada = []
    for elemento in lista:
        lista_capitalizada.append(elemento.capitalize())
    return lista_capitalizada

def adicionar_item(item, lista=[]):
    itens = lista
    itens.append(item)
    return itens

def remover_item(item, lista=[]):
    if item in lista:
        lista.remove(item)
    return lista

def soma_numeros(num):
    soma = 0
    for x in range(1,num+1):
        soma += x
    return soma

def soma_impares(num):
    soma = 0
    for x in range(1,num+1):
        if x%2==1:
            soma+=x
    return soma

def soma_pares(num):
    soma = 0
    for x in range(1,num+1):
        if x%2==0:
            soma+=x
    return soma

def pares_impares(intervalo):
    par = impar = 0
    for x in range(intervalo+1):
        if x % 2 == 0:
            par += 1
        else:
            impar += 1
    return f'O número de pares é {par} e o número de ímpares é {impar}'

def fatorial(num):
    fatorial = num
    for x in range(1, num):
        fatorial *= x
    return fatorial

def verifica_vazio(arg):
    if len(arg)==0:
        return True
    else:
        return False
