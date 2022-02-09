#SyntaxError
print 'Olá mundo'
#Correção
print('Olá mundo')


#NameError
print(idade)
#Correção
idade = 37
print(idade)

#IndexError
numbers = [1, 2, 3, 4, 5]
print(numbers[5])
#Correção
print(numbers[4])#Último índice da lista

#ModuloNotFoundError
import maths
#Correção
import math

#AttributeError
math.PI
#Correção
print(math.pi)

#KeyError
user = {'name':'Asab', 'age':250, 'country':'Finland'}
print(user['county'])
#Correção
print(user['country'])

#TypeError
print(4 + '3')
#Correção
print(3 +int('3'))
print(3 + float('3'))

#ImportError
from math import power
#Correção
from math import pow
print(pow(2, 3))

#ValueError
print(int('12a'))

#ZeroDivisionError
print(1/0)







