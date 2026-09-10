import numpy as np

def colocar_peca(tabuleiro, linha, coluna, peca):
    """Coloca a peça do jogador na posição escolhida"""
    tabuleiro[linha, coluna] = peca

def verifica_vitoria(tabuleiro, peca):
    """Verifica se o jogador venceu"""
    linhas = np.any(np.all(tabuleiro == peca, axis=1))
    colunas = np.any(np.all(tabuleiro == peca, axis=0))
    diagonais = np.all(np.diag(tabuleiro) == peca) or np.all(np.diag(np.fliplr(tabuleiro)) == peca)
    return linhas or colunas or diagonais

def imprimir_tabuleiro(tabuleiro):
    """Imprime o tabuleiro de forma legível"""
    for linha in tabuleiro:
        print(" | ".join(str(x) if x !=0 else " " for x in linha))
        print("-" * 8)

def jogo():
    """Função principal para rodar o jogo da velha"""
    tabuleiro = np.zeros((3, 3), dtype=int)

    peca_atual = 1
    vencedor = False
    empate = False

    while not vencedor and not empate:
        imprimir_tabuleiro(tabuleiro)
        try:
            linha = int(input(f"Jogador {peca_atual}, escolha a linha (0, 1, 2): "))
            coluna = int(input(f"Jogador {peca_atual}, escolha a coluna (0, 1, 2): "))

            #Verifica se a linha e a coluna são válidas
            if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
                print("\nEscolha linhas e colunas válidas (0, 1, 2). Tente novamente!\n")
                continue
            #Verifica se a posição já está ocupada
            if tabuleiro[linha, coluna] != 0:
                print("\nPosição já ocupada! Tente novamente!\n")
                continue
            
            colocar_peca(tabuleiro, linha, coluna, peca_atual)
            vencedor = verifica_vitoria(tabuleiro, peca_atual)

            #Se houve empate
            if np.all(tabuleiro != 0) and not vencedor:
                empate = True

        except ValueError:
            print("\nEntrada inválida! Por favor, insira números inteiros de 0 a 2.\n")

        #Trocar jogador
        if not vencedor and not empate:
            peca_atual = 2 if peca_atual == 1 else 1

    if vencedor:
        print(f"\nParabéns, Jogador {peca_atual}! Você venceu!\n")
    else:
        print("\nEmpate! Ninguém venceu!\n")

jogo()







        