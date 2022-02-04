for i in range(0, 10):
    print(i)

i = 0
while i != 10:
    print(i)
    i+=1

for i in range(10, 0, -1):
    print(i)

i = 10
while i != 0:
    print(i)
    i-=1

for  i in range(1,8):
    print(i * '#')

for x in range(0,8):
    for y in range(1):
        print(8 * ' #')

for i in range(0,11):
    print('{} x {} = {}'.format(i, i, i**2))

lista = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in lista:
    print(item)

for i in range(0,100):
    if i%2==0:
        print(i)
    else:
        continue

for i in range(0,100):
    if i%2==1:
        print(i)
    else:
        continue

soma = 0
for i in range(0, 101):
    soma+=i

print('A soma de todos os elementos é {}'.format(soma))


soma_pares = 0
for i in range(0, 101):
    if i%2==0:
        soma_pares+=i

print('A soma de todos os pares é {}'.format(soma_pares))

paises = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 
    'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 
    'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 
    'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 
    'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 
    'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 
    'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 
    'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 
    'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 
    'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 
    'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 
    'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 
    'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 
    'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 
    'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 
    'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 
    'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 
    'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 
    'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe',
    'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 
    'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 
    'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 
    'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 
    'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 
    'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
    ]

paises_land = []

for pais in paises:
    if pais.count('land') >= 1:
        paises_land.append(pais)
    else:
        continue

frutas = ['banana', 'orange', 'mango', 'lemon']
frutas_revertidas = []

for i in range(len(frutas)-1, -1, -1):
    frutas_revertidas.append(frutas[i])

print(frutas_revertidas)
