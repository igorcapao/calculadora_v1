# Calculadora em Python


def soma(num1, num2):
    """
    Função que soma 2 números
    """
    return num1 + num2



def subtracao(num1, num2):
    """
    Função que subtrai 2 números
    """
    return num1 - num2



def multiplicacao(num1, num2):
    """
    Função que multiplica 2 números
    """
    return num1 * num2

def divisao(num1, num2):
    """
    Função que divide 2 números
    """
    return num1 / num2



print("\n******************* Python Calculator *******************\n\n Selecione o número da operação desejada:\n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")

option = input('Digite sua opção (1/2/3/4): ')

n1 = int(input('\nDigite o primeiro número: '))
n2 = int(input('\nDigite o segundo número: '))

if option == '1':
    print(f'{n1} + {n2} = {soma(n1, n2)}')
elif option == '2':
    print(f'{n1} - {n2} = {subtracao(n1, n2)}')
elif option == '3':
    print(f'{n1} * {n2} = {multiplicacao(n1, n2)}')
elif option == '4':
    print(f'{n1} / {n2} = {divisao(n1, n2)}')
else:
    print('Opção inválida')
