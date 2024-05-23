#Operadores de Igualdade

print("OPERADORES DE IGUALDADE")

var_um = 1              #Atribuindo o valor 1 a variável
var_dois = 2            #Atribuindo o valor 2 a variável
var_tres = 3            #Atribuindo o valor 3 a variável
 
print(1 == var_um)      #Imprime se 1 é igual ao valor do var_um
print(2 == var_um)      #Imprime se 2 é igual ao valor do var_um

equal = (var_um == var_dois)        #Atribuindo se o var_um é igual ao var_dois
                                    #Os () são opcionais nesse caso, so ajudam na legibilidade do código
not_equal = (var_um != var_dois)    #Atibuindo se o var_um é diferente do var_dois

print("Um e igual a dois? " + str(equal))               #Imprime o resultado da variável equal
print("Um e diferente de dois? " + str(not_equal))      #Imprime o resultado da variável not_equal

#Operadores de Comparação

print("OPERADORES DE COMPARACAO")

print("Um e maior do que dois? " + str(var_um > var_dois))      #Imprime se o var_um é maior que o var_dois
print("Um e menor do que dois? " + str(var_um < var_dois))      #Imprime se o var_um é menor que o var_dois