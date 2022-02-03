#!/usr/bin/env python
# coding: utf-8

# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# ![python-1536x650.png](attachment:python-1536x650.png)

# # <center> <u>Exercícios Funções
# <center><font color='#787878'>Exercícios disponíveis no link: https://wiki.python.org.br/ExerciciosFuncoes, desenvolvidos por mim para aperfeiçoamento profissional.
#     
#     

# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>1. Faça um programa para imprimir:</b>
# 
#         1
#         2   2
#         3   3   3
#         .....
#         n   n   n   n   n   n  ... n
# 
# <b>para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.</b>

# In[ ]:


def imprime_linha(n):
    for n in range(1, n+1):
        for qtd in range(n, n+1):
            print(f'{n} ' * qtd )

n = int(input('Quantos Números? '))
imprime_linha(n)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>2. Faça um programa para imprimir:</b>
# 
#         1
#         1   2
#         1   2   3
#         .....
#         1   2   3   ...  n
# 
# <b>para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.</b>

# In[ ]:


def imprime_sequencia(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(f'{j} ', end= '')
        print()

n = int(input('Até que número? '))
imprime_sequencia(n)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>3. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

# In[ ]:


def soma(a, b=0, c=0):
    return(a + b + c)

soma(5, 9, 8)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>4. Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

# In[ ]:


def positivoNegativo(n):    
    return('N' if n <= 0 else 'P')
positivoNegativo(0)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>5. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

# In[ ]:


def somaImposto(taxaImposto, custo):
    return round((1 + taxaImposto/100) * custo, 2)

somaImposto(10, 100)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>6. Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

# In[ ]:


def conversao(h):
    return 'P' if (h > 12) and (h < 25) else 'A'

def saida(h, m):    
    return (f'{h}:{m} - A.M.' if conversao(h) == 'A'             else f'{h-12}:{m} - P.M.')
    
while True:    
    hora = int(input('Hora: [-1 para Sair]: '))    
    while hora < -1 or hora > 24:
        hora = int(input('Hora Inválida. Digite a Hora: [-1 para Sair]: '))
        
    if hora == -1:
        break
    
    minuto = int(input('Minuto: '))
    while minuto < 0 or minuto > 59:
        minuto = int(input('Minuto Inválido. Digite o Minuto: '))

    print(f'{saida(hora, minuto)}' + '\n' + '*'*25)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>7. Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

# In[ ]:


def valorPagamento(prestacao, dias):    
    return prestacao * 1.03 + 0.001 * dias if dias > 0 else prestacao

qtd = total = 0

while True:
    prestacao = float(input('Valor da prestação [0 -> SAIR]: R$ '))
    if prestacao == 0:
        print('*' * 40 + '\n' + f'Total: R$ {total:.2f} - Quantidade: {qtd} ')
        break
    dias = int(input('Dia em atraso: '))
    print(f'Valor a ser pago: R$ {valorPagamento(prestacao, dias) :.2f}')
    print('*' * 40)
    qtd += 1
    total += valorPagamento(prestacao, dias)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>8. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

# In[ ]:


def qtdDigitos(n):
    return len(str(n))

qtdDigitos(189)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>9. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

# In[ ]:


def reverso(n):
    return n[::-1]

numero = str(input('Informe um número: ')).strip()
print(f'{numero} -> {reverso(numero)}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>10. Jogo de Craps. Faça um programa que implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

# In[ ]:


import random as rd

def lancarDados():
    return rd.randint(2, 13)

while True:
    str(input('Aperte uma tecla para rolar os dados: '))
    resultado = lancarDados()
    
    if resultado == 7 or resultado == 11:
        print(f'Resultado: {resultado}\nVocê é um natural. Ganhou!')
        break
    elif resultado == 2 or resultado == 3 or resultado == 12:
        print(f'Resultado: {resultado}\nCRAPS. Perdeu!')
        break
    else:
        resultado2 = 0
        while True:
            str(input(f'Aperte uma tecla para rolar os dados novamente (OBjetivo: {resultado}): '))
            resultado2 = lancarDados()
            print(f'Resultado: {resultado2}')
            print('*'*70)
            
            if resultado2 == resultado:
                print('Venceu!')
                break
            elif resultado2 == 7:
                print('Perdeu!')
                break
    break


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>11. Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

# In[ ]:


def dataExtenso(data):
    listaMes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
           'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        
    return (data[0:2] + ' de ' + listaMes[int(data[3:5]) -1] + ' de ' + data[6:10])

dataExtenso('01/12/2014')
    


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>12. Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

# In[ ]:


def embaralhaPalavra(p):
    import random as rd
    
    p = list(p)
    rd.shuffle(p)
    p = ''.join(p)
    return print(p.upper())

embaralhaPalavra('Python')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>13. Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

# In[ ]:


def desenhaMoldura(linhas=1, colunas=1):
    
    if linhas > 20:        linhas = 20
    if colunas > 20:       colunas = 20
    if linhas < 1:        linhas = 1
    if colunas < 1:       colunas = 1
    
    print('+' + '-' * (colunas-2) + '+')
    for l in range(linhas):
        print('|' + ' '*(colunas-2) + '|')
    print('+' + '-' * (colunas-2) + '+')
    
desenhaMoldura(-10, 25)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>14. Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:</b>
# 
#     8  3  4 
#     1  5  9
#     6  7  2
# 
# <b>Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.</b>

# In[ ]:


from itertools import combinations, permutations

def validador(t):
    if sum(t[:3]) == sum(t[3:6]) == sum(t[6:10]) == sum(t[::3]) == sum(t[1::3]) == sum(t[2::3]) ==     sum(t[::4]) == sum(t[2:8:2]):                
        print('\n', t[0], t[1], t[2],              '\n', t[3], t[4], t[5],              '\n', t[6], t[7], t[8],              '\n', '-'*5)
        return 1
    else:
        return 0

def gerador(tab):
    total_combinacoes = 0
    quadrados_magicos = 0
    for i in permutations(tab,9):
        total_combinacoes += 1
        quadrados_magicos += validador(i)
    print(f'Total de Combinações: {total_combinacoes}')
    print(f'Total de Quadrados Mágicos: {quadrados_magicos}')

t = [1,2,3,4,5,6,7,8,9]

gerador(t)

