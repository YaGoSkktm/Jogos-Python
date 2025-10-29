def printCor(msg, cor, Nacor=None, **kwargs):
    '''
      :param msg: Aqui você pode escrever oque quer que apareça
      :param cor: Agui você escolhe a cor das letras (deve ser em inglês e em letras minúsculas)
      :param Nacor: aqui é o cur no fundo das letras, funciona igual a cor porém deve ter on_ antes da cor.
      :return:
      '''
    from termcolor import colored
    from colorama import init

    init()
    print(colored(msg, cor, Nacor))

def opcaoCorrigida(resposta_usuario):
        while True:
            print('Opçâo invalida')
            resposta_usuario = str(input('Digite sua opção: '))
            if resposta_usuario in ['1', '2', '3', '4']:
                return resposta_usuario
            else:
                continue