#!/usr/bin/env python
# coding: utf-8

# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# ![python-1536x650.png](attachment:python-1536x650.png)

# # <center> <u>Exercícios de Estrutura de Repetição Python
# <center><font color='#787878'>Exercícios disponíveis no link: https://wiki.python.org.br/EstruturaDeRepeticao, desenvolvidos por mim para aperfeiçoamento profissional.</font>

# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# In[ ]:


while True:
    nota = float(input('Informe uma nota [0 à 10]: '))
    if (nota <= 10) & (nota >= 0):
        break


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 

# In[ ]:


nomeUsuario = str(input('Informe o nome de usuário: ')).upper()
while True:
    senha = str(input('Informe a senha: ')).upper()
    if senha == nomeUsuario:
        print(f'A senha deve ser diferente de {nomeUsuario}')
    else:
        break


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>3. Faça um programa que leia e valide as seguintes informações:<br>
# a. Nome: maior que 3 caracteres;<br>
# b. Idade: entre 0 e 150;<br>
# c. Salário: maior que zero;<br>
# d. Sexo: 'f' ou 'm';<br>
# e. Estado Civil: 's', 'c', 'v', 'd';

# In[ ]:


while True:
    nome = str(input('Nome: '))
    if len(nome) < 3:
        print('O nome deve ter mais de 3 caracteres.')
    else:
        break

while True:
    idade = float(input('Idade [0 à 150]: '))
    if (idade <= 150) & (idade >= 0):
        break

while True:
    salario = float(input('Salário: R$ '))
    if salario > 0:
        break

while True:
    sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    if sexo in 'FM':
        break

while True:
    estadoCivil = str(input('Estado Civil [S/C/V/D]: ')).strip().upper()[0]
    if estadoCivil in 'SCVD':
        break


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

# In[ ]:


paisA = 80000
txCrescimentoPaisA = 1.03
paisB = 200000
txCrescimentoPaisB = 1.015
qtdAnos = 0

while paisA <= paisB:
    paisA *= txCrescimentoPaisA
    paisB *= txCrescimentoPaisB
    qtdAnos += 1

