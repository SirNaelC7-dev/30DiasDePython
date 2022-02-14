class Estatistica:
    def __init__(self, lista=[]):
        self.lista = lista
    
    def contar(self):
        return len(self.lista)
        
    def media(self):
        return sum(self.lista)/len(self.lista)
        
    def maximo(self):
        return max(self.lista)

    def minimo(self):
        return min(self.lista)

    def soma(self):
        return sum(self.lista)
            

class PersonAccount:
    def __init__(self, nome, sobrenome, rendimentos, propriedades_despesas, renda_total, despesa_total, info_conta,):
        self.nome = nome
        self.sobrenome = sobrenome
        self.rendimentos = rendimentos
        self.propriedades = propriedades_despesas
        self.renda_total = renda_total
        self.despesa_total = despesa_total
        self.info_conta = info_conta

