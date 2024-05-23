#Funções

print("FUNCOES")

def hello_world():                      #Função que quando chamada realizará tudo dentro dela
    print("Hello, World!")              #Imprime a string 
    print("Oi, Mundo!")                 #Imprime a string 
    print("Salut, Monde!")              #Imprime a string 
    print("Hola, Mundo!")               #Imprime a string 

for i in range(3):                      #Até que i for 3 entra dentro do FOR
    hello_world()                       #Função chamada e realizará o que a função foi definida anteriormente


#Funções com parâmetros

print("FUNCOES COM PARAMETRO")

def uma_funcao(x):                      #Função que quando chamada realizará tudo dentro dela
    print("x = %d" % x)                 #Imprime o valor de x

uma_funcao(5)                           #Função chamada com um parametro nela que realizará o que a função foi definida anteriormente

#Funções com retorno

print("FUNCOES COM RETORNO")

def soma(a, b):                         #Função que quando chamada realizará tudo dentro dela
    return a + b                        #Realiza a soma entre os valores e retorna essa soma

c = soma(7, 5)                          #Função chamada com dois parametro nela que realizará o que a função foi definida anteriormente
print("c = %d" % c)                     #Imprime o valor de c


#Funções com parâmetros default

print("FUNCOES COM PARAMETROS DEFAULT")

def multiplica(a, b=2):                 #Função que quando chamada realizará tudo dentro dela
    return a * b                        #Realiza a multiplicação entre os valores e retorna essa soma

print(multiplica(5, 84))                #Função chamada com dois parametros nela que realizará a função definida anteriormente

print(multiplica(7))                    #Função chamada com um parametro nela, sendo que o segundo parametro torna-se o valor colocado
                                        #na função anteriormente