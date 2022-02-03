idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Você tem idade suficiente para dirigir!')
else:
    print('Aguarde até possuir idade para dirigir\nDaqui há {} ano(s) você terá idade suficiente!'.format(abs(idade-18)))


minha_idade = 20
sua_idade = int(input('Digite sua idade: '))


if minha_idade > sua_idade:
    print('Eu sou mais velho que você por {} ano(s) de diferença'.format(abs(minha_idade-sua_idade)))
elif sua_idade > minha_idade:
    print('Você é mais velho que eu por {} ano(s) de diferença'.format(abs(sua_idade - minha_idade)))
else:
    print('Nossas idades são correspondentes!')


numero_um = int(input('Digite o primeiro número: '))
numero_dois = int(input('Digite o segundo número: '))

if numero_um > numero_dois:
    print('{} é maior que {}'.format(numero_um, numero_dois))
elif numero_um < numero_dois:
    print('{} é menor que {}'.format(numero_um, numero_dois))
else:
    print('{} é igual a {}'.format(numero_um, numero_dois))


pontuacao = int(input('Insira sua pontuação entre(0-100): '))

if pontuacao <= 100 and pontuacao >= 80:
    print('A')
elif pontuacao >= 70 and pontuacao <= 79:
    print('B')
elif pontuacao >= 60 and pontuacao <= 69:
    print('C')
elif pontuacao >= 50 and pontuacao <= 59:
    print('D')
elif pontuacao >= 0 and pontuacao <= 49:
    print('F')
else:
    print('Insira um número entre (0-100) na próxima execução')


outono = ('setembro', 'outubro', 'novembro')
inverno = ('dezembro', 'janeiro', 'fevereiro')
primavera = ('março','marco', 'abril', 'maio')
verao = ('junho', 'julho', 'agosto')

mes_do_ano = input('Me informe o mês do ano que te informarei a estação do ano: ').lower()
if mes_do_ano in outono:
    print('A estação do ano é Outono')
elif mes_do_ano in inverno:
    print('A estação do ano é Inverno')
elif mes_do_ano in primavera:
    print('A estação do ano é Primavera')
elif mes_do_ano in verao:
    print('A estação do ano é Verão')
else:
    print('Verifique se informou corretamente o mês do ano!')

frutas = ['banana', 'laranja', 'manga', 'limão']

fruta = input('Informe uma fruta para verificar presença na lista: ')
if fruta not in frutas:
    print('A fruta foi adicionada na lista!')
    frutas.append(fruta)
else:
    print('A fruta já está presente na lista!')

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

verificacao = 'skills' in person

if verificacao:
    tamanho = len(person[('skills')])//2
    print(person['skills'][tamanho])

if verificacao:
    python = 'Python' in person['skills']
    if python:
        print(python)

print(person['skills'])

fron_end = ['JavaScript', 'React']
back_end = ['Node', 'Python', 'MongoDB']
full_stack = ['React', 'Node', 'MongoDb']

if fron_end == person['skills']:
    print('Ele é um desenvolvedor Front-End')

elif back_end == person['skills']:
    print('Ele é um desenvolvedor Back-End')

elif full_stack == person['skills']:
    print('Ele é um desenvolvedor FullStack')

else:
    print('Nenhum título encontrado')

if person['is_marred'] and person['country']=='Finland':
    print('{} {} lives in {}. He is married'.format(person['first_name'], person['last_name'], person['country']))

