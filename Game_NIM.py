## Jogo do NIM ##

# Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. 
# Dois jogadores jogam alternadamente, retirando pelo menos 1 e no máximo m peças cada um.
# Quem tirar as últimas peças possíveis ganha o jogo.


def computador_escolhe_jogada(n, m):
    if n > m+1: 
        ret = n - (n // (m+1))*(m + 1)
    else:
        if n < m:
            ret = n
        else:
            ret = m
            
    n = n - ret
    print()
    print("O computador tirou %d peças." %ret)
    
    if n > 1:
        print("Agora restam %d peças no tabuleiro." %n)
        print()
    else:
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro")
    return ret

def usuario_escolhe_jogada(n, m):
    ret = m+1
    while ret > m or ret < 1:
        ret = int(input("Quantas peças você vai tirar? "))
        print()
        if ret > m or ret < 1:
            print("Oops! Jogada inválida! Tente de novo.")
            print()

    n = n - ret
    print("Você tirou %d peças." %ret)
    
    if n > 1:
        print("Agora restam %d peças no tabuleiro." %n)
        print()
    else:
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro")

    return ret

def nim():
    print("Bem-vindo ao jogo do NIM!")
    print()
    tipo_jogo = 0

    while tipo_jogo < 1 or tipo_jogo > 2:
        print("1 - Para jogar uma partida isolada.\n2 - Para jogar um campeonato.")
        tipo_jogo = int(input("\nEscolha: "))
        print()
    
    j = 0

    if tipo_jogo == 1:
        j = partida()
    else:
        print("Você escolheu um campeonato!")
        print()
        if tipo_jogo == 2:
            num = 1
            player = 0
            computer = 0
            while num < 4:
                print("**** Rodada %d ****" %num)
                print()
                j = partida()
                num += 1
                if j == 1:
                    computer += 1
                else:
                    if j == 2:
                        player += 1

        print("**** Final do campeonato! ****")
        print()
        print("Placar: Você %d X %d Computador" %(player,computer))

def partida():
    n_pecas = 0
    l_jogada = 0
    
    while n_pecas < 1: 
        n_pecas = int(input("Quantas peças? "))
    while l_jogada < 1:
        l_jogada = int(input("Limite de peças por jogada? "))
        print()

    band = 0
    if n_pecas % (l_jogada + 1) != 0:
            print("Computador começa!")
            band = 1
    else:
        print("Você começa!")
        band = 2

    winner = 0   
    while n_pecas > 0:
        if band == 1:
            pecas_ret = computador_escolhe_jogada(n_pecas, l_jogada)
            band = 2
            n_pecas = n_pecas - pecas_ret
            if n_pecas == 0:
                winner = 1
                print("Fim do jogo! O computador ganhou!")
                print()
        else:
            if band == 2:
                pecas_ret = usuario_escolhe_jogada(n_pecas, l_jogada)
                band = 1
                n_pecas = n_pecas - pecas_ret
                if n_pecas == 0:
                    winner = 2
                    print("Você ganhou!")
    return winner
nim()
    