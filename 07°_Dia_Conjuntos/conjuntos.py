it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(len(it_companies))

it_companies.add('Twitter')

it_companies.update(['Ubisoft', 'Nintendo', 'Playstation'])

it_companies.remove('Twitter')

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

A.union(B)

A.intersection(B)

print(A.issubset(B))

print(A.isdisjoint(B))

AB = A.union(B)
BA = B.union(A)

print(A.symmetric_difference(B))

del A, B

age = [22, 19, 24, 25, 26, 24, 25, 24]

age_set = set(age)

print('tamanho da lista =',len(age),'\ntamanho do conjunto =' ,len(age_set))

frase = 'I am a teacher and I love to inspire and teach people'
frase = frase.split()
frase = set(frase)
frase.intersection(frase)
