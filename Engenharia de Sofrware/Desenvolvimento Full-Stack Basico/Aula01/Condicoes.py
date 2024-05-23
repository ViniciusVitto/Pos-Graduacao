#Comando IF

print("IF: ")

nome = "Ana"
idade = 25

if nome == "Ana":                       #Se o nome for "Ana" entra dentro do IF
    print("Passou!")                    #Imprime caso passe do IF

if nome == "Ana" or idade == 17:                #Se o nome for "Ana" ou Se a idade for igual a 17 entra dentro IF
    print("Passou de novo!")                    #Imprime caso passe do IF
    print("%s tem %d anos" %(nome, idade))      #Imprime caso passe do IF


#Comandos IF, ELIF E ELSE

print("IF, ELIF E ELSE: ")

dias = ["sabado", "domingo"]

if len(dias) == 0:                              #Se o tamanho do array for 0 entra no IF
    print("Lista vazia")                        #Imprime caso passe do IF
elif len(dias) == 1:                            #Se o tamanho do array for 1 entra no IF
    print("so um dia")                          #Imprime caso passe do ELIF
else:                                           #Caso nao passe em nenhum if acima entra no else
    print("Tamanho %d" % len(dias))             #Imprime caso entre no else