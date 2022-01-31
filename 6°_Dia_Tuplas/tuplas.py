tupla = ()
tupla = tuple()

irmaos = ('Jorel', 'Irmão do Jorel', 'Márcio Ririzon', 'Carlos Felino')
irmas = ('Granny Juju', 'Vovó Gigi', 'Débora')

todos_irmaos = irmaos + irmas

print(len(todos_irmaos))

pais = ('Tosh', 'Danuza')

membros_familia = todos_irmaos + pais

frutas = ('Uva', 'Maçã', 'Banana', 'Laranja')
vegetais = ('Brócolis', 'Alface', 'Couve', 'Repolho')
produtos_animais = ('Leite', 'Ovo', 'Mel', 'Queijo')
comidas_diversas_tp = frutas + vegetais + produtos_animais

comidas_diversas_lt = list(comidas_diversas_tp)

item_meio_tp = comidas_diversas_tp[len(comidas_diversas_tp)//2]
item_meio_lt = comidas_diversas_lt[len(comidas_diversas_lt)//2]

tres_primeiros_lt = comidas_diversas_lt[0:3]
tres_ultimos_lt = comidas_diversas_lt[-3:]

del comidas_diversas_tp

paises_nordicos = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in paises_nordicos)
print('Iceland' in paises_nordicos)









