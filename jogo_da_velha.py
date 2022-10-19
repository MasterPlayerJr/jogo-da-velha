from random import randint as rand
import os
from time import sleep

def decidir_jogador():
    if jogada % 2 == 0:
        simb_jogador = 'X'
        jogador = 1
        return jogador, simb_jogador
    else:
        jogador = 2
        simb_jogador = 'O'
        return jogador, simb_jogador

def criar_tabelas():
    tabela = [['_','_','_'],
             ['_','_','_'],
             ['_','_','_']]    
    tabela_codigo = [[-2,-2,-2],
                    [-2,-2,-2],
                    [-2,-2,-2]]
    tabela_exemplo = [['1','2','3'],
                     ['4','5','6'],
                     ['7','8','9']]
    return tabela, tabela_codigo , tabela_exemplo

def verificar_vitoria():
    quina1 = tabela_codigo[0][0] + tabela_codigo[1][1] + tabela_codigo[2][2]
    quina1 = quina1 == 3 or quina1 == 6
    quina2 = tabela_codigo[0][2] + tabela_codigo[1][1] + tabela_codigo[2][0]
    quina2 = quina2 == 3 or quina2 == 6
    for i in range(0,2):
        linha = tabela_codigo[i][0] + tabela_codigo[i][1] + tabela_codigo[i][2]
        linha = linha == 3 or linha == 6
        coluna = tabela_codigo[0][i] + tabela_codigo[1][i] + tabela_codigo[2][i]
        coluna = coluna == 3 or coluna == 6
        if linha or coluna or quina1 or quina2:
            return True

def mostrar_tabela():
    for i in range(0,3):
        if verificacao:
            print(tabela[i])
        elif i == 1:
                    print(tabela[i],'Exemplo:',tabela_exemplo[i])
        else:
            print(tabela[i],' '*8,tabela_exemplo[i])

def iniciar_jogo():
    jogador = decidir_jogador()
    if modo_jogo == 1 and jogador[1] == 'O':
        joga = ''
    else:
        joga = ' JOGADOR'
    titulo_vez_de_joga = f'- VEZ DO{joga} {jogador[0]}({jogador[1]}) -'
    limpar(0)
    print(titulo_vez_de_joga.center(50))
    mostrar_tabela()
    return jogador

def escolher_tabela_codigo():
    if jogador[1] == 'X':
        tabela_codigo[num_lista][posicao_exemplo] = 1
        return tabela_codigo
    elif jogador[1] == 'O':
        tabela_codigo[num_lista][posicao_exemplo] = 2
        return tabela_codigo

def escolher_modo():
    titulo = '- JOGO DA VELHA -'
    print(titulo.center(50),'\n')
    print('1.Jogar contra computador \n2.Jogar contra outro jogador')
    modo_jogo = input('Selecione uma opção:')
    limpar(0)
    if modo_jogo == '1':
        return 1
    elif modo_jogo == '2':
        return 2
    else:
        return False

def jogar_denovo():
    denovo = input('Você deseja jogar denovo?(S/N):').upper()
    if denovo == 'N':
        limpar(0)
        return 'N'
    else:
        limpar(0)
        return 'S'

def limpar(tempo):
    if tempo == 0:
        os.system('cls')
    if tempo > 0:
        sleep(tempo)
        os.system('cls')

def opcao_errada():
    limpar(0)
    print("Opção errada! Digite outra.")
    limpar(1)

def ganhou():
    jogador = decidir_jogador()
    mostrar_tabela()
    print(f"Parabéns para o jogador {jogador[0]} ({jogador[1]}), Você Ganhou!!")
    

jogada = 0
verificacao = None
denovo = None

limpar(0)
modo_jogo = escolher_modo()

while True:
    if jogada == 0 or denovo == 'S':
        tabelas = criar_tabelas()
        tabela = tabelas[0]
        tabela_codigo = tabelas[1]
        tabela_exemplo = tabelas[2]
        if denovo == 'S':
            jogada = 0
            denovo = None
    verificacao = verificar_vitoria()
    if verificacao:
        jogada -= 1
        ganhou()
        denovo = jogar_denovo()
        if denovo == 'N':
            break
    if modo_jogo == 1 or modo_jogo == 2:
        if denovo != 'S':
            jogador = iniciar_jogo()
        if modo_jogo == 1 and jogador[0] == 2:
            escolha =  rand(1,9)
            escolha = str(escolha)
        elif denovo != 'S':
            escolha = input("Escolha a posição que você quer jogar:")
        num_lista = 0
        if escolha == '' or escolha == '0':
            continue
        elif int(escolha) > 3:
            for i in range(1,int(escolha)):
                if i % 3 == 0:
                    num_lista += 1
        posicao_exemplo = tabela_exemplo[num_lista].index(escolha)
        if denovo == 'S':
            continue
        elif tabela_codigo[num_lista][posicao_exemplo] != -2:
            jogada -= 1
            if jogador[0] == 1 and modo_jogo == 2:
                print("Essa posição ja foi ocupada.")
                limpar(1)
            else:
                limpar(0)
        else: 
            tabela[num_lista][posicao_exemplo] = jogador[1]
        escolher_tabela_codigo()
        if jogada == 8:
            print('Deu velha!')
            denovo = jogar_denovo()
            if denovo == 'N':
                limpar(2)
                break
            else:
                jogada = 0
    else:
        opcao_errada()
        modo_jogo = escolher_modo()
    jogada += 1
    limpar(0)