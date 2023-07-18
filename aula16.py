'''
Tuplas
São variáveis compostas e imutáveis que
permitem armazenar valores em uma mesma estrutura,
acessíveis por chaves individuais.
'''

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') #Tupla
print('-'*25)
print(lanche[1])    #Mostra o suco
print('-'*25)

print(len(lanche))  #Mostra a quantidade de elementos na tupla
print('-'*25)


for c in lanche:    #Para cada "comida" no lanche:
    print(f'Eu vou comer {c}')      #mostra todos itens da tupla
print('Comi demaiss')
print('-'*25)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')      #Mostra todos elementos na tupla
print('Comi demaiss')
print('-'*25)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição: [{cont}]')
print('Comi demaiss')
print('-'*25)
                    #A de cima e a de baixo funcionam da mesma forma. Contando mosrando cada numero que a tupla recebe
for pos, comida in enumerate(lanche):       #Enumerate funciona para mostrar a posição que tem na tupla
    print(f'Eu vou comer {comida} na posição: [{pos}]')
print('Comi demaiss')
print('-'*25)

print(sorted(lanche))  #Mostra os elementos da tupla em ordem
print('-'*25)

#Outro exemplo de tupla:

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)        #Junta a tupla a com a tupla b e mostra os números juntos
print('-'*25)
print(sorted(c))    #Mostra em ordem essas tuplas
print('-'*25)
print(len(c))   #Tamanho da tupla
print('-'*25)
print(c.count(5))   #Quantas vezes aparece o número citado
print('-'*25)
print(c.index(2))   #Em que posição está o número citado. (sempre pega a primeira ocorrencia)
print(c.index(2, 1))    #Deslocamento. O número 2 está na posição 0 mas há um outro que está na posição 6, para isso utilizamos um valor a mais depois da vírgula
print('-'*25)

pessoa = ('Hiago', 22, 'M', 63.88)
print(pessoa)
print('-'*25)

pessoa = ('Hiago', 22, 'M', 63.88)
del(pessoa)     #Apaga a tupla da memória e da erro caso peça para mostrar 
print(pessoa)