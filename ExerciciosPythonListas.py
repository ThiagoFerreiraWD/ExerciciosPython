#!/usr/bin/env python
# coding: utf-8

# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# ![python-1536x650.png](attachment:python-1536x650.png)

# # <center> <u>Exercícios com Listas Python
# <center><font color='#787878'>Exercícios disponíveis no link: https://wiki.python.org.br/ExerciciosListas, desenvolvidos por mim para aperfeiçoamento profissional.</font>

# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

# In[ ]:


vetor = []

for numero in range(1,6):
    vetor.append(float(input(f'Informe o {numero}º Número: ')))

print(vetor)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

# In[ ]:


vetor = []

for numero in range(1,4):
    vetor.append(float(input(f'Informe o {numero}º Número: ')))

vetor.reverse()
print(vetor)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

# In[ ]:


listaNotas = list()

for i in range(1, 5):
    nota = float(input(f'Nota da P{i}: '))
    listaNotas.append(nota)

print(f'Notas: {listaNotas} | Média: {sum(listaNotas)/len(listaNotas)}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

# In[ ]:


listaConsoantes = list()
total = 0

sequencia = str(input('Digite uma sequência de 10 caracteres: ')).upper().strip()
while len(sequencia) != 10:
    sequencia = str(input(
        f'{sequencia} tem {len(sequencia)} caracteres. Digite uma sequência de 10 caracteres: ')).upper().strip()

for caracter in sequencia:
    if caracter not in 'AEIOU':
        total += 1
        if caracter not in listaConsoantes:
            listaConsoantes.append(caracter)

print(f'Total de listaConsoantesntes: {total}')
print(f'listaConsoantesantes: {listaConsoantes}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

# In[ ]:


import random as rd

listaNumeros = list()
listaPares = list()
listaImpares = list()

i = 0
while i != 20:
    n = rd.randint(0, 99)
    if n not in listaNumeros:
        listaNumeros.append(n)
        i += 1

for numero in listaNumeros:
    if numero % 2 == 0:
        listaPares.append(numero)
    else:
        listaImpares.append(numero)

print(f'Lista Geral: {listaNumeros}')
print(f'Lista Pares: {listaPares}')
print(f'Lista Ímpares: {listaImpares}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

# In[ ]:


listaGeral = list()

for aluno in range(1, 11):
    listaAluno = list()
    nomeAluno = str(input(f'\nDigite o nome do {aluno}º Aluno: ')).title()
    for nota in range(1, 5):
        nota = float(input(f'P{nota} de {nomeAluno}: '))
        listaAluno.append(nota)
    listaAluno.append(sum(listaAluno) / len(listaAluno))
    listaAluno.append(nomeAluno)
    listaGeral.append(listaAluno)

print('-'*35)
print('Alunos com Média Superior à 7.0'.center(35))
print('-'*35)
for aluno in listaGeral:
    if aluno[4] >= 7:
        print(f'{aluno[5]}. Média: {aluno[4]}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

# In[ ]:


listaNumeros = list()

for i in range(1, 6):
    n = int(input(f'{i}º Valor: '))
    listaNumeros.append(n)

soma = 0
multiplicação = 1

for numero in listaNumeros:
    soma += numero
    multiplicação *= numero

print(f'\nListagem: {listaNumeros}')
print(f'Soma: {soma} | Multiplicação: {multiplicação}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

# In[ ]:


listaPeso = list()
listaAltura = list()

for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}ª Pessoa: '))
    listaPeso.append(peso)
    altura = float(input(f'Altura da {pessoa}ª Pessoa: '))
    listaAltura.append(altura)

for pessoa in range(4, -1, -1):
    print(f'{pessoa+1}ª Pessoa')
    print(f'Peso: {listaPeso[pessoa]} kg.')
    print(f'Altura: {listaAltura[pessoa]} m.\n')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

# In[ ]:


listaNumeros = list()

for numero in range(1, 11):
    n = int(input(f'{numero}º Número: '))
    listaNumeros.append(n)

for numero in listaNumeros:
    print(f'{numero}² = {pow(numero, 2)}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

# In[ ]:


lista1 = list()
lista2 = list()
listaFinal = list()

for i in range(1, 3):
    print(f'\n{i}ª Lista'.center(20))
    for numero in range(1, 11):
        n = int(input(f'{numero}º Número: '))
        lista1.append(n) if i == 1 else lista2.append(n)

for numero in range(0, 10):
    listaFinal.append(lista1[numero])
    listaFinal.append(lista2[numero])

print(listaFinal)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

# In[ ]:


lista1 = list()
lista2 = list()
lista3 = list()
listaFinal = list()

for lista in range(1, 4):
    print(f'{lista}ª Lista'.center(20))
    for numero in range(1, 11):
        n = int(input(f'{numero}º Número: '))
        if lista == 1:
            lista1.append(n)
        elif lista == 2:
            lista2.append(n)
        else:
            lista3.append(n)
    print('-'*20)

for numero in range(0, 10):
    listaFinal.append(lista1[numero])
    listaFinal.append(lista2[numero])
    listaFinal.append(lista3[numero])

print(listaFinal)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

# In[ ]:


import random as rd

listaAlunos = list()

for aluno in range(0, 30):
    listaTemp = []
    idade = rd.randint(9, 16)
    altura = rd.uniform(1, 2)
    listaTemp.append(idade)
    listaTemp.append(round(altura, 2))
    listaAlunos.append(listaTemp)

somaAltura = qtdAlunos = 0
for altura in listaAlunos:
    somaAltura += altura[1]

media_altura = somaAltura/len(listaAlunos)
print(f'Média de Altura da Turma: {media_altura:.2f} m.')

for aluno in listaAlunos:
    if aluno[1] <= media_altura and aluno[0] >= 13:
        qtdAlunos += 1
        print(f'Idade: {aluno[0]} | Altura: {aluno[1]}')
print(f'Total: {qtdAlunos} alunos.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>13. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

# In[ ]:


listaMes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

listaTemperatura = list()

for i in range(0, 12):
    temp = float(input(f'Temperatura de {listaMes[i]}: '))
    listaTemperatura.append(temp)

mediaAnualTemperatura = sum(listaTemperatura) / len(listaTemperatura)
print(f'\nMédia Anual: {mediaAnualTemperatura:.2f}º C.')
print('Meses Superiores à Média Anual: ')
for temp in range(0, 12):
    if listaTemperatura[temp] >= mediaAnualTemperatura:
        print(f'Mês: {listaMes[temp]}'.ljust(
            15) + f' - Temperatura: {listaTemperatura[temp]:.2f}º C.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#     
#     
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?" 
# 
# 
# <b>O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

# In[ ]:


listaPerguntas = ['Telefonou para a Vítima? ', 'Esteve no local do crime? ',
                  'Mora perto da vítima? ', 'Devia dinheiro para a vítima? ', 
                  'Já trabalhou com a vítima? ']

totalSIM = 0
for pergunta in listaPerguntas:
    resposta = str(input(pergunta+'[S/N]: ')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input(pergunta+'[S/N]: ')).upper().strip()[0]
    if resposta == 'S':
        totalSIM += 1

if totalSIM == 5:    print('Assassino!!')
elif totalSIM >= 3:    print('Cúmplice!')
elif totalSIM == 2:    print('Suspeita.')
else:    print('Inocente.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#     
#     
# a. Mostre a quantidade de valores que foram lidos;<br>
# b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;<br>
# c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;<br>
# d. Calcule e mostre a soma dos valores;<br>
# e. Calcule e mostre a média dos valores;<br>
# f. Calcule e mostre a quantidade de valores acima da média calculada;<br>
# g. Calcule e mostre a quantidade de valores abaixo de sete;
# 
#     
# <b>Encerre o programa com uma mensagem;

# In[ ]:


import time

listaValores = list()

while True:
    valor = str(input('Informe um valor: '))

    try:
        valor = int(valor)
        if valor == -1:
            break
        else:
            listaValores.append(valor)
    except ValueError:
        print('Valor Inválido!')


print('\nGerando Relatório.', end='')
for i in range(3, 10):
    print('.\n' if i == 9 else '.', end='', flush=True)
    time.sleep(0.19)

print('-'*65)
print('Relatório'.center(65))
print('-'*65)
print('Quantidade de Valores Inputados:' + f' {len(listaValores)}'.rjust(5))
print('Valores em Ordem de Inserção: ', end='')
for valor in listaValores:
    print(valor, end=' ')
listaValores.reverse()
print('\nValores em Ordem de Invertida: ', end='')
for valor in listaValores:
    print(valor, end=' ')
print(f'\nSoma dos Valores: {sum(listaValores)}')
print(f'Média dos Valores: {sum(listaValores)/len(listaValores):.2f}')
print(f'Valores acima da média: ', end='')
for valor in listaValores:
    if valor >= (sum(listaValores)/len(listaValores)):
        print(valor, end=' ')
print(f'\nValores maiores do que 7: ', end='')
for valor in listaValores:
    if valor <= 7:
        print(valor, end=' ')
print()
print('-'*65)

print('\nFinalizando Relatório.', end='')
for i in range(3, 10):
    print('.\n' if i == 9 else '.', end='', flush=True)
    time.sleep(0.19)
print('Aplicação Encerrada!')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>16. Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe 200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de 3000 em uma semana recebe 200 mais 9 por cento de 3000, ou seja, um total de 470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# 
# 
# a. 200 - 299<br>
# b. 300 - 399<br>
# c. 400 - 499<br>
# d. 500 - 599<br>
# e. 600 - 699<br>
# f. 700 - 799<br>
# g. 800 - 899<br>
# h. 900 - 999<br>
# i. 1000 em diante
#     
#     
# <b>Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

# In[ ]:


listaSalarios = [200, 300, 400, 500, 600, 700, 800, 900, 1000]
listaContagem = [0]*9
print(listaContagem)
for salario in listaSalarios:
    indice = salario//100-2
    listaContagem[indice] += 1
print(listaContagem)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>17. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
#     
# ![image.png](attachment:image.png)

# In[ ]:


listaSalto = ['', 'Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
listaAtleta = list()

while True:
    nomeAtleta = str(input('Nome do Atleta: ')).title().strip()
    if nomeAtleta == '':
        break

    print(f'Saltos de {nomeAtleta}.\n')
    for salto in range(1, 6):
        salto_atleta = float(input(f'{listaSalto[salto]} Salto: '))
        listaAtleta.append(salto_atleta)

    print('\nResultado Final: \nSaltos: ', end='')
    for salto in listaAtleta:
        if salto != listaAtleta[4]:
            print(salto, end=' - ')
        else:
            print(salto)

    print(f'Média dos Saltos: {sum(listaAtleta)/len(listaAtleta):.2f} m.')
    print('-'*45)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>18. Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
#     
#     
# a. O total de votos computados;<br>
# b. Os númeos e respectivos votos de todos os jogadores que receberam votos;<br>
# c. O percentual de votos de cada um destes jogadores;<br>
# d. O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
#     
#     
# <b>Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
#     
# 
# ![image.png](attachment:image.png)

# In[ ]:


lista_votos = list()
lista_texto = list()

print('Enquete: Quem foi o melhor jogador?\n')
while True:
    n = int(input('Quem foi o melhor jogador? [0 = FIM]: '))
    if n == 0:
        break
    elif n < 0 or n > 23:
        print('\033[1;31mInforme um valor entre 1 e 23 ou 0 para sair!\033[m')
    else:
        lista_votos.append(n)
print('-'*42)


if len(lista_votos) == 0:
    print('Nenhum Voto Computado. Programa Encerrado!')
else:
    lista_votos.sort()
    lista_sem_repetidos = sorted(set(lista_votos))
    print()
    texto_1 = ('Resultado da Votação: \n')
    texto_2 = (f'\nForam computados {len(lista_votos)} votos.\n')
    texto_3 = ('-'*30 + '\n')
    texto_4 = ('Jogador'.rjust(5) + 'Votos'.rjust(10) + '%'.rjust(10) + '\n')

    print(texto_1 + texto_2 + texto_3 + texto_4 + texto_3)

    lista_texto.append(texto_1)
    lista_texto.append(texto_2)
    lista_texto.append(texto_3)
    lista_texto.append(texto_4)
    lista_texto.append(texto_3)

    maior = numero = 0
    for voto in lista_sem_repetidos:
        if maior == 0:
            maior = lista_votos.count(voto)
            numero = voto
        elif maior < lista_votos.count(voto):
            maior = lista_votos.count(voto)
            numero = voto

        texto_6 = (f'{voto}'.rjust(4) + f'{lista_votos.count(voto)}'.rjust(11) +
                   f'{lista_votos.count(voto)/len(lista_votos)*100:.1f}'.rjust(14)+'\n')
        print(texto_6)
        lista_texto.append(texto_6)

    lista_texto.append(texto_3)
    print(texto_3)

    texto_7 = (
        f'\nO melhor jogador foi o número {numero}, com {lista_votos.count(numero)} votos, correspondendo a {lista_votos.count(numero)/len(lista_votos)*100:.0f}% do total de votos.')
    print(texto_7)

    lista_texto.append(texto_7)

    arquivo = open('arquivo.txt', 'w')
    for item in lista_texto:
        arquivo.write(item)
    arquivo.close()


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>19. Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
#     
#     
# ![image.png](attachment:image.png)
#     
# 
# <b>Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:,
#     
#     
# ![image-2.png](attachment:image-2.png)

# In[ ]:


def menu():
    print('-'*60)
    print('Qual o Melhor Sistema Operacional Para Uso Em Servidores? ')
    print('''
  1. Windows Server
  2. Unix
  3. LINUX
  4. Netware
  5. Mac OS
  6. Outro  
  0. Sair
  ''')

    while True:
        opção = str(input('Selecione uma Opção: '))
        while len(opção) == 0:
            opção = str(input('Selecione uma Opção: '))
        try:
            if opção in '0123456':
                return opção
        except ValueError:
            print('Campo Vazio não é Válido.')
        except:
            print('Erro')

dictVotação = {'Windows Server': 1499, 'Unix': 3499,
                'Linux': 2999, 'Netware': 499, 'Mac Os': 149, 'Outro': 149}
while True:
    opção = menu()

    if opção == '0':
        print('Finalizando Enquete!')
        break
    elif opção == '1':
        dictVotação['Windows Server'] += 1
    elif opção == '2':
        dictVotação['Unix'] += 1
    elif opção == '3':
        dictVotação['Linux'] += 1
    elif opção == '4':
        dictVotação['Netware'] += 1
    elif opção == '5':
        dictVotação['Mac Os'] += 1
    else:
        dictVotação['Outro'] += 1


totalVotos = sum(dictVotação.values())
maisVotado = max(dictVotação.keys())
qtdVotosMaisVotado = max(dictVotação.values())

print(dictVotação)
print('\n\n\n'+'='*40)
print('Sistema Operacional' + 'Votos'.rjust(10) + '%'.rjust(9))
print('-'*40)

for i, (k, v) in enumerate(dictVotação.items()):
    print(f'{k}'.center(20) + f'{v}'.rjust(7) +
          f'{v/totalVotos*100:.0f}%'.rjust(12))
print('-'*40)
print(f'Total de Votos' + f'{totalVotos}'.rjust(13))
print(
    f'\nO Sistema Operacional Mais Votado foi o {maisVotado}, com {qtdVotosMaisVotado}, correspondente a {qtdVotosMaisVotado/totalVotos*100:.0f}% dos votos.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>20. As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
#     
#     
# <b>Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
#     
#     
# <b>Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. 
#    
#     
# <b>Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
#     
#     
# a. O salário de cada funcionário, juntamente com o valor do abono;<br>
# b. O número total de funcionário processados;<br>
# c. O valor total a ser gasto com o pagamento do abono;<br>
# d. O número de funcionário que receberá o valor mínimo de 100 reais;<br>
# e. O maior valor pago como abono;
#     
# 
# <b>A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
#     
# 
# ![image.png](attachment:image.png)

# In[ ]:


premio = 0.2
linhas = '='*35
listaFuncionario = list()
listaTemp = list()

totalGasto = total_entradas = valor_minimo = maior_valor = 0
while True:
    salario = float(input('Salário do Colaborador: R$ '))
    if salario == 0:
        break
    abono = salario * premio
    if abono <= 100:
        abono = 100
        valor_minimo += 1
    listaTemp = [salario, abono]
    listaFuncionario.append(listaTemp)
    totalGasto += abono
    total_entradas += 1
    if abono > maior_valor:
        maior_valor = abono

print(f'\n{linhas}\n'+'Projeção de Gastos com Abono'.center(35) + f'\n{linhas}')
print('Salário'.center(15) + 'Abono'.rjust(12))
print('-'*35)
for salario in range(0, len(listaFuncionario)):
    print(f'    R$ {listaFuncionario[salario][0]:.2f}'.ljust(
        15) + f'R$ {listaFuncionario[salario][1]:.2f}'.rjust(15))
print('='*35 + '\n')

print(f'Foram processados: {total_entradas} colaboradores.')
print(f'Total gasto com abonos: R$ {totalGasto:.2f}.')
print(f'Valor mínimo pago a {valor_minimo} colaboradores.')
print(f'Maior valor de abono pago: R$ {maior_valor:.2f}.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>21. Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
#     
#     
# a. O modelo do carro mais econômico;<br>
# b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro.
# 
# 
# <b>Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
# 
# 
# ![image.png](attachment:image.png)

# In[ ]:


listaCarro = ['Fusca', 'Gol', 'Vectra', 'Uno', 'HB20']
listaConsumo = [7, 10, 12.5, 5, 14]

print('-'*40)
print('Comparativo de Consumo de Combustível'.center(40))
print('-'*40)
for carro in range(0, 5):
    print(f'Veículo {carro+1}')
    print(f'Nome: {listaCarro[carro]}')
    print(f'Km por Litro: {listaConsumo[carro]}')
    print('-'*40)

menorConsumo = 0
print('Relatório Final')
for carro in range(0, 5):
    km_por_litro = 1000 / listaConsumo[carro]
    if menorConsumo == 0:
        menorConsumo = carro
    elif menorConsumo < km_por_litro:
        menorConsumo = carro

    print(f'{carro+1}  ' + f'{listaCarro[carro]}'.ljust(10) + f' {listaConsumo[carro]}'.ljust(
        8) + f' {km_por_litro:.1f} litros'.ljust(15) + f' R$ {km_por_litro*2.25:.2f} ')

print(f'O menor consumo é do {listaCarro[menorConsumo]}.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>22. Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
#     
#     
# <b>Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
#     
#     
# a. necessita da esfera;<br>
# b. necessita de limpeza; <br>
# c. necessita troca do cabo ou conector;<br>
# d. quebrado ou inutilizado.
#     
# <b>Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
#     
# ![image.png](attachment:image.png)

# In[ ]:


dictLevantamento = {'Necessita de Esfera': 39, 'Necessita de Limpeza': 29,
                     'Troca de Cabo ou Conector': 14, 'Quebrado ou Inutilizado': 14}

def menu_defeito():
    print('-'*45)
    print('''
  1. Necessita de Esfera
  2. Necessita de Limpeza
  3. Necessita de Troca de Cabo ou Conector
  4. Quebrado ou Inutilizado
  ''')    
    print('-'*45)
    opção = str(input('Selecione uma Opção: ')).strip()
    while opção not in '1234':
        opção = str(input('Selecione uma Opção Válida: ')).strip()
    return opção


totalVotos = 96
while True:
    print('-'*45)
    n_id = str(input('Código de Identificação do Mouse: ')).strip()
    if n_id == '0':
        break

    opção = menu_defeito()
    if opção == '1':
        dictLevantamento['Necessita de Esfera'] += 1
    elif opção == '2':
        dictLevantamento['Necessita de Limpeza'] += 1
    elif opção == '3':
        dictLevantamento['Troca de Cabo ou Conector'] += 1
    else:
        dictLevantamento['Quebrado ou Inutilizado'] += 1
    totalVotos += 0

print('\n\n')
print('Situação                     Quantidade       Percentual')

for i, (k, v) in enumerate(dictLevantamento.items()):
    print(f'{i+1}. {k}'.ljust(30) + f'{v}'.rjust(5) +
          f'{(v/totalVotos)*100:.1f}%'.rjust(18))


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>23. A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
#     
#     
# ![image.png](attachment:image.png)
#     
#     
# <b>O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

# In[ ]:


def conversao_byte_megabyte(valor):
    kbytes = valor / 1024
    return kbytes / 1024

def calculo_percentual(tamanhoTotal, valor):
    return round((valor / tamanhoTotal * 100), 2)

listaArquivo = list()
listaConteudo = list()
tamanhoTotal = 0

############ COM ARQUIVO TXT ############
#with open('usuarios.txt', 'r') as file:
#    arquivoLido = file.readlines()

#for linha in arquivoLido:
#    listaTemp = list()
#    listaTemp.append(linha[:15].strip())
#    listaTemp.append(round(conversao_byte_megabyte(float(linha[15:-1])), 2))
#    tamanhoTotal += round(conversao_byte_megabyte(float(linha[15:-1])), 2)
#    listaArquivo.append(listaTemp)
############ FIM COM ARQUIVO TXT ############

############ COM LISTA ############
listaUsuarios = [['Alexandre', '456123789'], ['Anderson', '1245698456'], ['Antonio', '123456456'], 
                 ['Carlos', '91257581'], ['Cesar', '987458'], ['Rosemary', '789456125']]

for usuario in listaUsuarios:
    
    listaTemp = list()
    listaTemp.append(usuario[0])
    listaTemp.append(round(conversao_byte_megabyte(float(usuario[1])), 2))
    tamanhoTotal += round(conversao_byte_megabyte(float(usuario[1])), 2)
    listaArquivo.append(listaTemp)

############ FIM COM LISTA #########
    
print('-'*60)
print('ACME Inc.' + 'Uso do Espaço em Disco Pelos Usuários'.center(55))
print('-'*60)
print('Nr.  Usuário\t\tEspaço Utilizado\t% do Uso\n')
for usuario in range(0, len(listaArquivo)):
    temporario = (f'{usuario + 1}.'.ljust(5) + f'{listaArquivo[usuario][0]}'.title().ljust(15) + f'{listaArquivo[usuario][1]}'.ljust(
        8) + 'MB' + f'{calculo_percentual(tamanhoTotal, listaArquivo[usuario][1])}%\n'.rjust(20))
    print(temporario)
    listaConteudo.append(temporario)

print(f'\nEspaço Total Ocupado: {tamanhoTotal} MB.\n')
print(f'Espaço Médio Ocupado: {round(tamanhoTotal/len(listaArquivo),2)} MB.')
print('-'*60)


arquivo_relatorio = open('relatorio.txt', 'w')
for linha in listaConteudo:
    arquivo_relatorio.write(linha)
arquivo_relatorio.close()


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>24. Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

# In[ ]:


def lancaDados(qtd):
    import random as rd
    listaLancamentos = list()
    for i in range(0, qtd):
        listaLancamentos.append(rd.randint(1, 6))
    return listaLancamentos

qtd = int(input('Lançar o dado quantas vezes? '))
lista = lancaDados(qtd)

for numero in range(1, 7):
    print(f'Número {numero} - ' + f'{lista.count(numero)} vezes - '.ljust(3) +
          f'{round(lista.count(numero)/len(lista)*100)}'.ljust(3) + '%')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------
