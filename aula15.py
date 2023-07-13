'''
Interrompendo repetições while
'''
'''
enquanto Verdadeiro
    se bloco
        passo
    se buraco
        pula
    se moeda
        pega
    se trofeu
        pula
        interrompa
pega

#python:

while True:
    if bloco
        passo
    if buraco
        pula
    if moeda
        pega
    if trofeu       #Se encontrar trofeu: break: vai sair do loop e ir para fora do loop e ir para o pega
        pula
        break
pega
'''
#Na prática

#While True: -> Vai executar pra sempre

cont = 1
while cont <= 10:
    print(f'{cont}', '> ', end='')
    cont += 1
print('Acabou')

'''
n = s = 0
while n != 999:
    n = int(input('Um número: '))
    s += n
s -= 999    #Gambiarra
print(f'{s} = soma dos valores. ')
'''

#Forma 'correta'
n = s = 0
while True:
    n = int(input('Um número: '))
    if n == 999:
        break       #Isso faz com que some todos valores, mas não some o '999' já que esse é o nosso flag
    s += n
print(f'{s} = soma dos valores. ')

