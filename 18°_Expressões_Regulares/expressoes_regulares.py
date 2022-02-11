import re


paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

paragraph = re.sub('[.]', '', paragraph)
palavras = re.split(' ',paragraph)

resultado = [(palavras.count(palavra), palavra) for palavra in palavras]
resultado = sorted(set(resultado), reverse=True)

print(resultado)


regex_pattern = r'^[\D]' and r'^[a-z]'
txt = 'firstname'
match = bool(re.findall(regex_pattern, txt))
print(match)


sentenca = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
sentenca_limpa = re.sub('[%@&#;$?!,.]', '', sentenca)

palavras = re.split(' ',sentenca_limpa)

resultado = [(palavras.count(palavra), palavra) for palavra in palavras]
resultado = sorted(set(resultado), reverse=True)
resultado = resultado[0:3]

print(resultado)