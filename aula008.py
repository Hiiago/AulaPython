# Utilizando módulos


'''# Para incluir alguma coisa = import + alguma coisa (módulo/biblioteca)
# import bebida

# Para importar uma "bebida" específica nessa biblioteca
# from bebida import suco


# math = matemática - funcionalidades extras. vai importar:
# ceil = arredonda para cima
# floor = arredonda para baixo
# trunc = elimina da virgula pra frente
# pow = potência
# sqrt = raíz quadrada
# factorial = fatorial

# from math import sqrt = apenas consigo utilizar a função sqrt
# from math import sqrt, ceil = importa as duas funções
'''


'''import math
num = int(input('Um número: '))
raiz = math.sqrt(num)
print(f'A raíz de {num} é igual a {raiz}')

import math
num = int(input('Um número: '))
raiz = math.sqrt(num)
print(f'A raíz de {num} é igual a {math.ceil(raiz)}')

from math import sqrt, floor
num = int(input('Um número: '))
raiz = math.sqrt(num)
print(f'A raíz de {num} é igual a {floor(raiz):.2f}')'''

'''para ver as bibliotecas que posso importar:

python.org > versão > Library reference > escolher um tópico'''

#importando uma lib de numeros aleatorios entre 0 e 1
'''import random
num = random.random()
print(num)'''

# importando numeros aleatorios inteiros de 1 a 10
'''import random
num = random.randint()
print(num)'''

'''Em python.org > PyPi = Python package index = indice de pacotes extras:
Lista que pode ser importada separadamente
browse package > emoji > emjogi cheat sheet'''

# clique na lampada vermelha para baixar a lib
'''import emoji
print(emoji.emojize("Olá, mundo! :face_with_symbols_on_mouth:" ))'''

'''para ver os modulos instalados:
ferramentas > preferencias > projetos > interpretador
adicionar vai no " + " e escolhe algum 
desinstalar: vai no que quer e aperta o " - " '''
