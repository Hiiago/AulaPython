'''Condições - condicionais
Simples e compostas'''

#Todos métodos tem (parenteses) no final

'''imagine um carro numa estrada com um ponto de chegada'''

#Estrutura sequencial: conjunto de passos que sempre vai ser seguido da esquerda para a direita
'''carro.siga() #Vai seguir em frente
carro.esquerda() #Vira a esquerda
carro.siga() #Vai segui em frente
carro.direita() #Vira a direita
carro.siga() #Vai segui em frente
carro.direita() #Vira a direita
carro.siga() #Vai segui em frente
carro.esquerda() #Vira a esquerda
carro.siga() #Vai segui em frente
carro.pare() #Parar o carro'''

'''#Imagine um carro numa estrada com um ponto de chegada com opções de curvas

#Bloco de comandos caso escolha o caminho da esquerda:

carro.siga() #Vai seguir em frente
#aqui uma bifurcação, onde temos que escolher onde virar, caso escolha um, não da pra escolher outro
#subalgoritmo
carro.siga() #Vai seguir em frente <- seguiu o caminho da esquerda
carro.direita() #Vira a direita
carro.siga() #Vai seguir em frente
carro.direita() #Vira a direita
carro.esquerda() #Vira a esquerda
carro.siga() #Vai seguir em frente
carro.direita() #Vira a direita
carro.siga() #Vai seguir em frente
carro.pare() #Parar o carro

#Bloco de comandos caso escolha o caminho da direita:

carro.siga() #Vai seguir em frente
#aqui uma bifurcação, onde temos que escolher onde virar, caso escolha um, não da pra escolher outro
#subalgoritmo
carro.siga() #Vai seguir em frente
carro.esquerda() #Vira a esquerda
carro.siga() #Vai seguir em frente
carro.esquerda() #Vira a esquerda
carro.siga() #Vai seguir em frente
carro.pare() #Parar o carro

#Independente da escolha, sempre terá o começo "carro.siga()" e "carro.pare()" '''

'''Estrutura "se" e "senão" = "if" "else" 
#Representação estruturada ou identada:


carro.siga() #Vai seguir em frente
se carro.esquerda()
#Caminho verde = bloco verdadeiro = se a condição do 'se' for verdadeira, vai executar esse bloco:
    carro.siga() #Vai seguir em frente <- Seguiu caminho da esquerda
    carro.direita() #Vira a direita
    carro.siga() #Vai seguir em frente
    carro.direita() #Vira a direita
    carro.esquerda() #Vira a esquerda
    carro.siga() #Vai seguir em frente
    carro.direita() #Vira a direita
    carro.siga() #Vai seguir em frente

#Caminho vermelho = bloco falso = senão virar a esquerda, vai executar esse bloco:
senão carro.direita()
    carro.siga() #Vai seguir em frente <- Seguiu a direita
    carro.esquerda() #Vira a esquerda
    carro.siga() #Vai seguir em frente
    carro.esquerda() #Vira a esquerda
    carro.siga() #Vai seguir em frente
carro.pare() #Parar o carro '''

'''
#Nessa condição nunca vai ser executado o bloco verde e o vermelho juntos 
if para estrutura simples
if e else para estrutura composta

se carro.esquerda()   =  if carro.esquerda():
    bloco_V_          =     bloco True 
senão                   else:
    bloco_F_          =     bloco False
'''

#if e else para estrutura composta
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo!')
else:
    print('Carro velho!')
print('--FIM--')

#if estrutura simplificada
tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo!' if tempo <= 3 else 'Carro velho!') #Escreva 'carro novo!' se o tempo for menor ou igual a 3, senão, escreva 'carro velho!'
print('--FIM--')


nome = str(input('Nome: '))
if nome == 'Hiago':
    print('Que nome lindo! ')
print(f'Bom dia, {nome}!')

nome = str(input('Nome: '))
if nome == 'Hiago':
    print('Que nome lindo! ')
else:
    print('Que nome normal...')
print(f'Bom dia, {nome}!')

nota1 = float(input('Nota: '))
nota2 = float(input('Nota: '))
media = (nota1 + nota2) / 2   #() <- Ordem de precedencia
print(f'A sua média foi: {media:.1f}')
if media >= 6.0:
    print('Sua média foi boa!')
else:
    print('Sua média foi ruim! ')
