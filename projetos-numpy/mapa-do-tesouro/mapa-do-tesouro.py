import numpy as np

#Mapa 5 x 5
mapa = np.random.randint(1, 10, size=(5, 5))

#Posiciona o tesouro em uma posição aleatória
while True:
    tesouro_x, tesouro_y = np.random.randint(0, 5, size=2)
    if (tesouro_x, tesouro_y) != (0, 0):
        break

posicao_jogador = (0, 0)
pontuacao = 0

def mostrar_mapa(mapa, posicao_jogador):
    mapa_com_jogador = mapa.copy()
    linha, coluna = posicao_jogador
    mapa_com_jogador[linha, coluna] = -1

    mapa_com_jogador_str = np.char.mod('%2d', mapa_com_jogador) #Converte a matriz para string
    mapa_com_jogador_str[mapa_com_jogador_str == '-1'] = ' P' #Marca a posição do jogador com 'P'

    print("\nMapa Atual:")
    for linha in mapa_com_jogador_str:
        print(" ".join(linha))

#Fluxo principal do jogo
while True:
    mostrar_mapa(mapa, posicao_jogador)

    direcao = input("Informe a direção que seja mover! (cima, baixo, esquerda, direita)").strip().lower()

    movimentos = {
        "cima": (-1, 0),
        "baixo": (1, 0),
        "esquerda": (0, -1),
        "direita": (0, 1),
        "c": (-1, 0),
        "b": (1, 0),
        "e": (0, -1),
        "d": (0, 1)
    }
    if direcao in movimentos:
        nova_posicao = (posicao_jogador[0] + movimentos[direcao][0], posicao_jogador[1] + movimentos[direcao][1])
    else:
        print("Direção inválida! Tente novamente.")
        continue

    #Verifica se a nova posição é válida
    if not (0 <= nova_posicao[0] < 5 and 0 <= nova_posicao[1] < 5):
        print("Movimento fora dos limites! Tente novamente.")
        continue

    posicao_jogador = nova_posicao
    pontuacao += 1

    if posicao_jogador == (tesouro_x, tesouro_y):
        mostrar_mapa(mapa, posicao_jogador)
        print(f"\n\n======Parabéns! Você encontrou o tesouro!======")
        print(f"Pontuação: {pontuacao}")
        print(f"Posição do tesouro: ({tesouro_x}, {tesouro_y})")
        break
    