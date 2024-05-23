#Tipos variáveis

print("TIPOS VARIAVEIS")

tipo_string = "Aluno"  #Variável com letras e números
tipo_inteiro = 7       #Variável com somentes números inteiros
tipo_float = 7.584     #Variável com números com virgula
tipo_booleano = True   #Variável com dois tipos de valores (Verdadeiro ou Falso)

#Imprime os tipos de valriaveis e os valores inclusos nela

print(tipo_float)          #Imprime o valor da variável
print(type(tipo_float))    #Imprime o tipo dela

#Casting: Convertendo a variavel

print("CASTING")

print(int(tipo_float))    #Convertendo o tipo float em um inteiro
print(str(tipo_float))    #Convertendo o tipo float em uma string

#Operações Aritméticas

print("OPERACOES ARITMETICAS")

resultado_1 = 7 + 5                         #Operação soma
resultado_2 = tipo_inteiro - resultado_1    #Operação subtração
resultado_3 = resultado_2 * 3               #Operação multiplicação
resultado_4 = resultado_3 / 4               #Operação divisão
resultado_5 = 2 ** 4                        #Potencialização
resultado_6 = 2 % 4                         #Resto da divisão

#Imprime todos os resultados contatenando uma string com o resultado numérico

print("Resultado da soma = " + str(resultado_1))                #Imprime o resultado da soma 
print("Resultado da subtracao = " + str(resultado_2))           #Imprime o resultado da subtração
print("Resultado da multiplicacao = " + str(resultado_3))       #Imprime o resultado da multiplicação
print("Resultado da divisao = " + str(resultado_4))             #Imprime o resultado da divisão
print("Resultado da potenciacao = " + str(resultado_5))         #Imprime o resultado da potenciação
print("Resultado do resto da divisao = " + str(resultado_6))   #Imprime o resultado da divisão

#Incremento e Decremento 

print("INCREMENTO E DECREMENTO")

tipo_inteiro -= 3       #Decrementando em 3
print("Resultado do decremento: " + str(tipo_inteiro))      #Imprime o resultado do decremento = 7 - 3 = 4,
                                                            #com isso o tipo_inteiro passou a ser 4

tipo_inteiro += 5       #Incrementando em 5
print("Resultado do incremento: " + str(tipo_inteiro))      #Imprime o resultado do incremento = 4 + 5 = 9,
                                                            #com isso o tipo_inteiro passou a ser 9