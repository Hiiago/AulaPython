#MUNDO 2
'''Condições aninhadas

Nessa aula, vamos aprender como criar estruturas condicionais aninhadas,
usando os comandos if.. elif.. else em programas Python.'''


'''É quando se coloca uma coisa dentro da outra
quando se coloca estruturas condicionais dentro de estruturas condicionais = Condições aninhadas'''


'''O mesmo exemplo da aula 10, com um carro em uma estrada, mas agora com 3 caminhos para escolher
'''


'''
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
senão se carro.direita()
    carro.siga() #Vai seguir em frente <- Seguiu a direita
    carro.esquerda() #Vira a esquerda
    carro.siga() #Vai seguir em frente
    carro.esquerda() #Vira a esquerda
    carro.siga() #Vai seguir em frente
    
senão
    carro.siga() # <- Terceiro caminho
carro.pare() #Parar o carro'''



#Forma com "if, elif e else":

'''
carro.siga()
if carro.esquerda():
    carro.siga() 
    carro.direita() 
    carro.siga() 
    carro.direita() 
    carro.esquerda()
    carro.siga() 
    carro.direita() 
    carro.siga() 


elif carro.direita():
    carro.siga() 
    carro.esquerda() 
    carro.siga() 
    carro.esquerda() 
    carro.siga() 

else:
    carro.siga() 
carro.pare() '''


#Estrutura aninhadas. Pode-se usar quantos "elif" quiser desde que esteja dentro do if
'''if carro.esquerda():
    bloco1
elif carro.direita():
    bloco2
elif carro.ré():
    bloco3
else:
    bloco4'''


nome = str(input('Nome: '))
if nome == 'Hiago':
    print('Que nome lindo! ')
elif nome == 'finslan' or nome == 'gut' or nome == 'eli':
    print(f'Dariam um belo nickname!')
elif nome in 'Ana Cláudia Izabel Jaqueline':
    print('Nomes femininos ! ')
else:
    print('Nome normalzinho...')        #<- "else" é opcional
print(f'Tenha um bom dia, {nome}!')
