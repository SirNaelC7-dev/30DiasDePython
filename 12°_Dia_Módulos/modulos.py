import string
from random import choice, randint


def id_aleatorio_usuario(tamanho = 6, digito = string.digits, letras = string.ascii_lowercase + string.ascii_uppercase):
    return ''.join(choice(digito+letras) for i in range(tamanho)) 

def id_gerador_usuario(tamanho = 6, quantidade=1, digito = string.digits, letras = string.ascii_lowercase + string.ascii_uppercase):
    ids=list()
    for x in range(quantidade):
        id =  ''.join(choice(digito+letras) for i in range(tamanho)) 
        ids.append(id)
    return ids
    
def rgb_gerador():
    vermelho = randint(0, 255)
    verde = randint(0, 255)
    azul = randint(0, 255)
    return f'rgb({vermelho},{verde},{azul} )'
