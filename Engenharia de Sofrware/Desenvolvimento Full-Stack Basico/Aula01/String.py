#Concatenação de String

print("CONCATENACAO DE STRING")

programacao = "Programacao"                     #Pode ser delimitada tanto com aspas duplas,
oo = 'OO'                                       #quanto por aspas simples, porem sempre combinando.
proragamacao_oo = programacao + " " + oo        #Concatenação entre as strings

print(proragamacao_oo)                          #Imprime o resultado da concatenação
print(oo + " " + programacao)                   #Fazendo a concatenação direto na impressão

#Tamanho da string 

print("TAMANHO DA STRING")

print(len(proragamacao_oo))                     #Imprime o tamanho da string através da função len

#Indexação e substrings

print("INDEXACAO E SUBSTRINGS")

frase = "Python e muito divertido!"

print(frase[3])                 #Imprime a 3 letra da string, sendo que na indexação começa com 0

print(frase[-1])                #Imprime a última letra da frase

print(frase[-2])                #Imprime a penúltima letra da frase

#string[start:end] e o end não é incluso
print(frase[:4])                #Termina na quarta letra, lembrando que inicia com 0, então não esta incluso o "o" 
print(frase[10:])               #Começa no décima letra e vai até o final
print(frase[5:10])              #Começa na quinta letra e termina na décima sem incluir a décima
print(frase[:])                 #Imprime toda a frase

#Multiplicação de uma string por um numero 

print("MULTIPLICACAO DE UMA STRING POR UM NUMERO")

ola = "ola"                 #Atribui o "ola" na string
sete_olas = ola * 7         #Atribui 7 vezes a string 

print(sete_olas)            #Imprime a string

#Operador in

print("OPERADOR IN")

programacao_python = "Programacao em Python"        #Atribui "Programacao em Python" na string

print("Python" in programacao_python)               #Checa se a string contém "Python" e Imprime se é (Verdadeiro ou Falso)

print("python" in programacao_python)               #Checa se a string contém "python" e Imprime se é (Verdadeiro ou Falso)

print("abacate" in programacao_python)              #Checa se a string contém "abacate" e Imprime se é (Verdadeiro ou Falso)

#Escaping

print("ESCAPING")

print("Estou estudando\n" + programacao_python)     #Imprime a string com um pulo de linhas devido ao "\n"

#Maiúsculas e Minúsculas

print("MAIUSCULO E minusculo")

print(programacao_python.lower())                   #Imprime tudo minúsculo
print(programacao_python.upper())                   #Imprime tudo maiúsculo

tudo_minusculo = "aula de python"
print(tudo_minusculo.capitalize())                  #Imprime com a primeira letra maiúscula

#Formatação

print("FORMACAO")

nome = "Belinha"
num_int = 7
num_dec = 7.584

print("Ola, meu nome e %s! Tenho %d anos e %d reais"            #Imprime o float como inteiro
      %(nome, num_int, num_dec))                                

print("Ola, meu nome e %s! Tenho %d anos e %f reais"            #Imprime o float como float
      %(nome, num_int, num_dec))

print("Ola, meu nome e %s! Tenho %d anos e %.2f reais"          #Imprime o float com duas casas decimais
      %(nome, num_int, num_dec))