import random
import TemasSorteio

TEMA = random.choice(list(TemasSorteio.temas.keys()))
palavraSorteada = random.choice(TemasSorteio.temas[TEMA])

palavra = palavraSorteada
letras_palavra = []
letras_ditas = letras_palavra[:]
vidas = 5
vitoria = False

from termcolor import colored
from colorama import init

init()

def printCor(msg, cor, Nacor=None):
    '''
    :param msg: Aqui você pode escrever oque quer que apareça
    :param cor: Agui você escolhe a cor das letras (deve ser em inglês e em letras minúsculas)
    :param Nacor: aqui é o cur no fundo das letras, funciona igual a cor porém deve ter on_ antes da cor.
    :return:
    '''
    print(colored(msg, cor, Nacor))

try:
    printCor(f'O TEMA É: {TEMA.upper()}', cor='blue', Nacor='on_black')

    while True:
        for letra in palavra:
            if letra in letras_palavra:
                print(letra, end='')
            else:
                print('-', end='')
        print()

        tentativa = str(input(colored('Digite a sua letra: ', 'white'))).lower().strip()[0]
        if tentativa.isnumeric():
            print('Isso não é uma letra.')
        else:
            letras_palavra.append(tentativa)
            if tentativa not in letras_ditas:
                letras_ditas.append(tentativa)
            printCor(f'LETRAS DITAS: {", ".join(letras_ditas)}', 'blue', 'on_black')
            if tentativa not in palavra:
                vidas -= 1
                printCor('ERROU!', 'red', 'on_black')
                if vidas > 0:
                    printCor(f'Você tem {vidas} vidas', 'magenta', 'on_black')
            printCor('++' * 15, 'blue')
            vitoria = True
            for letra in palavra:
                if letra not in letras_palavra:
                    vitoria = False

            if vidas < 1 or vitoria:
                break
except KeyboardInterrupt:
    print()

if vitoria:
    printCor(f'PARABENS, VOCÊ GANHOU!. A palavra era {palavra.upper()}', 'light_cyan')
else:
    printCor('GAME OVER!', 'magenta')
    printCor(f'Você perdeu. A palavra era {palavra.upper()}', 'magenta')


