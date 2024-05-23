
class ListaDeNumeros:
    def __init__(self, numeros):
        self.numeros = numeros
    def __str__(self):
        return ",".join([str(n) for n in self.numeros])
    def soma(self):
        return sum(self.numeros)
    def media(self):
        return self.soma()/len(self.numeros)
    
minha_lista = ListaDeNumeros([1,3,5,7,9])

print(f"A soma de {minha_lista} e {minha_lista.soma()}")
print(f"A media de {minha_lista} e {minha_lista.media()}")