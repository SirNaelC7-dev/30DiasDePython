try:
    name = input('Digite seu nome:')
    year_born = input('Ano que nasceu:')
    age = 2022 - int(year_born)
    print(f'Eu sou {name}. Minha idade é {age}.')
except TypeError:
    print('TypeError')
except ValueError:
    print('ValueError')
except ZeroDivisionError:
    print('ZeroDivisionError')
else:
    print('Eu costumo correr com o bloco try.')
finally:
    print('Eu fui executado.')



paises = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*paises_nordicos, es, ru = paises


print(paises_nordicos)
print(es)
print(ru)
