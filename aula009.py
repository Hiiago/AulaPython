'''Manipulando cadeias de caracteres '''

#Análises
'''frase = 'Curso em Video Python'
frase.count('o', 0, 13) #quantas vezes a leta 'o' aparece do 0 ao 13
find('deo') #em que momento começou 'deo'
frase.find('Android') #retorna o valor -1 (nao existe)
'Curso' in frase #dentro de frase, tem a palavra Curso? = True'''

#Transformação
'''frase.replace('Python', 'Android') #Substitui frase
frase.upper() #transforma todas letras em maiúsculo
frase.lower() #transforma todas letras em minúsculas
frase.capitalize() #todos caracteres ficam minusculo e o primeiro fica maiusculo
frase.title() #analisa quantas palavras tem em frase e coloca as primeiras letras em maiusculo
frase.strip() #remove espaços inúteis (começo e final)
frase.rstrip() #remove ultimos espaços (direira)
frase.lstrip() #remove primeiros espaços (esquerda)'''

#Divisão
# frase.split() #cada string se transforma em uma lista própria

#Junção
# '-'.join(frase) #para juntar os elementos (string unica) mas com '-' onde seria espaço


frase = 'Curso em Vídeo Python'
print(frase.lower().find('vídeo'))

