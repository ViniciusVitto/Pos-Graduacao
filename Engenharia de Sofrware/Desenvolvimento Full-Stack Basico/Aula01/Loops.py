#FOR

print("FOR:")

for i in range(6):                  #Até que i faça o loop até 6, entra dentro do FOR
    print(i)                        #Imprime o valor de i

#OBS: A função range() pode ser considerada em três formas:
#   range(stop_value): Considera o ponto inicial como zero e vai até o valor colocado
#   range(start_value, stop_value): Gera uma sequência baseado nos valores adicionados
#   range(start_value, stop_value, step_size): Gera a sequência incrementando o valor inicial usando o tamanho do passo,
                                               #até atingir o valor final 


#WHILE

print("WHILE:")

numero = 1

while numero <= 7:                  #Enquanto o numero nao for menor ou igual a sete, entra dentro do while
    print(numero)                   #Imprime o valor
    numero += 1                     #Incrementa o numero em + 1


#BREAK

print("BREAK: ")

count = 0

while True:                         #Enquanto for verdade entrará no while
    print(count)                    #Imprime o valor
    count += 1                      #Incrementa o contador em + 1
    if count >= 5:                  #Se o contador for maior ou igual a 5, entra no IF
        break                       #Faz com que para o while



#CONTINUE

print("CONTINUE: ")

for i in range(5):                  #Até que i faça o loop até 5, entra dentro do FOR
    if i == 3:                      #Se o valor i for igual a 3, entra dentro do IF
        continue                    #Faz com que continue o FOR, voltando nele de novo
    print(i)                        #Imprime o valor de i