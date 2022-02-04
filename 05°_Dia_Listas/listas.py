import statistics
lista_op1 = list()
lista_op2 = []

lista_itens = ['eu', 'tu', 'ele', 'nós' 'vós', 'eles']

print(len(lista_itens))

primeiro_item = lista_itens[0]
meio_item = lista_itens[len(lista_itens)//2]
ultimo_item = lista_itens[-1]

lista_variada = ['Naelson', '20', 1.80, 'Solteiro', 'RN']

companhias = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(companhias)

print(len(companhias))

primeiro_item = companhias[0]
meio_item = companhias[len(companhias)//2]
ultimo_item = companhias[-1]

print(primeiro_item)
print(meio_item)
print(ultimo_item)

companhias[0] = 'Udemy'
print(companhias)

companhias.append('Cisco')

companhias.insert(len(companhias)//2, 'SpaceX')

companhias[0] = 'UDEMY'

companhias.remove('IBM')

lista = '#; '.join(companhias)

print('Oracle' in companhias)

companhias.sort()

companhias.sort(reverse=True)

corte_primeiras = companhias[0:3]

corte_ultimas = companhias[-3:]

divisao_1 = companhias[0: len(companhias)//2]
divisao_2 = companhias[-len(companhias)//2: ]

del companhias[0]

del companhias[(len(companhias)//2)]

companhias.pop()

companhias.clear()

del companhias

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)

full_stack = front_end.copy()

full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')

idades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

idades.sort()

idades.append(idades[0])
idades.sort()
idades.append(idades[-1])

mediana = statistics.median(idades)

media = sum(idades)/len(idades)

intervalo_maxmin = abs(idades[0] - idades[-1])

print(abs(idades[0]-media), abs(idades[-1]-media))











