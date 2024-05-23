#PROGRAMA 03

def bem_vindo():
        print("Calculadora simples em Python")
        calcular()

def calcular():
        print("\nQual operacao deseja executar? (1) Soma (2) Subtracao (3) Multiplicacao (4) Divisao ")
        operacao = int(input("Digite a operacao a ser realizada: "))

        if(operacao !=1 and operacao !=2 and operacao !=3 and operacao !=4):
                print("Desculpe, esta calculadora ainda nao suporta esta operacao. Por favor, execute o programa novamente")
                return
        
        num_um = int(input("Digite o primeiro numero: "))
        num_dois = int(input("Digite o segundo numero: "))

        if(operacao == 1):
                print("O resultado e", num_um + num_dois)
        elif(operacao == 2):
                print("O resultado e", num_um - num_dois)
        elif(operacao == 3):
                print("O resultado e", num_um * num_dois)
        else:
                print("O resultado e", num_um / num_dois)
        
        calcular_outra_vez()


def calcular_outra_vez():
        outra_vez = input("Deseja realizar outra operacao? Por favor, digite S para SIM ou N para NAO: ")

        if outra_vez.upper() == 'S':
                calcular()
        elif outra_vez.upper() == 'N':
                print("Até a proxima")
        else:
                print("Opcao invalida.")
                calcular_outra_vez()

bem_vindo()