import random
import PerguntasShowDoMilhão
from time import sleep
from Utilitarios import printCor, opcaoCorrigida
from termcolor import colored

# lista de prêmios e variáveis
premios = [1000,2000,3000,4000,5000,
           10000,20000,30000,40000,50000,
           100000,200000,300000,400000,500000,1000000]

pulos = 3
ajudas = 3
ajuda_universitarios = 1
ajuda_garantida = 1
ajuda_eliminar = 1
valor_acumulado = 0
contador_perguntas = 0

try:
# randomizador de perguntas e opções
    while True:
        pergunta = random.choice(PerguntasShowDoMilhão.perguntasMilhao)
        printCor('-='*20, 'yellow')
        printCor(pergunta['pergunta'], 'yellow')

        for opcao in pergunta['opcoes']:
            printCor(opcao, 'green')

        # Perguntas, sistema de ajuda e pulos
        try:
            printCor('Você pode digitar PULAR para pular ou AJUDA para o mesmo', 'yellow')
            resposta_usuario = str(input(colored('Digite sua opção: ','green'))).strip().upper()
            if resposta_usuario < '1' or resposta_usuario > '4':
                opcaoCorrigida(resposta_usuario)

            elif resposta_usuario == 'PULAR' and pulos > 0:
                pulos -= 1
                continue

            elif resposta_usuario == 'AJUDA' and ajudas > 0:
                ajudas -= 1
                printCor('''-=-=-=-=-=-=-=-=-=-=
[1] ACERTO GARANTIDO
[2] UNIVERSITÁRIOS
[3] ELIMINAR DUAS ALTERNATIVAS
-=-=-=-=-=-=-=-=-=-=''', 'yellow')
                opcao = int(input(colored('Qual você vai escolher? ', 'green')))

                # primeiro tipo de ajuda
                if opcao == 1 and ajuda_garantida == 1:
                    ajuda_garantida -= 1
                    printCor(f'A resposta correta é...', 'yellow', end = '',)
                    sleep(1.3)
                    printCor(f'Opção {pergunta["resposta"]}','yellow')
                    resposta_usuario = str(input(colored('Digite sua opção: ','green'))).strip().upper()

                elif opcao == 2 and ajuda_universitarios == 1:
                    ajuda_universitarios -= 1
                    print('Os universitários estão pensando...')
                    sleep(2)
                    for i in range(0, 3):
                        ChanceAcerto = random.randint(1, 100)
                        if ChanceAcerto <= 70:
                            resposta = pergunta['resposta']
                        else:
                            opcoes_erradas = ["1", "2", "3", "4"]
                            opcoes_erradas.remove(pergunta['resposta'])
                            resposta = random.choice(opcoes_erradas)
                        print(f'O universitário {i+1} acha que a resposta é: {resposta}')
                    resposta_usuario = str(input(colored('Digite sua opção: ','green'))).strip().upper()

                elif opcao == 3 and ajuda_eliminar == 1:
                    ajuda_eliminar -= 1
                    erradas = [op for op in pergunta['opcoes'] if pergunta['resposta'] not in op]
                    eliminar = random.sample(erradas, 2)
                    print("Eliminando alternativas:")
                    for e in eliminar:
                        print(e)
                    for e in eliminar:
                        pergunta['opcoes'].remove(e)

                    print("\nOpções restantes:")
                    for op in pergunta['opcoes']:
                        print(op)

                    resposta_usuario = str(input(colored('Digite sua opção: ','green'))).strip().upper()

                else:
                    print('Você não tem mais esse tipo de ajuda.')
                    resposta_usuario = str(input(colored('Digite sua opção: ','green'))).strip().upper()

            elif resposta_usuario == 'PULAR' and pulos <= 0:
                while True:
                    print('Você não possui mais pulos.')
                    resposta_usuario = str(input(colored('Digite sua opção: ','green'))).strip().upper()
                    if resposta_usuario != 'PULAR':
                        break

            elif resposta_usuario == 'AJUDA' and ajudas <= 0:
                while True:
                    print('Você não possui mais ajudas.')
                    resposta_usuario = str(input(colored('Digite sua opção: ','green'))).strip().upper()
                    if resposta_usuario == 'PULAR' and pulos > 0:
                        pulos -= 1
                        break
                    elif resposta_usuario != 'AJUDA':
                        break

        except ValueError:
            printCor('Entrada inválida, tente novamente.','red')
            continue
        except Exception as erro:
            printCor(f'Houve um erro: {erro}','red')
            continue

        # Verificação de acerto
        if str(resposta_usuario) == str(pergunta['resposta']):
            printCor('Parabéns, você acertou!','cyan')
            contador_perguntas += 1
            PerguntasShowDoMilhão.perguntasMilhao.remove(pergunta)

            if contador_perguntas <= len(premios):
                valor_acumulado = premios[contador_perguntas - 1]
            else:
                valor_acumulado = premios[-1]

            printCor(f'O seu dinheiro atual é R$ {valor_acumulado:,}','green'.replace(',', '.'))

            if contador_perguntas == len(premios):
                print('Parabéns, você acertou todas as perguntas!!')
                break
        else:
            printCor(f'Você errou. Seu prêmio foi de: R$ {valor_acumulado/2:,}','green'.replace(',', '.'))
            break
except KeyboardInterrupt:
    print('\nFinalizando Jogo...')
    sleep(2)
    print('Jogo finalizado')