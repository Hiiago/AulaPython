'''Manipulando cadeias de caracteres, texto '''

frase = 'Curso em Video Python'

#Fatiamento
#Sempre o ultimo digito do colchete retorna um valor a menos
print('-Fatiamento')
print(f'{frase[9]}') #Retorna a letra do numero do indice dessa string (9 = V)
print(f'{frase[9:13]}') #Retorna do 9 ao 12 = do V ao O
print(f'{frase[9:21]}') #Vai do 9 ao 21 = do V ao n
print(f'{frase[9:21:2]}') #Vai do 9 ao 21 pulando de 2 em 2
print(f'{frase[:5]}') #Vai do começo da string e termina no 5 = termina no 4 = o
print(f'{frase[15:]}') #Vai do 15 ao final = Python
print(f'{frase[9::3]}') #Vai do 9 pulando de 3 em 3 até o final = V ao n
print('-' * 30)

#Análise
#Sempre o ultimo digito do colchete retorna um valor a menos
print('-Análise')
print(len(frase)) #Conta o tamanho da frase junto dos espaços
print(frase.count('o')) #Conta quantas vezes aparece a letra 'o'
print(frase.count('o', 0, 13)) #Conta do 0 ao 13 e mostra quantas vezes aparece o 'o'
print(frase.find('deo')) #Mostra em que momento começou o 'deo'
print(frase.find('Android')) #Retorna o valor -1 pois não existe 'Android'
print('Curso' in frase) #Se existe 'Curso' na frase(string) e retorna True ou False
print('-' * 30)

#Transformação
print('-Transformação')
print(frase.replace('Python', 'Android')) #Substitui uma frase pela outra
print(frase.upper()) #Coloca as letras em maiuscula
print(frase.lower()) #Para minuscula
print(frase.capitalize()) #Todos caracteres ficam minusculo, menos o primeiro
print(frase.title()) #Trasforma todas primeiras letras em maiusculo

frase2 = 'Aprendendo Python'
print(frase2.strip()) #Remove os primeiros e ultimos espaços
print(frase2.rstrip()) #Remove os ultimos espaços
print(frase2.lstrip()) #Remove os primeiro espaços
print('-' * 30)

#Divisão
print('-Divisão')
print(frase.split()) #Onde tiver espaço cria divisão e forma substrings, cada palavra recebe indexação nova(cada uma em uma lista nova)
print('-'.join(frase)) #Junta todos elementos de frase e usa o '-' para separa-los nos espaços
