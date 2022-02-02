"""dog = {}

dog['nome', 'cor', 'raca','idade' ] = ['cachorro', 'marrom-caramelo', 'vira-copo', 37]
"""
estudante = {
    'primeiro_nome' : 'Dobby',
    'ultimo_nome' : 'Potter',
    'sexo' : 'masculino',
    'idade' : 73,
    'estado_civil' : 'solteiro',
    'habilidades' :['manuseio_de_varinha', 'feitiçaria', 'trabalhos_domésticos'],
    'endereco':{
        'pais' : 'Brasil',
        'cidade' : 'Assú'
    }
}

#print(len(estudante))

#print('habilidades :',estudante['habilidades'], 'tipo de dado das habilidades :',len(estudante['habilidades']))

#estudante['habilidades'].append('cuidador')

#lista_chaves = estudante.keys()

#lista_valores = estudante.values()

dct_lista = estudante.items()

print(type(dct_lista))









