'''Cores no terminal'''

#Formato ensinado no curso:

'''
Código de cor:
   style  back
\033[0;33;44m
       text

STYLE          TEXT                 BACKGROUND <- cor de fundo
             
0 None         30      black       preto      40
1 negrito      31      red         vermelho   41
4 sublinhado   32      green       verde      42
7 Negativo     33      yellow      amarelo    43
               34      blue        azul       44
               35      Magenta     Magenta    45
               36      cyan        ciano      46
               37      grey        cinza      47
               97      white       branco     107
'''

#print('\033[0;30;41mTeste\033[m')
#print('\033[4;33;44mTeste\033[m')
#print('\033[1;35;43mTeste\033[m')
#print('\033[30;42mTeste\033[m')
#print('\033[mTeste\033[m')
#print('\033[7;30mTeste\033[m')


nome = 'finslan'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}                     # <- nome é o nome que está na variável nome
print(f"Prazer em te conhecer, {cores['pretoebranco']}{nome}{cores['limpa']}") #<- Cores limpas serve para a cor não continuar na linha
                                    # <- cores 'pretoebranco' indica a cor que está na variável cores

                            #Sempre se atentar com o uso das aspas simples e aspas duplas "" ''.

#Forma como aprendi fora do curso:

'''importando a biblioteca "colorama" e suas funções como init, Fore, Back, Style'''

from colorama import Fore, Back, Style
nome = 'finslan'
print(f'Prazer em te conhecer, {Fore.WHITE + Back.BLACK + (nome) + Style.RESET_ALL}')

