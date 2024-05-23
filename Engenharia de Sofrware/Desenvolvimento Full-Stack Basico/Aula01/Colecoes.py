#Listas

print("LISTAS: ")

numeros = [1, 10, 100, 1000]            #Atibui uma lista de numeros na variável

print(numeros)                          #Imprime a lista

print(numeros[2])                       #Imprime o elemento no índice 2, sempre começando pelo 0

#Operações de listas

print("OPERACAO DE LISTAS: ")

numeros += [10000, 1000000]             #Adicionando 2 novos itens na lista, usando +=

print(numeros)                          #Imprime os itens da lista

numeros.append(10000000)                #Adiciona 1 novo item utlizando append

print(numeros)                          #Imprime os itens da lista

numeros[1:3] = [7]                      #Substituiu os itens nas posições 1 e 2 da lista por 7, então os numeros 10 e 100 são trocados
                                        #[índice_incluído:índice_exluído]
print(numeros)                          #Imprime os itens da lista

numeros[1:3] = []                       #Substituiu os itens nas posições 1 e 2 da lista por 7, então os numeros 7 e 1000 são trocados

print(numeros)                          #Imprime os itens da lista

print(len(numeros))                     #Imprime o tamanho da lista


#Tuplas

print("TUPLAS: ")

naipes = ('copas', 'ouros', 'espadas', 'paus')      #Atribui um tupla de itens na variável

print(naipes)                                       #Imprime a tupla com os itens atribuidos


#Dicionários 

print("DICIONARIOS: ")

notas = {"Ana": 8, "Maria": 5, "Thais": 10}         #Cria um dicionário e atribui a variável

print(notas)                                        #Imprime o dicionário

print(notas["Thais"])                               #Imprime o valor correspondente à chave "Thais"

notas["Zaira"] = 9                                  #Adiciona um novo item

print(notas)                                        #Imprime todos os itens

del notas["Thais"]                                  #Deleta o item "Thais" do dicionário

print(notas)                                        #Imprime todos os itens

print("Maria" in notas)                             #Checa se cotem "Maria" nas notas