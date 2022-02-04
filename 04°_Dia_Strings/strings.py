espaco = ' '
var1 = 'Thirty'
var2 = 'Days'
var3 = 'Of'
var4 = 'Python'

concatenacao = var1 + espaco + var2 + espaco + var3 + espaco + var4

var1 = 'Coding'
var2 = 'For'
var3 = 'All'
concatenacao = var1 + espaco + var2 + espaco + var3

empresa = 'Coding For All'

print(empresa)

print(len(empresa))

empresa = empresa.upper()

empresa = empresa.lower()

empresa = empresa.capitalize()
empresa = empresa.title()
empresa = empresa.swapcase()

primeira_palavra = empresa[0:6]

print(empresa.index('Coding'))
print(empresa.find('Coding'))

print(empresa.replace( 'Coding','Python'))

frase = 'Python for Everyone'
frase = frase.replace('Everyone', 'All')

empresa = empresa.split()

empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
empresas = empresas.split(', ')

print(empresa[0])

print(empresa[-1])

print(empresa[10])

frase = 'Python For Everyone'
print(frase[0:len(frase)-2:4])


print(frase[0:len(frase)-2:len(frase)-3])

var_c = frase.index('C')
print(var_c)

var_f = frase.index('F')
print(var_f)

frase = 'Coding For All People'
var_i = frase.rfind('i')

frase = 'You cannot end a sentence with because because because is a conjunction'
ocorrencia = frase.index('because')

ocorrencia = frase.rindex('because')
print(ocorrencia)

corte = frase[31:54]

ocorrencia = frase.find('because')

frase = frase.replace(' because because because ', ' ')

frase = 'Coding For All'
frase = frase.find('Coding')==0

frase = frase.find('Coding') == -1

frase = '  Coding For All    '
frase = frase.strip(' ')

var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'

print(var1.isidentifier())
print(var2.isidentifier())

frameworks = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
lista = ' '.join(frameworks)
print(lista)

print('I am enjoying this challenge.\nI just wonder what is next.')

print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2d.' %(radius, area)

print(f'radius = {radius}')
print('area = {} * radius ** 2'.format(pi))
print(formated_string)

var1, var2 = 8, 6
print('{} + {} = {}'.format(var1, var2, var1+var2))
print('{} - {} = {}'.format(var1, var2,var1-var2))
print('{} * {} = {}'.format(var1, var2, var1*var2))
print('{} / {} = {:.2f}'.format(var1, var2, var1/var2))
print('{} % {} = {}'.format(var1, var2, (var1%var2)))
print('{} // {} = {}'.format(var1, var2, var1//var2))
print('{} ** {} = {}'.format(var1, var2, var1**var2))
