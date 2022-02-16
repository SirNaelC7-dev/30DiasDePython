import numpy as np

print('numpy:', np.__version__)
print(dir(np))

lista_python = [1, 2, 3, 4, 5]
print('Type:', type(lista_python))


lista_bidimensional = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(lista_bidimensional)

array_numpy_lista = np.array(lista_python)
print(type(array_numpy_lista))
print(array_numpy_lista)

array_numpy_lista2 = np.array(lista_python, dtype=float)
print(array_numpy_lista2)


array_numpy_booleano = np.array([0, 1, -1, 0, 0], dtype=bool)
print(array_numpy_booleano)

array_numpy_multidimensional = np.array(lista_bidimensional)
print(type(array_numpy_multidimensional))
print(array_numpy_multidimensional)

np_to_list = array_numpy_lista.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', array_numpy_multidimensional.tolist())

python_tupla = (1,2,3,4,5)

print(type (python_tupla))
print('python_tuple: ', python_tupla) 

numpy_array_tupla = np.array(python_tupla)
print(type (numpy_array_tupla)) 
print('numpy_array_from_tuple: ', numpy_array_tupla)