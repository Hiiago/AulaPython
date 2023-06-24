'''
Estrutura de repetição for
também podem ter essese nomes: laços, repetições ou iterações

Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o "for",
 que é uma estrutura versátil e simples de entender. Por exemplo:

for c in range(0, 4):
     print(c)
print('Acabou')
laçoes de repetição (parte 1)
'''


'''imagina que existam 6 blocos 
o primeiro está nosso personagem e o último o objetivo que é pegar a maçã
vamos dar o primeiro comando passo:

passo()
passo()
passo()
passo()
passo()
pegar() #Agora posso pegar a maçã

se percebermos isso está se repetindo, imagine que seja milhares de passos, isso seria cansativo
então temos um comando, a estrutura de laço

vamos colocar uma "bola que gira" e dentro dela o comando "passo()"
#Isso faria com que o comando se repetisse infinitamente 

para isso precisamos colocar um limite chamado laço de repetição ou laço de iteração:
sabendo que cada espaço tem uma númeração e nós precisamos chegar ao numero 10
faremos um limite dentro dessa "bola que gira" do "1 ao 10"
quando chegar ao 10 irá parar e sair para executar outro comando
nesse caso, o comando "pegar()"
#Esse laço especíco se chama laço com variável de controle

Comando:
laço c no intervalo(1, 10) # Laço para contar no intervalo entre 1 e 10. "c" variável de controle (pode ter qualquer nome) 
    passo   # <- é o comando que será executado do 1 ao 10
pega    # <- está fora do laço (executa assim que acabar o laço de repetição)

Em Python:
for c in range(1, 10):  # sempre lembrar dos dois pontos 
    passo
pega
------------------------------------------------

#Imagine outra situação com mesmos objetivos, mas com buracos que precisam ser pulados
seria assim:

passo()     #anda
pula()      #pula o buraco
passo() 
pula()
passo()
pula()
passo()
pega()      #pega a mação

#Os comandos passo() e pula() executa 3 vezes
Então vamos criar um laço "bola que gira" e fazer ele repetir
colocamos o passo() e pula() dentro
e colocaremos um limite entre 0 e 3     #Caso queira repetir mais vezes, mude o 3 para quantos preferir
depois irá sair quando terminar a contagem 
terá mais um passo() e um pega() 
fim do laço

Comando:
laço c no intervalo(0, 3)
    passo
    pula
passo
pega

Em Python
for c in range(0, 3):
    passo
    pula
passo
pega
------------------------------------------------------

#O mesmo último cenário mas agora adicionando duas moedas no caminho

passo()
pula()
pega()      #pega moeda
passo()
pula()
passo()
pula()
pega()      #pega moeda
passo()
pega()      #pega maçã


comando com "se" = "if"
dentro desse laço de repetição, se tiver moeda: pega

#Aninhando estruturas (colocando uma estrutura dentro da outra)
laço c no intervalor(0, 3)  #Estrutura de repetição
    se moeda        #Estrutura condicional
        pega
    elif maçã:
        pega
    passo
    pula
passo
pega


No Python
for c in range(0, 3):
    if moeda:
        pega
    elif maçã:
        pega
    passo
    pula
'''
#Na prática:

'''print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')'''
#com estrutura de repetição for

for c in range(0, 6):
    print('Oi')     #<- que vai se repetir
print('Fim')        #<- fora do for para não repetir também

for c in range(0, 6):
    print(c)        #<- vai mostrar o número dentro do range (de 0 a 5)
print('Fim')

for c in range(6, 0, -1):
    print(c)        #Mostra os números de trás pra frente (6 ao 1)
print('Fim')

for c in range(0, 7, 2):
    print(c)        #Vai de 0 a 7 contando de 2 em 2 (0, 2, 4, 6)
print('Fim')

n = int(input('Número:'))
for c in range(0, n+1):     #"+1" para adicionar um número no número em que pediu e mostrar o resultado que pediu
    print(c)                #Mostra o número do range (0) até o número que foi pedido na variável
print('Fim')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):  #f+1: número pedido na variável "f" = Fim +1 (isso da o número exato pedido)
    print(c)           #Será mostrado o inicio, pulando de quantos pediu até o final que foi pedido
print('Fim')            #exemplo: inicio: 1. fim: 8. passo: 2 (1, 3, 5, 7)

for c in range(0, 3):
    n = int(input('Digite um valor: '))     #Vai ler a variável "n" 3 vezes e vai parar
print('Fim')

s = 0       #Soma começa recebendo 0 pois precisa começar com algum valor para somar depois
for c in range(0, 4):
    n = int(input('Digite um valor: '))     #Vai ler a variável "n" 4 vezes e vai parar
    s += n      # s recebe s + n. Isso soma os valores dentro do range (exemplo: 2 + 4 + 5 = s = 11. print(11))
print(f'O somatório de todos os valores foi {s}.')

