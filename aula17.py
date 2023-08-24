'''
Variáveis compostas [listas]
'''

#Listas podem ser modificadas, são mutáveis

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
lanche[3] = 'sorvete'   #Posso substituir um elemento
print(lanche)

#Posso adicionar um novo elemento a lista:
lanche.append('cookie')
print('-'*20)
print(lanche)

#Posso adicionar um elemento a posição que eu quiser
print('-'*20)
lanche.insert(0,'cachorro quente')
print(lanche)

#Para deletar um elemento:
print('-'*20)
del(lanche[3])
#lanche.pop(3)
#lanche.remove('pizza')
#lanche.pop() #remove o último elemento
print(lanche)
print('-'*20)

valores = list(range(4, 11)) #Contagem de 4 até 10 colocando em uma lista 'valores' sendo as chaves do 0 ao 6
print(valores)
print('-'*20)

valores1 = [9,5,6,2,6,0]
valores1.sort() #Ordena os valores
valores1.sort(reverse = True) #Ordena ao contrário
print(valores1)
print('-'*20)

valores2=[8,3,7,5,6,9,1]
print(len(valores2))  #Faz a contagem de elementos (são 7)
print('-'*20)

num = [3, 6, 7, 0, 4]
if 5 in num:
    num.remove(5)
else:
    print('5 não encontrado.')
print(f'Essa lista tem {len(num)} elementos.')
print('-'*20)

numeros = list()
numeros.append(8)
numeros.append(5)
numeros.append(3)

for c, n in enumerate(numeros):
    print(f'Na posição {c} encontrei o valor {n}!')
print('Final da lista.')
print('-'*20)

lista = list()
for cont in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(f'Valores na lista: {lista}')
print('-'*20)

a = [3, 5, 6, 2]
b = a
b[2] = 8

print(f'Lista {a}')
print(f'Lista {b}')
print('-'*20)
a = [3, 5, 6, 2]
b = a[:] #Pega todos valores de a e joga em b fazendo uma cópia
b[2] = 8

print(f'Lista {a}')
print(f'Lista {b}')
