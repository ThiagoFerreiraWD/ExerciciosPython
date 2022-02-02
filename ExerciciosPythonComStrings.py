#!/usr/bin/env python
# coding: utf-8

# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# ![python-1536x650.png](attachment:python-1536x650.png)

# # <center> <u>Exercícios com Strings
# <center><font color='#787878'>Exercícios disponíveis no link: https://wiki.python.org.br/ExerciciosComStrings, desenvolvidos por mim para aperfeiçoamento profissional.
#     
#     

# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>1. Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
#     
# ![image.png](attachment:image.png)

# In[ ]:


string1 = str(input('Digite a primeira string: '))
string2 = str(input('Digite a segunda string: '))

print('Compara duas strings')
print(f'String 1: {string1}')
print(f'String 2: {string2}')
print(f'Tamanho de "{string1}": {len(string1)} caracteres.')
print(f'Tamanho de "{string2}": {len(string2)} caracteres.')
print(f'As duas strings são de tamanho ', end='')
print('diferentes' if len(string1) != len(string2) else 'igual')
print(f'As duas strings possuem conteúdo ', end='')
print('diferente' if string1.lower() != string2.lower() else 'igual')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>2. Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

# In[ ]:


nome = str(input('Digite seu nome: '))
print(f'{nome[::-1].upper()}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>3. Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
#     
# ![image.png](attachment:image.png)

# In[ ]:


nome = str(input('Digite seu nome: ')).upper()
for letra in nome:
    print(letra)


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>4. Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
# 
# ![image.png](attachment:image.png)

# In[ ]:


nome = str(input('Digite seu nome: '))
for letra in range(len(nome)+1):
    print(nome[0:letra])


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>5. Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
# 
# ![image.png](attachment:image.png)

# In[ ]:


nome = str(input('Digite seu nome: '))
for letra in range(len(nome), 0, -1):
    print(nome[0:letra])


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>6. Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
#     
# ![image.png](attachment:image.png)

# In[ ]:


listaMes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

data = str(input('Informe da Data de Nascimento (dd/mm/aaaa): '))

dia = data[0:2]
mes = int(data[3:5])
ano = data[6:10]

print(f'Você nasceu em {dia} de {listaMes[mes-1]} de {ano}.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>7. Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
# 
# a. quantos espaços em branco existem na frase.
#     
#     
# b. quantas vezes aparecem as vogais a, e, i, o, u. 

# In[ ]:


frase = str(input('Digite uma frase: '))

total_vogais = total_espacos = 0

for letra in frase:
    if letra == ' ':        total_espacos += 1
    if letra.lower() in 'aeiouéáàêãíóôõúü':        total_vogais += 1

print(f'A frase "{frase}" possui {total_espacos} espaco(s) e {total_vogais} vogal(is)')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>8. Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

# In[ ]:


frase = str(input('Informe uma frase ou uma palavra: '))

print(f'Palíndromo' if frase.replace(' ', '').lower() == frase.replace(' ', '')[::-1].lower() else 'Não é Palíndromo')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>9. Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

# In[ ]:


n_cpf = str(input('Informe o número do CPF: ')).strip()

cpf_format = n_cpf.replace('.', '').replace('-', '')

# PRIMEIRO DIGITO
total_digito1 = 0
v1 = 10
for n in cpf_format[:9]:
    total_digito1 += int(n) * v1
    v1 -= 1    

if total_digito1 % 11 < 2:    
    digito1 = 0
else:    
    digito1 = 11 - (total_digito1 % 11)
    
# SEGUNDO DIGITO
total_digito2 = 0
v2 = 11

for n in cpf_format[:10]:
    total_digito2 += int(n) * v2
    v2 -= 1

if total_digito2 % 11 < 2:    
    digito2 = 0
else:    
    digito2 = 11 - (total_digito2 % 11)
    
# VALIDACAO

if (int(cpf_format[9]) == digito1) and (int(cpf_format[10]) == digito2):
    print('CPF Válido!')
else:
    print(f'CPF Inválido!! Os dígitos verificadores deveriam ser {digito1, digito2}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>10. Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

# In[ ]:


dictNumeros = {0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove',
               10: 'dez', 11: 'onze', 12: 'doze', 13: 'treze', 14: 'catorze', 15: 'quinze', 16: 'dezesseis', 17: 'dezessete',
               18: 'dezoito', 19: 'dezenove', 20: 'vinte', 30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta',
               70: 'setenta', 80: 'ointenta', 90: 'noventa'}

while True:
    numero = str(input('Informe um número entre 0 e 99: '))
    if int(numero) >= 0 and int(numero) <= 99:
        break
        
if int(numero) < 21:
    print(dictNumeros[int(numero)])
elif int(numero) % 10 == 0:
    print(dictNumeros[int(numero)])
else:
    primeiro = int(numero) // 10 * 10
    segundo = numero[-1]     
    print(dictNumeros[int(primeiro)], end=' e ')
    print(dictNumeros[int(segundo)])


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>11. Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
#     
# ![image.png](attachment:image.png)

# In[ ]:


import random as rd

lista_palavras = []

with open('ex11e14.txt', 'r', encoding='utf-8') as f:
    for palavra in f.readlines():
        lista_palavras.append(palavra.split())

palavra_sorteada = lista_palavras[rd.randint(0, len(lista_palavras)-1)]
tentativas = 5
digitadas = []
validador = False

while tentativas != 0:
    letra = str(input(f'Digite uma letra [{tentativas} tentativa(s) restante(s).]'))[0].strip().upper()
    while letra in digitadas:
        letra = str(input(f'Digite uma letra [{letra} já foi] [{tentativas} tentativa(s) restante(s).]'))[0].strip().upper()
    
    if letra not in palavra_sorteada[0]:
        tentativas -= 1 
    
    digitadas.append(letra)
    senha = ''    
    for l in palavra_sorteada[0]:
        if l in digitadas:
            senha += l
        else:
            senha += ' _ '    
            
    if senha == palavra_sorteada[0]:
        validador = True
        break
    else:
        print(senha)

print(f'Você Venceu com {tentativas} tentativa(s) restante(s).' if validador else       f'Você Perdeu!!! A palavra era {palavra_sorteada[0]}')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>12. Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.
#     
# ![image.png](attachment:image.png)

# In[ ]:


telefone = str(input('Digite o Nº do Telefone: '))

telefoneSemDigito = telefone.replace('-','')

valido = True
if len(telefoneSemDigito) == 7:    telefoneSemDigito = '3' + telefoneSemDigito  
elif len(telefoneSemDigito) == 8:  telefoneSemDigito = telefoneSemDigito
else:    valido = False

if valido == True:
    print(f'Telefone Formatado: {telefoneSemDigito}')    
    print(f'Telefone Sem Dígito Formatado: {telefoneSemDigito[:4] + "-" + telefoneSemDigito[4:]}')
else:
    print('Número de Telefone Inválido')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b> 13. Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

# In[ ]:


import random as rd

palavras = []

with open('ex11e14.txt', 'r', encoding='utf-8') as f:    
    for p in f.readlines():  palavras.append(p.split())

p_sorted = palavras[rd.randint(1, len(palavras)-1)]
p_shuffle = ' - '.join(rd.sample(p_sorted[0],len(p_sorted[0])))

print('-'*50 + '\n' + p_shuffle.center(50)+ '\n' + '-'*50)

tentativa = 1
while tentativa != 6:
    palavra = str(input(f'Qual é a palavra? [{tentativa}/5] ')).strip().upper()
    if palavra == p_sorted[0].upper():
        print('-'*50 + '\n' + f'Acertou com {tentativa} tentativa(s).')
        break
    else:
        tentativa += 1
        
if tentativa == 6:
    print('-'*50 + '\n' + f'Você perdeu. A palavra era {p_sorted}.')


# <b><center>-------------------------------------------------------------------------------------------------------------------------------

# <b>14. Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.

# In[ ]:


dict_LeetSpek = {'A':'4', 'B':'I3', 'C':'[', 'D':'[)', 'E':'3', 'F':'ƒ', 'G':'6','H':'#', 'I':'!', 'J':']', 
                      'K':'|<', 'L':'1', 'M':'M','N':'|\|','O':'0', 'P':'|o', 'Q':'()_', 'R':'?-','S':'5', 'T':'7', 
                      'U':'|_|', 'V':'\/', 'W':'\/\/', 'X':'><', 'Y':'\|/', 'Z':'2', 'Ã': '4', 'Á':'4', 'Â': '4', 
                      'É':'3', 'Ó': '0', 'Ú': '|_|', '.': '.', '!':'!', '?':'?', ':':':', ';':';', ',':','}

frase = str(input('Digite a frase: ')).upper()

for letra in frase:
    print(dict_LeetSpek[letra], end='') if letra in dict_LeetSpek else print(letra, end='')

