import random

def criar_baralho(cartas_retiradas=[]):
    naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei', 'Ás']
    baralho = [(valor, naipe) for naipe in naipes for valor in valores if (valor, naipe) not in cartas_retiradas]
    random.shuffle(baralho)
    return baralho

def valor_carta(cartas):
    valores = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'Valete': 10, 'Dama': 10, 'Rei': 10, 'Ás': 11}
    valor_total = sum(valores[carta[0]] for carta in cartas)
    num_as = sum(1 for carta in cartas if carta[0] == 'Ás')
    while valor_total > 21 and num_as:
        valor_total -= 10
        num_as -= 1
    return valor_total

def mostrar_cartas(mao, jogador):
    nome_jogador = "Jogador" if jogador else "Banca"
    print(f"{nome_jogador}:")
    for carta in mao:
        print(f"   {carta[0]} de {carta[1]}")

def jogar_blackjack():
    baralho = criar_baralho()
    cartas_retiradas = []
    mao_jogador = [baralho.pop(), baralho.pop()]
    mao_banca = [baralho.pop(), baralho.pop()]
    cartas_retiradas.extend(mao_jogador + mao_banca)

    while True:
        #mostrar_cartas(mao_jogador, True)
        #mostrar_cartas(mao_banca, False)

        if valor_carta(mao_jogador) > 21:
            return 0 #("Você estourou! Banca vence.")
            break
        elif valor_carta(mao_jogador) == 21:
            return 1 #("Blackjack! Você vence!")
            break

        # Condições automáticas para pedir carta
        if mao_banca[0][0] in ['2', '3']:
            if valor_carta(mao_jogador) < 13:
                mao_jogador.append(baralho.pop())
        elif mao_banca[0][0] in ['4', '5', '6']:
            if valor_carta(mao_jogador) < 12:
                mao_jogador.append(baralho.pop())
        else:
            if valor_carta(mao_jogador) < 17:
                mao_jogador.append(baralho.pop())

        # Condição 2
        while valor_carta(mao_banca) < 17:
            mao_banca.append(baralho.pop())

        #mostrar_cartas(mao_jogador, True)
        #mostrar_cartas(mao_banca, False)

        if valor_carta(mao_jogador) > 21:
            return 0 #"Você estourou! Banca vence."
            break
        elif valor_carta(mao_banca) > 21:
            return 1 #"Banca estourou! Você vence!"
            break
        elif valor_carta(mao_banca) == valor_carta(mao_jogador):
            return 1 #"Empate"
            break
        elif valor_carta(mao_banca) > valor_carta(mao_jogador):
            return 0  #"Banca vence."
            break
        else:
            return 1 #"Você vence!"
            break

historico = []
n = 1000000 #Quantidade de partidas
for i in range(n):
    historico.append(jogar_blackjack())

vitorias = historico.count(1)
derrotas = historico.count(0)

print("Sua taxa de vitória é de:{:.4f}".format(vitorias/n))
print("Sua taxa de derrotas é de:{:.4f}".format(derrotas/n))