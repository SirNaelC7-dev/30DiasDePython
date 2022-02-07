"""numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negativo_zero = [i for i in numbers if i <= 0]


lista_de_listas =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
numeros_lista_das_listas = [numero for numero in lista_de_listas for numero in numero for numero in numero]


seq_potenciada = [(i, i**0 , i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(seq_potenciada)

paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lista = [list(tupla) for tupla in paises for tupla in tupla]

paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lista = [dict(pais_cidade) for pais_cidade in paises for pais_cidade in paises]
"""

nomes = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenado = [nome for nome in nomes for nome in nome for nome in nome]
print(concatenado)
