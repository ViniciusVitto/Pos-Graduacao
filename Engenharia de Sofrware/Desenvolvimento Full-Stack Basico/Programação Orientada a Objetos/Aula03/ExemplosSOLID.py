#Exemplo SPR Não-Aplicado

#A classe Animal tem mais de uma responsabilidade. Ela representa um animal e seus comportamentos além de ser responsável por salvar
#no banco de dados:

class AnimalSPRNaoAplicado: 

    def __init__(self, nome):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome
    
    def salvar(self):
        #Salva o animal no banco de dados
        pass

#Aplicando SPR

#Teremos uma classe para cada responsabilidade

class AnimalSPRAplicado:

    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
class AnimalDAO:
    
    def salvar(self, animal: AnimalSPRAplicado):
        #Salva o animal no banco de dados
        pass

#Exemplo OCP Não-Aplicado

#À medida que tivermos novos animais no nosso programa, teremos que modificar a classe Animal.

class AnimalOCPNaoAplicado:

    def __init__(self, nome):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome
    
    def faz_som(self):
        if self.__nome == "Cachoro":
            print("Au Au")
        if self.__nome == "Gato":
            print("Miau")

#Aplicando OCP

#Teremos uma classe para cada tipo de animal.

class AnimalOCPAplicado:

    def __init__(self, nome):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome
    
    def faz_som(self):
        pass

class Cachorro(AnimalOCPAplicado):
    def faz_som(self):
        print("Au Au")

class Gato(AnimalOCPAplicado):
    def faz_som(self):
        print("Miau")

#Exemplo LSP Não-Aplicado

class AnimalLSPNaoAplicado:
    pass

class Cachorro(AnimalLSPNaoAplicado):

    def latir(self):
        print("Au Au")

class Gato(AnimalLSPNaoAplicado):

    def miar(self):
        print("Miau")

class Dono:

    def passear(self, cachorro:Cachorro):
        cachorro.latir()

#Aplicando LSP

class AnimalLSPAplicado:
    def faz_som(self):
        pass

class Cachorro(AnimalLSPAplicado):

    def faz_som(self):
        self.__latir()

    def __latir(self):
        print("Au Au")

class Gato(AnimalLSPAplicado):

    def faz_som(self):
        self.__miar()

    def __miar(self):
        print("Miau")

class Dono:

    def passear(self, animal:AnimalLSPAplicado):
        animal.faz_som()

#Exemplo ISP Não-Aplicado

#Nesse emplo, podemos utilizar a classe ImpressoraFazTudoISPNaoAplicado como base da classe ImpressoraMultifuncionalNaoAplicado, porque
#a impressora multifuncional imprime, digitaliza e envia faz. Mas se formos utilizar a class ImpressoraFazTudoISPNaoAplicado para uma
#ImpressoraPadrão, violaremos o princípio ISP, porque ela irá herdar métodos que não serão utilizados(digitaliza e envia faz).

class ImpressoraFazTudoISPNaoAplicado:

    def imprime(self):
        pass

    def digitaliza(self):
        pass
    
    def envia_fax(self):
        pass

class ImpressoraMultifuncionalNaoAplicado(ImpressoraFazTudoISPNaoAplicado):

    def imprime(self):
        pass

    def digitaliza(self):
        pass

    def envia_fax(self):
        pass

#Aplicando ISP

#Vamos dividir a classe Impressora em classes menores, pare que as classes cliente implementem somente o que precisam.

class Impressora:

    def imprime(self):
        pass

class Digitalizadora:

    def digitaliza(self):
        pass

class Fax:

    def envia_fax(self):
        pass

class ImpressoraMultifuncionalISPAplicado(Impressora, Digitalizadora, Fax):
    
    def imprime(self):
        pass

    def digitaliza(self):
        pass

    def envia_fax(self):
        pass

class ImpressoraPadraoISPAplicado(Impressora):

    def imprime(self):
        pass

#DIP
#Exemplo de código
class Animal:

    def faz_som(self):
        pass

class Cachorro(Animal):

    def faz_som(self):
        self.latir()

    def latir(self):
        print("Au Au")

class Gato(Animal):

    def faz_som(self):
        self.miar()

    def miar(self):
        print("Miau")

#Exemplo DIP Não-Aplicado

class DonoDIPNaoAplicado:

    def passear(self, cachorro:Cachorro):
        cachorro.latir()

#Exemplo DIP Aplicado

class DonoDIPAplicado:

     def passear(self, animal:Animal):
        animal.faz_som()