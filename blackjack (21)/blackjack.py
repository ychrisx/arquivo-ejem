import random

jogador = {
    "nome": "Jogador",
    "saldo": 100
}

def criar_baralho():
    cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baralho = cartas * 4
    random.shuffle(baralho)
    return baralho

def valor_carta(carta):
    if carta in ['J', 'Q', 'K']:
        return 10
    elif carta == 'A':
        return 11
    else:
        return int(carta)

def calcular_pontuacao(mao):
    total = sum(valor_carta(carta) for carta in mao)

    # Ajuste do Ás
    ases = mao.count('A')
    while total > 21 and ases:
        total -= 10
        ases -= 1

    return total

def mostrar_mao(nome, mao, esconder_primeira=False):
    if esconder_primeira:
        print(f"{nome}: ['?'] + {mao[1:]}")
    else:
        print(f"{nome}: {mao} (Total: {calcular_pontuacao(mao)})")

def jogar():
    while jogador["saldo"] > 0:
        print("\n===== NOVA RODADA =====")
        print(f"Saldo: {jogador['saldo']}")

        aposta = int(input("Quanto deseja apostar? "))
        if aposta > jogador["saldo"]:
            print("Saldo insuficiente!")
            continue

        baralho = criar_baralho()

        jogador_mao = [baralho.pop(), baralho.pop()]
        casa_mao = [baralho.pop(), baralho.pop()]

        while True:
            mostrar_mao("Você", jogador_mao)
            mostrar_mao("Casa", casa_mao, esconder_primeira=True)

            if calcular_pontuacao(jogador_mao) > 21:
                print("Você estourou!")
                jogador["saldo"] -= aposta
                break

            escolha = input("1 - Comprar carta | 2 - Parar: ")

            if escolha == "1":
                jogador_mao.append(baralho.pop())
            else:
                break

        if calcular_pontuacao(jogador_mao) <= 21:
            while calcular_pontuacao(casa_mao) < 17:
                casa_mao.append(baralho.pop())

            print("\n===== RESULTADO =====")
            mostrar_mao("Você", jogador_mao)
            mostrar_mao("Casa", casa_mao)

            jogador_total = calcular_pontuacao(jogador_mao)
            casa_total = calcular_pontuacao(casa_mao)

            if casa_total > 21 or jogador_total > casa_total:
                print("Você ganhou!")
                jogador["saldo"] += aposta
            elif jogador_total < casa_total:
                print("Você perdeu")
                jogador["saldo"] -= aposta
            else:
                print("Empate")

        if jogador["saldo"] <= 0:
            print("Você ficou sem saldo!")
            break

        sair = input("Deseja continuar? (s/n): ")
        if sair.lower() != 's':
            break

jogar()
