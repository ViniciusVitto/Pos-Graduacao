#PROGRAMA 01

class Pessoa:
    num_pessoas = 0
    def __init__(self, nome):
        self.nome = nome
        Pessoa.num_pessoas += 1
    

nomes = ['Joao', 'Paulo', 'Jorge', 'Ringo']
pessoas = [Pessoa(nome) for nome in nomes]
print(Pessoa.num_pessoas)
print(pessoas[0].nome)