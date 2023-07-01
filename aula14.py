'''
Estruturas de repetição while
'''

'''
Sempre que tiver um "balãozinho", vamos entender como "enquanto" 
enquanto não maçã =  vai repetir sem parar enquanto não chegar na maçã
quando terminar a repetição, vai sair do laço e pegar a maçã
'''
#Quando não soubermos o limite, usamos while
'''
enquanto não maçã 
    passo
pega

#em python: 
while not apple:
    passo
pega
'''

'''imaginemos que nosso personagem tenha que pegar a maçã que está longe
no caminho há alguns buracos que temos que pular 
e moedas que podemos pegar
para isso faremos: 
'''

'''enquanto não maçã
    se tiver chão 
        passo
    se tiver buraco
        pule
    se tiver moeda 
        pega
pega maçã #Se tornou falso quando chegou na maçã
        
essa estrutura se repete até chegar na maçã
se no caminho não tiver alguma condição, ela continua para a próxima e repete novamente a estrutura 
até chegar na maçã'''

'''
em python:

while not apple:
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
pega
'''

'''for c in range(1, 10):
    print(c)
print('fim')    #Vai de 1 até 9'''
#Com while:

c = 1
while c < 10:   #Enquanto o contador (c) for menor do que 10:
    print(c)
    c += 1  #Quando vola, adiciona 1 a cara repetição


for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')        #Para digitar valores 4 vezes


n = 1
while n != 0:   #Vai se repetir até digitar o valor 0
    n = int(input('Digite um valor'))

resp = 'S'
while resp == 'S':    #Enquanto resposta == S, ele vai perguntar o valor de novo
    n = int(input('Digite um valor: '))
    resp = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 ==0:
            par += 1
        else:
            impar += 1
print(f'{par} Pares. {impar} Ímpares.')

