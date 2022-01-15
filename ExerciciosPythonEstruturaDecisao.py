#!/usr/bin/env python
# coding: utf-8

# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# ![python-1536x650.png](attachment:python-1536x650.png)

# # <center> <u>Exercícios de Estrutura de Decisão
# <center><font color='#787878'>Exercícios disponíveis no link: https://wiki.python.org.br/EstruturaDeDecisao, desenvolvidos por mim para aperfeiçoamento profissional. <br><b>Sem utilização de listas e/ou bibliotecas.</b></font>
#     
#     

# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>1. Faça um Programa que peça dois números e imprima o maior deles.

# In[ ]:


n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))

if n1 > n2:    print(f'O maior é {n1}.')
elif n1 < n2:        print(f'O maior é {n2}.')
else:            print('Números Iguais.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

# In[ ]:


numero = float(input('Digite um número: '))
if numero > 0:    print('Número Positivo')
elif numero < 0:  print('Número Negativo.')
else:             print('Valor 0.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

# In[ ]:


letra = str(input('Informe o Sexo: (F/M): ' )).strip().upper()[0]
if letra == 'F':    print('Sexo Feminino')
elif letra == 'M':  print('Sexo Masculino')
else:               print('Sexo Inválido.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# In[ ]:


letra = str(input('Informe uma letra: ')).strip().lower()[0]
if letra in 'aeiou':    print('Vogal.')
elif letra in '123456789':    print('Númeral.')
elif letra in 'bcdfghjklmnpqrstvwxyz':    print('Consoante.')
else:    print('Símbolo ou pontuação.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# 
#     A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#     A mensagem "Reprovado", se a média for menor do que sete;
#     A mensagem "Aprovado com Distinção", se a média for igual a dez.

# In[ ]:


nota1 = float(input('Valor da P1: '))
nota2 = float(input('Valor da P2: '))
media = (nota1 + nota2)/2
if media == 10:    print(f'Aluno APROVADO COM DISTINÇÃO!')
elif media >= 7:    print(f'Aluno APROVADO com média {media}')
else:    print(f'Aluno REPROVADO com média {media}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>6. Faça um Programa que leia três números e mostre o maior deles.

# In[ ]:


a = int(input('1º Número: '))
b = int(input('2º Número: '))
c = int(input('3º Número: '))
if (a > b):
    if (a > c):        print(a)
    else:        print(c)
elif(b > c):    print(b)
else:        print(c)    


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>7. Faça um Programa que leia três números e mostre o maior e o menor deles.

# In[ ]:


a = int(input('1º Número: '))
b = int(input('2º Número: '))
c = int(input('3º Número: '))
maior = menor = a
if (b > maior):        maior = b
if (c > maior):        maior = c    
if (b < menor):        menor = b
if (c < menor):        menor = c
print(f'Maior: {maior}\nMenor: {menor}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

# In[ ]:


produto1 = float(input('Valor do 1º produto: '))
produto2 = float(input('Valor do 2º produto: '))
produto3 = float(input('Valor do 3º produto: '))

if (produto1 < produto2):
    if (produto1 < produto3):        
        print(f'Comprar o Produto 1. Valor R$: {produto1:.2f}')
    else:        
        print(f'Comprar o Produto 3. Valor R$: {produto3:.2f}')
elif(produto2 < produto3):    
        print(f'Comprar o Produto 2. Valor R$: {produto2:.2f}')
else:   
        print(f'Comprar o Produto 3. Valor R$: {produto3:.2f}') 


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

# In[ ]:


primeiro = int(input('Informe o 1º número: '))
segundo  = int(input('Informe o 2º número: '))
terceiro = int(input('Informe o 3º número: '))

if(terceiro > segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux
if(segundo > primeiro):
    aux = segundo
    segundo = primeiro
    primeiro = aux
if(terceiro > segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux

print(f'{primeiro} -> {segundo} -> {terceiro}.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

# In[ ]:


turno = str(input('Informe seu turno [M/V/N]: ')).upper().strip()[0]

if turno == 'M':      print(f'Período Matutino. Bom Dia!')
elif turno == 'V':    print(f'Período Vespertino. Boa Tarde!')
elif turno == 'N':    print(f'Período Noturno. Boa Noite!')
else:                 print('Valor Inválido!')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#     Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#     
# * salários até R 280,00 (incluindo) : aumento de 20%
# * salários entre R 280,00 e R 700,00 : aumento de 15%
# * salários entre R 700,00 e R 1500,00 : aumento de 10%
# * salários de R 1500,00 em diante : aumento de 5%<br><br>
# Após o aumento ser realizado, informe na tela:<br>
# a. salário antes do reajuste;<br>
# b. percentual de aumento aplicado;<br>
# c. valor do aumento;<br>
# d. novo salário, após o aumento.

# In[ ]:


salarioAtual = float(input('Informe o valor do salário do colaborador: '))

if salarioAtual <= 280:      print(f'a) Salário antes do reajuste: R${salarioAtual:.2f}\nb) Percentual de aumento aplicado: 20%\nc) Valor do aumento: R$ {salarioAtual * 0.2:.2f}\nd) Novo salário: R$ {salarioAtual * 1.2:.2f}    ')
elif salarioAtual <= 700:    print(f'a) Salário antes do reajuste: R${salarioAtual:.2f}\nb) Percentual de aumento aplicado: 15%\nc) Valor do aumento: R$ {salarioAtual * 0.15:.2f}\nd) Novo salário: R$ {salarioAtual * 1.15:.2f}')
elif salarioAtual < 1500:    print(f'a) Salário antes do reajuste: R${salarioAtual:.2f}\nb) Percentual de aumento aplicado: 10%\nc) Valor do aumento: R$ {salarioAtual * 0.1:.2f}\nd) Novo salário: R$ {salarioAtual * 1.1:.2f}    ')
else:    print(f'a) Salário antes do reajuste: R${salarioAtual:.2f}\nb) Percentual de aumento aplicado: 5%\nc) Valor do aumento: R$ {salarioAtual * 0.05:.2f}\nd) Novo salário: R$ {salarioAtual * 1.05:.2f}    ')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# 
#     Desconto do IR:
#     Salário Bruto até 900 (inclusive) - isento
#     Salário Bruto até 1500 (inclusive) - desconto de 5%
#     Salário Bruto até 2500 (inclusive) - desconto de 10%
#     Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
# 
# 
# ![12.jpg](attachment:12.jpg)

# In[ ]:


valorHora = float(input('Informe o valor da hora: R$ '))
qtdHora = int(input('Informe a quantidade de horas trabalhadas: '))

salarioBruto = valorHora * qtdHora

if salarioBruto <= 900:    ir = 0
elif salarioBruto <= 1500:    ir = 0.05
elif salarioBruto <= 2500:    ir = 0.1
else:    ir = 0.2
    
print(f'Salário Bruto: ({valorHora} * {qtdHora}): R$ {salarioBruto:.2f}')
print(f'(-) IR ({ir}%) : R$ {salarioBruto * ir:.2f}')
print(f'(-) INSS (10%) : R$ {salarioBruto * 0.1:.2f}')
print(f'FGTS (11%) : R$ {salarioBruto * 0.11:.2f}')
print(f'Total de descontos: R$ {(salarioBruto * ir) + (salarioBruto * 0.1):.2f}')
print(f'Salário Líquido: R$ {salarioBruto - ((salarioBruto * ir) + (salarioBruto * 0.1)):.2f}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

# In[ ]:


diaSemana = int(input('Informe o dia da semana: '))
if diaSemana == 1:    print('Domingo')
elif diaSemana == 2:  print('Segunda')
elif diaSemana == 3:  print('Terça')
elif diaSemana == 4:  print('Quarta')
elif diaSemana == 5:  print('Quinta')
elif diaSemana == 6:  print('Sexta')
elif diaSemana == 7:  print('Sábado')
else:                   print('Dia Inválido!')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# 
# ![14.jpg](attachment:14.jpg)
#     
# <br>O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

# In[ ]:


nota1 = float(input('Digite o valor da P1: '))
nota2 = float(input('Digite o valor da P2: '))
media = (nota1 + nota2)/2

if media >= 9.0:      conceito = 'A'
elif media >= 7.5:    conceito = 'B'
elif media >= 6.0:    conceito = 'C'
elif media >= 4.0:    conceito = 'D'
else:                 conceito = 'E'

if conceito in 'ABC':
    print(f'Nota P1: {nota1}\nNota P2: {nota2}\Média: {media}\nConceito: {conceito}\nAluno APROVADO.')
else:
    print(f'Nota P1: {nota1}\nNota P2: {nota2}\Média: {media}\nConceito: {conceito}\nAluno REPROVADO.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# 
#     Dicas:
#     Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#     Triângulo Equilátero: três lados iguais;
#     Triângulo Isósceles: quaisquer dois lados iguais;
#     Triângulo Escaleno: três lados diferentes;

# In[ ]:


ladoA = float(input('Primeiro Lado: '))
ladoB = float(input('Segundo Lado: '))
ladoC = float(input('Terceiro Lado: '))

if (ladoA + ladoB > ladoC) & ((ladoA + ladoC > ladoB) & (ladoB + ladoC > ladoA)):
    if (ladoA==ladoB==ladoC):        print('Triângulo Equilátero.')
    elif((ladoA!=ladoB) & (ladoA!=ladoC) & (ladoB!=ladoC)):        print('Triângulo Escaleno.')
    else:        print('Triângulo Isósceles.')
else:    print('Os lados não formam um triângulo.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# 
#     a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#     b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#     c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#     d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

# In[ ]:


a = float(input('Valor de A: '))

if a == 0:    print('Equação não é de segundo grau. Programa Encerrado!')
else:    
    b = float(input('Valor de B: '))
    c = float(input('Valor de C: '))    
    delta = (b * b) - 4 * a * c
    
    if delta == 0:
        raiz = (-b + (delta ** 0.5)/(2 * a))
        print(f'Equação possui apenas uma raiz. Valor: {raiz:.1f}')
    elif delta > 0:
        raiz1 = (-b + (delta ** 0.5)/(2 * a))
        raiz2= (-b - (delta ** 0.5)/(2 * a))
        print(f'Equação possui duas raízes. Valor: Raiz 1: {raiz1:.1f} | Raiz 2: {raiz2:.1f}')
    else:        print('Equação não possui raízes reais.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

# In[ ]:


ano = int(input('Digite o ano com 4 dígitos: '))

if ano%4 == 0:
    if ano%100 == 0:
        if ano%400 == 0:            print('Ano Bissexto')
        else:            print('Ano não Bissexto')    
    else:        print('Ano Bissexto')
else:        print('Ano não Bissexto')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

# In[ ]:


data = str(input('Digite uma data [dd/mm/aaaa]: '))

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:11])

dataValida = False

if (mes == 1) | (mes == 3) | (mes == 5) | (mes == 7) | (mes == 8) | (mes == 10) | (mes == 12):
    if dia <= 31:        
        dataValida = True
elif (mes == 4) | (mes == 6) | (mes == 9) | (mes == 11):
    if dia<=30:
        dataValida = True
elif mes == 2:
    if ano%4 == 0:
        if ano%100 == 0:
            if ano%400 == 0:            
                if (dia<=29):
                    dataValida = True              
        else:        
            dataValida = True       

if dataValida:    print('Data válida')
else:    print('Data Inválida')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# 
#     Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#     326 = 3 centenas, 2 dezenas e 6 unidades
#     12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

# In[ ]:


numero = int(input('Digite um número inteiro menor do que 1000: '))
centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 10)

print(f'{numero} = ', end='')

if centena == 1:    print('1 centena', end='')
elif centena > 1:    print(f'{centena} centenas', end='')

if (centena >= 1 and dezena >= 1) and unidade >= 1:    print(', ', end='')

if (centena >= 1 and dezena >= 1) and unidade < 1:    print(' e ', end='')

if dezena == 1:      print('1 dezena', end='')
elif dezena > 1:    print(f'{dezena} dezenas', end='')

if (dezena >= 1 or centena >= 1) and unidade >= 1:    print(' e ', end='')

if unidade == 1:    print('1 unidade.')
elif unidade > 1:    print(f'{unidade} unidades.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# 
#     A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#     A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#     A mensagem "Aprovado com Distinção", se a média for igual a 10.

# In[ ]:


n1 = float(input('1ª Nota: '))
n2 = float(input('2ª Nota: '))
n3 = float(input('3ª Nota: '))

media = (n1 + n2 + n3) / 3

if media == 10:  print(f'Aprovado com Disntinção. Média: {media:.2f}')
elif media >= 7:  print(f'Aprovado. Média: {media:.2f}')
else:  print(f'Reprovado. Média: {media:.2f}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# 
#     Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#     Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

# In[ ]:


valor_saque = int(input('Valor do Saque: R$ '))

while valor_saque > 600 or valor_saque < 10:
    print('Valores deve ser entre R$ 10.00 e R$ 600.00')
    valor_saque = int(input('Valor do Saque: R$ '))

qtdNota100 = valor_saque // 100
qtdNota50 = (valor_saque % 100) // 50
qtdNota10 = (valor_saque % 50) // 10
qtdNota05 = (valor_saque % 10) // 5
qtdNota01 = (valor_saque % 5) // 1

print(f'Quantidade de Notas de R$ 100.00 = {qtdNota100}') if qtdNota100 >= 1 else ()
print(f'Quantidade de Notas de R$ 50.00 = {qtdNota50}') if qtdNota50 >= 1 else ()
print(f'Quantidade de Notas de R$ 10.00 = {qtdNota10}') if qtdNota10 >= 1 else ()
print(f'Quantidade de Notas de R$ 5.00 = {qtdNota05}') if qtdNota05 >= 1 else ()
print(f'Quantidade de Notas de R$ 1.00 = {qtdNota01}') if qtdNota01 >= 1 else ()


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

# In[ ]:


numero = int(input('Digite um número inteiro: '))
print('Par' if numero % 2 == 0 else 'Ímpar')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

# In[ ]:


numero = float(input('Digite um número inteiro: '))
print('Número Inteiro.' if numero == round(numero) else 'Número Decimal.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# 
#     par ou ímpar;    positivo ou negativo;    inteiro ou decimal. 

# In[ ]:


numero = float(input('Digite um número: '))
print('='*25,'\n1. Par ou Ímpar\n2. Positivo ou Negativo\n3. Inteiro ou Decimal\n', '='*25)

escolha = int(input('Escolha uma opção: '))

if escolha == 1:  print('Par' if numero % 2 == 0 else 'Ímpar')
elif escolha == 2:  print('Positivo' if numero >= 0 else 'Negativo')
elif escolha == 3:  print('Inteiro' if numero == round(numero) else 'Decimal')
else:  print('Escolha Inexistente.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# 
#     1. "Telefonou para a vítima?"
#     2. "Esteve no local do crime?"
#     3. "Mora perto da vítima?"
#     4. "Devia para a vítima?"
#     5. "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

# In[ ]:


print('Responda 1 para SIM ou 0 para NÃO.')
quest_1 = int(input('Telefonou para a Vítima? [0/1]: '))
quest_2 = int(input('Esteve no local do crime? [0/1]: '))
quest_3 = int(input('Mora perto da vítima? [0/1]: '))
quest_4 = int(input('Devia para a vítima? [0/1]: '))
quest_5 = int(input('Já trabalhou com a vítima? [0/1]: '))

total = quest_1 + quest_2 + quest_3 + quest_4 + quest_5

if total == 5:  print('Assassino!!')
elif total >= 3:  print('Cúmplice.')
elif total == 2:  print('Suspeito.')
else:  print('Inocente.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# 
#     Álcool:    até 20 litros, desconto de 3% por litro    acima de 20 litros, desconto de 5% por litro
#     Gasolina:    até 20 litros, desconto de 4% por litro    acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R 2,50 o preço do litro do álcool é R 1,90.

# In[ ]:


combustivel = str(input('[A] Álcool | [G] Gasolina: ')).upper()[0]

while combustivel not in 'AG':  
    print('Digite apenas [A] para Álcool ou [G] para Gasolina!')
    combustivel = str(input('[A] Álcool | [G] Gasolina: ')).upper()[0]

preçoGasolina = 2.5
preçoAlcool = 1.9

litro = float(input('Quantos litros? '))

if combustivel == 'A':
    if litro > 20:
        desconto = litro * 0.05    
    else:
        desconto = litro * 0.03
    preço = preçoAlcool
else:
    if litro > 20:
        desconto = litro * 0.06
    else:
        desconto = litro * 0.04
    preço = preçoGasolina

valor = litro * preço 
valor -= desconto

print(f'R$ {desconto:.2f} de desconto | Total: R$ {valor:.2f}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:<br>
#     ![27.jpg](attachment:27.jpg)<br>
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# In[ ]:


kgMorango = float(input('Quantidade [Kg] de Morango: '))
kgMaça = float(input('Quantidade [Kg] de Maça: '))

preçoMorango = 2.5 if kgMorango < 5 else 2.2
preçoMaça = 1.8 if kgMaça < 5 else 1.5

valor = (kgMorango * preçoMorango) + (kgMaça * preçoMaça)

if valor >= 25 or kgMaça + kgMorango >= 8:  valor -= (valor * 0.1)
else:  valor = valor  
print(f'R$ {valor:.2f}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:<br>
#     ![28.jpg](attachment:28.jpg)<br>
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

# In[ ]:


from time import sleep

print('-'*40)
print('Hipermercado Tabajara'.center(40))
print('-'*40)
print('\n\t\tAté 5Kg\t\tAcima de 5Kg')
print('1. Filé Duplo\tR$ 4.9 Kg\tR$ 5.8 Kg')
print('2. Alcatra\tR$ 5.9 Kg\tR$ 6.8 Kg')
print('3. Picanha\tR$ 6.9 Kg\tR$ 7.8 Kg')
print('\n'+'-'*40)
escolha = int(input('Escolha uma opção: '))

while escolha not in (1,2,3):
    escolha = int(input('Opção Inválida. Escolha uma opção: '))

if escolha == 1:
    carne = 'Filé Duplo'
elif escolha == 2:
    carne = 'Alcatra'
else:
    carne = 'Picanha'

qtd_kg = float(input(f'Quantos Kg de {carne}: '))

cartão_tabajara = False

pgt_cartão = str(input('Utilizará Cartão Tabajara? [S/N]: '))[0]
while pgt_cartão not in 'SsNn':
    pgt_cartão = str(input('Utilizará Cartão Tabajara? [S/N]: '))[0]

if pgt_cartão in 'Ss':    cartão_tabajara = True

print('\n\nGerando Cupom Fiscal .',end='')
for i in range(0, 15):
    if i == 14: 
        print('.')
    else:
        print('.',end='',flush=True)
    sleep(0.2)
print()

if escolha == 1:    preço = qtd_kg * 4.9 if qtd_kg <= 5 else qtd_kg * 5.8
elif escolha == 2:  preço = qtd_kg * 5.9 if qtd_kg <= 5 else qtd_kg * 6.8
else:  preço = qtd_kg * 6.9 if qtd_kg <= 5 else qtd_kg * 7.8

if cartão_tabajara == True:  desconto = preço * 0.1
else:  desconto = 0

print('-'*40)
print('Cupom Fiscal Hipermercado Tabajara'.center(40))
print('-'*40)
print(f'{qtd_kg}kg de {carne}: \t\tR$ {preço:.2f}')
print(f'Desconto Cartão Tabajara: \tR$ {desconto:.2f}')
print(f'Valor com Desconto: \t\tR$ {preço - desconto:.2f}')
print('-'*40)


# In[ ]:




