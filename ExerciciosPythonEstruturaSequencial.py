#!/usr/bin/env python
# coding: utf-8

# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# ![python-1536x650.png](attachment:python-1536x650.png)

# # <center> <u>Exercícios de Estrutura Sequencial Python
# <center><font color='#787878'>Exercícios disponíveis no link: https://wiki.python.org.br/EstruturaSequencial, desenvolvidos por mim para aperfeiçoamento profissional.</font>

# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.

# In[ ]:


print('Alô Mundo!')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]. 

# In[ ]:


numero = int(input('Digite um número: '))
print(f'O número digitado foi {numero}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>3. Faça um Programa que peça dois números e imprima a soma. 

# In[ ]:


numero1 = int(input('Digite o 1º valor: '))
numero2 = int(input('Digite o 2º valor: '))
print(f'{numero1} + {numero2} = {numero1 + numero2}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>4. Faça um Programa que peça as 4 notas bimestrais e mostre a média. 

# In[ ]:


listaNotas = []
for nota in range(1,5):
    listaNotas.append(int(input(f'Digite a {nota}ª Nota: ')))
print(f'A média de notas do aluno foi: {sum(listaNotas)/len(listaNotas)}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>5. Faça um Programa que converta metros para centímetros. 

# In[ ]:


numeroMetros = float(input('Digite a quantidade de metros: '))
print(f'{numeroMetros:.0f} metro(s) = {numeroMetros*100:.0f} centímetros.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. 

# In[ ]:


import math
valorRaio = float(input('Qual o valor do raio: '))
print(f'Um círculo cujo raio seja {valorRaio} possui área igual à {math.pi * math.pow(valorRaio, 2):.2f} ')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. 

# In[ ]:


valorLado = float(input('Informe o valor do lado: '))
print(f'Área do quadrado = {math.pow(valorLado, 2)}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 

# In[ ]:


valorHora = float(input('Informe o valor da hora: R$ '))
nHoras = int(input('Informa a quantidade de horas trabalhadas: '))
print(f'Você receberá R$ {valorHora * nHoras:.2f} este mês.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.<br>C = 5 * ((F-32) / 9). 

# In[ ]:


tempFah = float(input('Digite o valor da tempecratura em Fahrenheit: '))
print(f'{tempFah} Fahrenheit = {5*((tempFah-32)/9):.2f}º Celsius')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. 

# In[ ]:


tempCelsius = float(input('Digite o valor da tempecratura em º Celsius: '))
print(f'{tempCelsius}ºC = {(tempCelsius * 9/5)+32:.2f} Fahrenheit')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:<br>
#     a. o produto do dobro do primeiro com metade do segundo.<br>
#     b. a soma do triplo do primeiro com o terceiro.<br>
#     c. o terceiro elevado ao cubo. 

# In[ ]:


nInt1 = int(input('Informe o 1º número inteiro: '))
nInt2 = int(input('Informe o 2º número inteiro: '))
nFlo1 = float(input('Informe um número real: '))

print(f'a. {nInt1} x {nInt2 / 2} = {nInt1*(nInt2/2)}')
print(f'b. {nInt1 * 3} + {nFlo1} = {nInt1 + nFlo1}')
print(f'c. {nFlo1}³ = {math.pow(nFlo1, 3)}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 

# In[ ]:


alturaPessoa = float(input('Informe a altura da pessoa em metros: '))
print(f'O peso ideal para uma pessoa com {alturaPessoa} metros de altura é {(72.7*alturaPessoa)-58:.2f}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:<br>
#     a. Para homens: (72.7*h) - 58<br>b. Para mulheres: (62.1*h)-44.7    

# In[ ]:


alturaPessoa = float(input('Informe a altura da pessoa em metros: '))
print(f'O peso ideal para um HOMEM com {alturaPessoa} metros de altura é {(72.7*alturaPessoa)-58:.2f}')
print(f'O peso ideal para uma MULHER com {alturaPessoa} metros de altura é {(62.1*alturaPessoa)-44.7:.2f}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas. 

# In[ ]:


pesoPeixe = float(input('Informe o peso do peixe em Kg: '))
excesso = pesoPeixe - 50
multa = excesso * 4
if excesso > 0:    print(f'Peixe com {pesoPeixe} excedeu em {excesso} Kg. Valor da multa: R$ {multa:.2f}')
else:    print('Peixe não excedeu o peso.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:<br>
# 
#     a. salário bruto. 
#     b. quanto pagou ao INSS. 
#     c. quanto pagou ao sindicato. 
#     d. o salário líquido. 
#     e. calcule os descontos e o salário líquido, conforme a tabela abaixo: 
# 
# ![ex15.jpg](attachment:ex15.jpg)<br>
# 
# <i>Obs.: Salário Bruto - Descontos = Salário Líquido.</i>

# In[ ]:


valorHora = float(input('Informe o valor da hora: R$ '))
nHoras = int(input('Informa a quantidade de horas trabalhadas: '))
salarioBruto = valorHora * nHoras
ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - ir - inss - sindicato
print(f'+ Salário Bruto: R$ {salarioBruto}')
print(f'- IR (11%): R$ {ir}')
print(f'- INSS (8%): R$ {inss}')
print(f'- Sindicato (5%): R$ {sindicato}')
print(f'= INSS (8%): R$ {salarioLiquido}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 

# In[ ]:


tamanhoArea = float(input('Informe o valor da área em m²: '))
litrosMetro = tamanhoArea/3
qtdLatas = int(litrosMetro/18)
valorLata = 80
if litrosMetro % 18 != 0:    qtdLatas += 1

print(f'Para {tamanhoArea}m² deve-se utilizar {qtdLatas}. Custo: R$ {qtdLatas * valorLata}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R 80,00 ou em galões de 3,6 litros, que custam R 25,00.<br>
# 
#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     a. comprar apenas latas de 18 litros;
#     b. comprar apenas galões de 3,6 litros;
#     c. misturar latas e galões, de forma que o desperdício de tinta seja menor.

# In[ ]:


tamanhoArea = float(input('Informe o valor da área em m²: '))
litrosMetro = tamanhoArea/6
qtdLatas = int(litrosMetro/18)
qtdGaloes = int(litrosMetro/3.6)
valorLata = 80
valorGalao = 25
misturaLata = int(litrosMetro / 18.0)
misturaGalao = int((litrosMetro - (misturaLata * 18)) / 3.6)

# Apenas latas de 18 litros
if litrosMetro % 18 != 0:    qtdLatas += 1
print(f'---- Apenas Latas de 18 litros ----\nPara {tamanhoArea}m² deve-se utilizar {qtdLatas} lata(s). Custo: R$ {qtdLatas * valorLata}')
# Apenas galões de 3.6 litros
if litrosMetro % 3.6 != 0:    qtdGaloes += 1
print(f'---- Apenas Galões de 3.6 litros ----\nPara {tamanhoArea}m² deve-se utilizar {qtdGaloes} galão(ões). Custo: R$ {qtdGaloes * valorGalao}')
# Latas e galões
if litrosMetro - (misturaLata * 18) % 3.6 != 0:    misturaGalao += 1
print(f'---- Misturando Latas e Galões ----\nPara {tamanhoArea}m² deve-se utilizar {misturaLata} Lata(s) e {misturaGalao} galão(ões). Custo: R$ {(misturaLata * valorLata) + (misturaGalao * valorGalao)}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 

# In[ ]:


tamanhoArquivo = float(input('Informe o tamanho do arquivo em MB: '))
velocidadeInternet = float(input('Informe a velocidade da internet em MBps: '))
print(f'Tempo aproximado de download: {((tamanhoArquivo/(velocidadeInternet/8))/60):.1f} minuto(s)')