print(f'Em {qtdAnos} anos a população do País A ultrapassará a população do País B em {round(paisA - paisB, 0):.0f} pessoas.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

# In[ ]:


paisA = int(input('Quantidade de pessoas do País A: '))
txCrescimentoPaisA = float(input('Taxa de crescimento do País A [%]: '))
paisB = int(input('Quantidade de pessoas do País B: '))
txCrescimentoPaisB = float(input('Taxa de crescimento do País B [%]: '))
qtdAno = 0

while paisA <= paisB:
    paisA *= txCrescimentoPaisA
    paisB *= txCrescimentoPaisB
    qtdAnos += 1

print(f'Em {qtdAnos} anos a população do País A ultrapassará a população do País B em {round(paisA - paisB, 0):.0f} pessoas.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

# In[ ]:


for numero in range(1, 21):
    print(numero)

for numero in range(1, 21):
    print(numero, end=' ')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>7. Faça um programa que leia 5 números e informe o maior número.

# In[ ]:


maior = 0
for n in range(1, 6):
    numero = int(input(f'Digite o {n}º número: '))
    if numero > maior:
        maior = numero
print(f'O maior número é: {maior}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>8. Faça um programa que leia 5 números e informe a soma e a média dos números. 

# In[ ]:


soma = 0
for n in range(1, 6):
    numero = int(input(f'Digite o {n}º número: '))
    soma += numero

print(f'Soma: {soma}\nMédia: {soma/5}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50. 

# In[ ]:


for impares in range(1, 50, 2):
    print(impares, end=' ')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

# In[ ]:


n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número: '))

if n1 > n2:
    for i in range(n1+1, n2):
        print(i, end=' ')
elif n2 > n1:
    for i in range(n2-1, n1, -1):
        print(i, end=' ')
else:
    print('Não há intervalo. Números iguais.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>11. Altere o programa anterior para mostrar no final a soma dos números. 

# In[ ]:


n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número: '))
soma = 0

if n1 > n2:
    for i in range(n1+1, n2):
        print(i, end=' ')
        soma+=i
elif n2 > n1:
    for i in range(n2-1, n1, -1):
        print(i, end=' ')
        soma+=i
else:
    print('Não há intervalo. Números iguais.')
print(f'Soma: {soma}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:</b>
#     
# ![image.png](attachment:image.png)

# In[ ]:


while True:
    numero = int(input('Digite um valor entre 1 e 10: '))
    if (numero < 11) & (numero > 0):
        break

print(f'Tabuada de {numero}:')
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

# In[ ]:


base = int(input('Informe o valor da base: '))
expoente = int(input('Informe o valor do expoente: '))

valor = 1
for i in range(1, expoente + 1):
    if i == expoente:
        print(f'{base}', end=' = ')
    else:
        print(f'{base} x ', end='')
    valor *= base

print(valor)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

# In[ ]:


pares = impares = 0
for i in range(1, 11):
    n = int(input(f'{i}º Valor: '))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Pares: {pares} | Ímpares: {impares}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

# In[ ]:


termo = int(input('Qual termo? '))
a = 0
b = 1

print(a, b, end=' ')
for i in range(1, termo+1):
    c = a + b
    print (c, end= ' ')
    a = b
    b = c


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>16. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

# In[ ]:


a = 0
b = 1
c = a + b
print(a, b, end=' ')

while c < 500:
    print(c, end=' ')
    a = b
    b = c
    c = a + b


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

# In[ ]:


n = int(input('Digite o valor: '))

print(f'{n}! = {n}', end=' ')
for i in range(n - 1, 0, -1):
    print(f'x {i}', end=' ')
    n *= i

print(f'= {n}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

# In[ ]:


while True:
    n = int(input('Digite o valor: '))
    if (n < 1000) & (n > 0):
        break

print(f'{n}! = {n}', end=' ')
for i in range(n - 1, 0, -1):
    print(f'x {i}', end=' ')
    n *= i

print(f'= {n}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

# In[ ]:


while True:
    n = float(input('Digite um número: '))

    while (n > 15 or n < 2) or round(n) != n:
        print('Só é permitido números inteiros entre 1 e 16.')
        n = float(input('Digite um número: '))

    n = int(n)
    print(f'{n}! = {n}', end='')

    valor = 1
    for i in range(n - 1, 0, -1):
        if i == 1:
            print(f' x {i} = ', end='')
        else:
            print(f' x {i}', end='')
        valor *= n

    print(valor)

    resp = str(input('Novamente? [S/N]: ')).upper()[0]
    if resp == 'N':
        break


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

# In[ ]:


n = int(input('Número: '))

qtd = 0
for i in range(1, n+1):
    if n % i == 0:
        qtd += 1

if qtd > 2:
    print('Não é Primo.')
else:
    print('É primo.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

# In[ ]:


n = int(input('Número: '))

lista_primos = []
qtd = 0
for i in range(1, n+1):
    if n % i == 0:
        qtd += 1
        lista_primos.append(i)

if n == 1 or n == 0:
    print('Primo.')
else:
    if qtd > 2:
        print('Não é Primo.')
        print(f'Divísivel por {lista_primos}')
    else:
        print('É primo.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

# In[ ]:


n = int(input('Digite um número: '))

qtd = 0
lista_primos = list()

for i in range(1, n + 1):
    if n % i == 0:
        lista_primos.append(i)
    qtd += 1

if qtd > 2:
    print('Não é Primo.')
    print(f'Quantidade de Execuções: {qtd}')
    print(f'Lista de Números Divisíveis: {lista_primos}')
else:
    print('Primo.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>24. Faça um programa que calcule o mostre a média aritmética de N notas.

# In[ ]:


contador = soma = 0
while True:
    contador += 1
    nota = float(input(f'{contador}ª Nota: '))
    soma += nota
    resp = str(input('Inserir outra nota? [S/N]: ')).upper()[0]
    if resp == 'N':
        break

print(f'Média: {soma/contador}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>25. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

# In[ ]:


contador = soma_idade = 0

while True:
    contador += 1
    idade_pessoa = int(input('Digite sua idade: '))
    soma_idade += idade_pessoa

    resp = str(input('Continuar? ["N" - SAIR]: ')).upper()[0]
    if resp == 'N':
        break

media_idade = soma_idade / contador
if media_idade > 60:
    print('Turma Idosa.')
elif media_idade > 26:
    print('Turma Adulta.')
else:
    print('Turma Jovem.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

# In[ ]:


import time

qtd_eleitores = int(input('Quantidade de Eleitores: '))
while qtd_eleitores <= 0:
    qtd_eleitores = int(
        input('Quantidade de Eleitores deve ser maior do que 0. Tente Novamente: '))

print('Carregando Urna.', end='')
for i in range(0, 7):
    if i == 9:
        print('.')
    else:
        print('.', end='', flush=True)
    time.sleep(0.1)

print('\n\n\n')

print('='*40)
print('URNA ELETRÔNICA BRASIL 2022'.center(40))
print('='*40)
print('\tNº\tCANDIDATO')
print('\t1\tZezinho da Esquina')
print('\t2\tWalter em nome de Deuxxx!')
print('\t3\tFrancisquinho da Ordem')
print('\t4\tClaudiomiro Bezerra')
print('\t0\tBranco')
print('='*40)

candidato_1 = candidato_2 = candidato_3 = candidato_4 = branco = nulo = 0

for i in range(1, qtd_eleitores + 1):
    voto = int(input(f'{i}º Eleitor - Escolha um candidado: '))
    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1
    elif voto == 4:
        candidato_4 += 1
    elif voto == 0:
        branco += 1
    else:
        nulo += 1

if candidato_1 > candidato_2 and candidato_1 > candidato_3 and candidato_1 > candidato_4:
    vencedor = 'Zezinho da Esquina'
if candidato_2 > candidato_1 and candidato_2 > candidato_3 and candidato_2 > candidato_4:
    vencedor = 'Walter em nome de Deuxxx!'
if candidato_3 > candidato_2 and candidato_3 > candidato_1 and candidato_3 > candidato_4:
    vencedor = 'Francisquinho da Ordem'
if candidato_4 > candidato_2 and candidato_4 > candidato_3 and candidato_4 > candidato_1:
    vencedor = 'Claudiomiro Bezerra'
if candidato_1 == candidato_2 == candidato_3 == candidato_4 == 0:
    vencedor = 'ELEIÇÃO ANULADA'


print('Carregando Resultado da Eleição.', end='')
for i in range(0, 7):
    if i == 9:
        print('.')
    else:
        print('.', end='', flush=True)
    time.sleep(0.25)

print('\n\n\n')
print('='*40)
print('RESULTADO ELEIÇÃO BRASIL 2022'.center(40))
print('='*40)
print('CANDIDATO\t\tQTD DE VOTOS')
print(f'Zezinho da Esquina\t\t {candidato_1}')
print(f'Walter em nome de Deuxxx!\t {candidato_2}')
print(f'Francisquinho da Ordem\t\t {candidato_3}')
print(f'Claudiomiro Bezerra\t\t {candidato_4}')
print(f'BRANCO\t\t\t\t {branco}')
print(f'NULO\t\t\t\t {nulo}')
print('='*40)
print(f'Presidente Eleito: {vencedor}'.center(40))
print('='*40)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>27. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

# In[ ]:


soma_alunos = 0

qtd_turmas = int(input('Quantas turmas? '))
while qtd_turmas <= 0:
    qtd_turmas = int(input('Quantas turmas? '))

for i in range(1, qtd_turmas + 1):
    alunos = int(input(f'Quantidade de Alunos da {i}ª Turma: '))
    soma_alunos += alunos

print(f'O colégio tem {qtd_turmas} turmas e a média de alunos é {soma_alunos/qtd_turmas:.1f}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

# In[ ]:


qtd_cds = int(input('Qual é a quantidade de CDs? '))
valor_medio = float(input('Valor médio gasto em cada CD? R$ '))

print(f'O colecionador tem {qtd_cds}, que custam em média R$ {valor_medio:.2f} cada um.')
print(f'Estima-se que sua coleção valha R$ {qtd_cds * valor_medio:.2f}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>29. O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:</b>
#     
# ![image.png](attachment:image.png)

# In[ ]:


print('='*40)
print('Loja Quase Dois - Tabela de Preços'.center(40))
print('='*40)

for i in range(1, 51):
    print(f'{i}\t\t|\t\tR$ {i * 1.99:.2f}')
    print('-'*40)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>30. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:</b>
# 
# ![image.png](attachment:image.png)

# In[ ]:


preço_pão = float(input('Preço do Pão: R$ '))
while preço_pão <= 0:
    preço_pão = float(input('Preço do Pão: R$ '))

print('='*50)
print('Panificadora Pão de Ontem - Tabela de Preços'.center(50))
print('='*50)

for i in range(1, 51):
    print(f'{i}\t\t\t|\t\tR$ {preço_pão * i:.2f}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>31. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:</b>
#     
#     
# ![image.png](attachment:image.png)

# In[ ]:


lista_preços = list()
preço = float(input('Valor [0 - SAIR]: R$ '))

while preço != 0:
    lista_preços.append(preço)
    preço = float(input('Valor [0 - SAIR]: R$ '))

contador = total = 0

print('-'*30)
print('Lojas Tabajara'.center(30))
print('-'*30)


for produto in lista_preços:
    if contador == len(lista_preços) - 1:
        print(f'Produto {contador + 1}\t\t\tR$ {lista_preços[contador]:.2f}')
        print('-'*30)
    else:
        print(f'Produto {contador + 1}\t\t\tR$ {lista_preços[contador]:.2f}')
        print('.'*30)
    total += lista_preços[contador]
    contador += 1


print(f'Total:\t\t\t\tR$ {total:.2f} ')
print('-'*30)

if contador != 0:
    pagamento = float(input('Valor Pagamento R$: '))
    while pagamento < total:
        pagamento = float(input(f'Faltam R$ {total-pagamento:.2f} Pagamento R$: '))

    if pagamento > total:
        print(f'Troco: R$ {pagamento - total:.2f}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:</b>
# 
# ![image.png](attachment:image.png)

# In[ ]:


numero = int(input('Fatorial de: '))

print(f'{numero}! = {numero}',end='')
for i in range(numero - 1, 0, -1):
    print(f' . {i}',end='')
    numero *= i

print(f' = {numero}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

# In[ ]:


temp = float(input('Temperatura [1000 - SAIR]: '))
menor = maior = total = temp
qtd = 0
while temp != 1000:
    qtd += 1
    if temp > maior:    maior = temp
    if temp < menor:    menor = temp
    total += temp
    temp = float(input('Temperatura [1000 - SAIR]: '))

print(f'A maior temperatura registrada foi de {maior}ºC.')
print(f'A menor temperatura registrada foi de {menor}ºC.')
print(f'A média registrada foi de {total/qtd:.2f}ºC.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>34. Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

# In[ ]:


temp = float(input('Temperatura [1000 - SAIR]: '))
menor = maior = total = temp
qtd = 0
while temp != 1000:
    qtd += 1
    if temp > maior:    maior = temp
    if temp < menor:    menor = temp
    total += temp
    temp = float(input('Temperatura [1000 - SAIR]: '))

print(f'A maior temperatura registrada foi de {maior}ºC.')
print(f'A menor temperatura registrada foi de {menor}ºC.')
print(f'A média registrada foi de {total/qtd:.2f}ºC.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>35. Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

# In[ ]:


numero = int(input('Digite um número inteiro: '))

qtd = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        qtd += 1

if qtd != 2 or numero == 1 or numero == 0:
    if numero == 1 or numero == 0:
        print(f'{numero} NÃO é Primo.')
    else:
        print(f'{numero} NÃO é Primo. Ele é divisível {qtd} vezes.')
else:
    print(f'{numero} é Primo.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>36. Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:</b>
#     
# ![image.png](attachment:image.png)
# 
# <b>Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.<b/>

# In[ ]:


numero = int(input('Montar a tabuada do: '))
inicio = int(input('Começar por: '))
fim = int(input('Termina em: '))

while fim <= inicio:
    fim = int(input(f'Deve terminar em pelo menos {inicio + 1}. Então, termina em? '))

print(f'\nVou montar a tabuada do {numero} começando em {inicio} e terminando em {fim}: ')
for i in range(inicio, fim + 1):
    print(f'{numero} x {i} = {numero * i}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>37. Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

# In[ ]:


maior_peso = menor_peso = total_peso = maior_altura = menor_altura = total_altura = total_cliente = 0
cliente_maior_peso = cliente_menor_peso = cliente_maior_altura = cliente_menor_altura = ''

while True:
    codigo = str(input('Código do Cliente [0 - SAIR]: '))
    if codigo == '0':
        break

    peso = float(input(f'Peso do Cliente [{codigo}]: '))
    altura = float(input(f'Altura do Cliente [{codigo}]: '))

    if maior_peso == 0:
        maior_peso = peso
        cliente_maior_peso = codigo
    else:
        if peso > maior_peso:
            maior_peso = peso
            cliente_maior_peso = codigo

    if maior_altura == 0:
        maior_altura = altura
        cliente_maior_altura = codigo
    else:
        if altura > maior_altura:
            maior_altura = altura
            cliente_maior_altura = codigo

    if menor_peso == 0:
        menor_peso = peso
        cliente_menor_peso = codigo
    else:
        if peso < menor_peso:
            menor_peso = peso
            cliente_menor_peso = codigo

    if menor_altura == 0:
        menor_altura = altura
        cliente_menor_altura = codigo
    else:
        if altura < menor_altura:
            menor_altura = altura
            cliente_menor_altura = codigo

    print('-' * 35)
    total_altura += altura
    total_peso += peso
    total_cliente += 1

print('='*35)

print(f'{cliente_maior_altura} é o Cliente mais Alto com {maior_altura:.2f}m')
print(f'{cliente_menor_altura} é o Cliente mais Baixo com {menor_altura:.2f}m')

print(f'{cliente_maior_peso} é o Cliente mais Pesado com {maior_peso:.2f}Kg')
print(f'{cliente_menor_peso} é o Cliente mais Leve com {menor_peso:.2f}Kg')

print(f'A Academia possui {total_cliente} clientes.')
print(f'A média de altura é de {total_altura/total_cliente:.2f}m')
print(f'A média de peso é de {total_peso/total_cliente:.2f}Kg')

print('='*35)


# In[ ]:





# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>38. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:<br>
# a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;<br>
# b. Em 1996 recebeu aumento de 1,5 por cento sobre seu salário inicial;<br>
# c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

# In[ ]:


aumento = 0.15
salario = float(input('Informe o salário inicial do funcionário:'))

for i in range(1996, 2022):
    salario += (salario * aumento)
    print(f'Ano: {i} Valor: R$ {aumento}')
    aumento *= 2
    
print(f'R$ {salario:.2f}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>39. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

# In[ ]:


alto = baixo = cod_alto = cod_baixo = 0

for i in range(1, 11):
    cod = int(input(f'Código do {i}º Aluno: '))
    alt = float(input(f'Altura em cm do {i}º Aluno: '))

    if alto == 0:
        alto = alt
        cod_alto = cod
    else:
        if alt > alto:
            alto = alt
            cod_alto = cod

    if baixo == 0:
        baixo = alt
        cod_baixo = cod
    else:
        if alt < baixo:
            baixo = alt
            cod_baixo = cod

print(f'Aluno Mais Alto: {cod_alto} com {alto} centímetros.')
print(f'Aluno Mais Baixo: {cod_baixo} com {baixo} centímetros.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>40. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:<br>
# a. Código da cidade;<br>
# b. Número de veículos de passeio (em 1999);<br>
# c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:<br>
# d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;<br>
# e. Qual a média de veículos nas cinco cidades juntas;<br>
# f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

# In[ ]:


maior_indice = menor_indice = total_acidentes = total_veiculos = 0
cidade_maior_indice = cidade_menor_indice = cidades_com_menos_2000 = 0

for i in range(1, 6):
    cod = str(input(f'Nome da {i}ª Cidade: ')).title()
    veiculos = int(input(f'Número de Veículos da {i}ª Cidade: '))
    acidentes = int(input(f'Número de Acidentes com Vítimas em {cod}: '))

    indice = (acidentes / veiculos) * 100

    if maior_indice == 0:
        maior_indice = indice
        cidade_maior_indice = cod
    else:
        if indice > maior_indice:
            maior_indice = indice
            cidade_maior_indice = cod

    if menor_indice == 0:
        menor_indice = indice
        cidade_menor_indice = cod
    else:
        if indice < menor_indice:
            menor_indice = indice
            cidade_menor_indice = cod

    total_veiculos += veiculos
    if veiculos < 2000:
        total_acidentes += indice
        cidades_com_menos_2000 += 1

    print('='*50)

print('Gerando Relatório')
print(f'Cidade com Maior Índice de Acidentes: {cidade_maior_indice} com {maior_indice:.2f}%')
print(f'Cidade com Menor Índice de Acidentes: {cidade_menor_indice} com {menor_indice:.2f}%')
print(f'Total de veículos das 5 cidades: {total_veiculos}')
print(f'Média de acidentes em cidades com menos de 2000 veículos: {total_acidentes/cidades_com_menos_2000:.2f}%')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>41. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
#     
# ![image.png](attachment:image.png)

# In[ ]:


divida = float(input('Valor da dívida: R$ '))

print('Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela')
for i in range(1, 15, 3):
    if i == 1:
        juros = 0
        print(f'R$ {divida:.2f}\t\t{juros * divida:.2f}\t\t\t{i}\t\tR$ {((divida+juros) / i):.2f}')
    elif i == 4:
        juros = 0.1
        parcela = (divida + (juros * divida)) / (i-1)
        print(f'R$ {divida:.2f}\t\t{juros * divida:.2f}\t\t\t{i - 1}\t\tR$ {parcela:.2f}')
    else:
        juros += 0.05
        parcela = (divida + (juros * divida)) / (i-1)
        print(f'R$ {divida:.2f}\t\t{juros * divida:.2f}\t\t\t{i - 1}\t\tR$ {parcela:.2f}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>42. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

# In[ ]:


l1 = l2 = l3 = l4 = 0
while True:
    n = int(input('Digite um número [-1 para SAIR]: '))

    if n < 0:        break

    if n <= 25:        l1 += 1
    elif n <= 50:        l2 += 1
    elif n <= 75:        l3 += 1
    elif n <= 100:        l4 += 1

print(f'Números entre 0 e 25: {l1}')
print(f'Números entre 26 e 50: {l2}')
print(f'Números entre 51 e 75: {l3}')
print(f'Números entre 76 e 100: {l4}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>43. O cardápio de uma lanchonete é o seguinte:
#     
# ![image.png](attachment:image.png)
#     
# <br>Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

# In[ ]:


import time as tm

dict_cardapio = {
    100: ('Cachorro-Quente', 1.2),
    101: ('Bauru Simples', 1.3),
    102: ('Bauru com Ovo', 1.5),
    103: ('Hamburguer', 1.2),
    104: ('Cheeseburguer', 1.3),
    105: ('Refrigerante', 1.5)}

lista_pedido = []

print('='*40)
print('LANCHONETE CACHORRO LOKO'.center(40))
print('='*40)
print('  Lanche'.rjust(5) + 'Código'.rjust(15) + 'Preço'.rjust(15))
print('-'*40)
print('Cachorro-Quente'.rjust(5) + '100'.rjust(7) + 'R$ 1,20'.rjust(17))
print('Bauru Simples'.rjust(5) + '101'.rjust(9) + 'R$ 1,30'.rjust(17))
print('Bauru com Ovo'.rjust(5) + '102'.rjust(9) + 'R$ 1,50'.rjust(17))
print('Hamburguer'.rjust(5) + '103'.rjust(12) + 'R$ 1,20'.rjust(17))
print('Cheeseburguer'.rjust(5) + '104'.rjust(9) + 'R$ 1,30'.rjust(17))
print('Refrigerante'.rjust(5) + '105'.rjust(10) + 'R$ 1,50'.rjust(17))
print('-'*40)
print()

total = 0

while True:
    lista_codigo = []
    codigo = int(input('Digite o código do produto [0 - SAIR]: '))
    while codigo != 0 and (codigo < 100 or codigo > 105):
        codigo = int(
            input('Código Inexistente. Digite o código do produto [0 - SAIR]: '))
    if codigo == 0:
        break

    quantidade = int(input(f'Quantos {dict_cardapio[codigo][0]}? '))
    valor = dict_cardapio[codigo][1] * quantidade

    lista_codigo.append(dict_cardapio[codigo][0])
    lista_codigo.append(quantidade)
    lista_codigo.append(valor)

    lista_pedido.append(lista_codigo)
    print('.'*40)

print('\n\n\n')
print('Gerando Pedido.')
for i in range(0, 41):
    if i == 40:
        print('.')
    else:
        print('.', end='', flush=True)
    tm.sleep(0.09)

for elemento in lista_pedido:
    print(f'{elemento[0]} - R$ {elemento[2]:.2f}')
    total += elemento[2]

    print('.'*40)
print(f'Valor Total: R$ {total:.2f}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>44. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 
# ![image.png](attachment:image.png)
#     
# <br>Faça um programa que calcule e mostre:<br>
# a. O total de votos para cada candidato;<br>
# b. O total de votos nulos;<br>
# c. O total de votos em branco;<br>
# d. A percentagem de votos nulos sobre o total de votos;<br>
# e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>45. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:<br>
# a. Maior e Menor Acerto;<br>
# b. Total de Alunos que utilizaram o sistema;<br>
# c. A Média das Notas da Turma.<br>
#     
# ![image.png](attachment:image.png)
# 
# <br>Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

# In[ ]:


mais_votos = 0
vencedor = ''
total_votos = 0
lista_candidatos = [['Zezinho da Esquina', 1, 0], ['Walter de Deuxx!', 2, 0], ['Cândida Amada', 3, 0], [
    'Doutor Izaquias', 4, 0], ['Voto Nulo', 5, 0], ['Voto Branco', 6, 0]]

print('¨'*40)
print('Eleição Presidencial 2022'.center(40))
print('¨'*40)
print('  Candidato'.ljust(20) + 'Código'.rjust(15))
print('¨'*40)
for candidato in lista_candidatos:
    print(f'{candidato[0]}'.ljust(20) + f'{candidato[1]}'.rjust(13))
print('¨'*40)

while True:
    codigo = int(input('Qual Candidato?  [0 - SAIR]: '))

    while codigo > 7 or codigo < 0:
        codigo = int(input('Inválido. Tente Novamente [0 - SAIR]: '))

    if codigo == 0:
        break
    else:
        lista_candidatos[codigo-1][2] += 1
        total_votos += 1

print('¨'*40)
print('Eleição Presidencial 2022'.center(40))
print('¨'*40)

for candidato in lista_candidatos:
    print(f'{candidato[0]}'.ljust(20) + f'{candidato[2]}' +
          f'{(candidato[2]/total_votos)*100:.2f}%'.rjust(18))
    if candidato[1] < 5:
        if candidato[2] > mais_votos:
            vencedor = candidato[0]
            mais_votos = candidato[2]
print('¨'*40)

print(f'Presidente Eleito: {vencedor} com {mais_votos} votos.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>46. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# 
# ![image.png](attachment:image.png)

# In[ ]:


lista_atletas = []
ls = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
atleta = 0

while True:
    lista_saltos = []
    nome = str(input('Nome do Atleta [Deixe em branco para sair]: ')).title().strip()

    if nome == '':
        break

    for salto in range(1, 6):
        s = float(input(f'Distância do {salto}º salto: '))
        lista_saltos.append(s)

    print()
    print('-'*40)
    print('Resultado'.center(40))
    print('-'*40)
    print(f'Atleta:\t\t{nome}\n')
    for salto in range(0, 5):
        print(f'{ls[salto]} Salto:\t\t{lista_saltos[salto]} m.')

    print(f'Melhor Salto:\t\t{max(lista_saltos)} m.')
    print(f'Pior Salto:\t\t{min(lista_saltos)} m.')

    lista_saltos.pop(lista_saltos.index(max(lista_saltos)))
    lista_saltos.pop(lista_saltos.index(min(lista_saltos)))

    media = 0
    for salto in lista_saltos:
        media += salto

    print(f'Média dos saltos:\t{media/3:.1f} m.')
    lista_saltos.append(media/3)
    lista_saltos.append(nome)
    lista_atletas.append(lista_saltos)

    print(
        f'Resultado Final:\n\t{lista_atletas[atleta][4]}: {lista_atletas[atleta][3]:.1f} m.')
    atleta += 1
    print('='*40)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>47. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
#     
# ![image.png](attachment:image.png)

# In[ ]:


lista_atleta = []

nome = str(input('Nome do atleta: ')).title().strip()
while len(nome) < 3:
    nome = str(input('Nome do atleta: ')).title().strip()

for i in range(1, 8):
    nota = float(input(f'Nota {i}º Jurado: '))
    lista_atleta.append(nota)


print(f'\n\n\nAtleta:\t {nome}')
for nota in lista_atleta:
    print(f'Nota:\t {nota}')

print('\nResultado Final:\n')
print(f'Atleta:\t {nome}')
print(f'Melhor Nota: {max(lista_atleta)}')
print(f'Pior Nota: {min(lista_atleta)}')

lista_atleta.pop(lista_atleta.index(max(lista_atleta)))
lista_atleta.pop(lista_atleta.index(min(lista_atleta)))
print(sum(lista_atleta))
print(f'Média: {sum(lista_atleta) / 5:.2f}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>48. Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:
#     
# ![image.png](attachment:image.png)

# In[ ]:


def isnumber(value):
    try:
        int(value)
    except ValueError:
        return False
    return True

numero = str(input('Digite um número inteiro positivo: '))

while isnumber(numero) == False or int(numero) < 0:
    print(
        'O número deve ser \033[1;31mINTEIRO\033[m e \033[1;31mPOSITIVO\033[m.')
    numero = str(input('Digite um número: '))

print(f'{numero} => {numero[::-1]}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>49. Faça um programa que mostre os n termos da Série a seguir:
# 
# ![image.png](attachment:image.png)
#     
# <br>Imprima no final a soma da série

# In[ ]:


lista_numerador = []
lista_denominador = []
lista_mmc = []
lista_soma = []

termos = int(input('Quantos termos? '))

m = 1
for n in range(1, termos + 1):
    if n == termos:
        print(f'{n}/{m}', end=' = ')
    else:
        print(f'{n}/{m} + ', end='')
    lista_numerador.append(n)
    lista_denominador.append(m)
    m += 2

# CRIA UMA CÓPIA DA LISTA DE DENOMINADORES PARA VERIFICAÇÂO POSTERIOR
lista_denominador_secundaria = lista_denominador.copy()

# VERIFICA SE A DIVISÂO É EXATA E SUBSTITUI A LISTA DE DENOMINADORES SECUNDARIA POR 1.
for i in range(0, len(lista_denominador)):
    for divisor in range(3, max(lista_denominador_secundaria)+3, 2):
        if lista_denominador_secundaria[i] % divisor == 0:
            lista_mmc.append(divisor)
            lista_denominador_secundaria[i] = round(
                lista_denominador[i] / divisor)

mmc = 1
for elemento in lista_mmc:
    mmc *= elemento

# CALCULA OS NUMERADORES (DIVIDE PELO DE BAIXO | MULTIPLICA PELO DE CIMA)
for i in range(0, len(lista_denominador)):
    x = (mmc / lista_denominador[i]) * lista_numerador[i]
    lista_soma.append(x)

print(f'{sum(lista_soma):.0f}/{mmc}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>50. Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

# In[ ]:


qtd_termos = int(input('Quantidade de termos: '))
valorH = 0

for i in range(1, qtd_termos + 1):
    if i == 1:
        print(i, end=' + ')
    elif i == qtd_termos:
        print(f'1/{i}', end=' = ')
    else:
        print(f'1/{i}', end=' + ')
    valorH += (1 / i)

print(round(valorH, 2))


# <b><center>-------------------------------------------------------------------------------------------------------------------------------
