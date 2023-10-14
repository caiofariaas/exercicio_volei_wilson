pontos = list()
time = list()

print("-=" * 20)
qtdJogadores = int(input("Quantos jogadores deseja adicionar? "))

for s in range(qtdJogadores):
    pontos.clear()
    jogadores = dict()

    print("-=" * 20)
    jogadores['Codigo'] = s+1
    posicao = "Jogador"
    jogadores[posicao] = input(f"Qual o nome do jogador {s + 1}: ")

    escolha = input("Esse jogador jogou alguma partida? ")
    escolha = escolha.lower()

    if escolha == "sim":
        partidas = int(input("Digite quantas partidas ele jogou: "))

        for pt in range(partidas):
            pontos.append(int(input(f"Quantos pontos ele fez na partida {pt + 1}: ")))
        jogadores['pontos'] = pontos[:]
        jogadores['total'] = sum(pontos)

    time.append(jogadores)
    print("-=" * 20)
    print("\nAqui estão todos os jogadores que você adicionou")

    for i, jogador in enumerate(time):
        print(f"\n{jogador}")

print("-=" * 20)
escolha1 = input("\nDeseja consultar algum jogador especifico? (sim/nao): ")
escolha1 = escolha1.lower()

if escolha1 == "sim":
    codigo = int(input("Digite o código do jogador: "))

    jogador_procurado = None

    for j in time:
        if j.get('Codigo') == codigo:
            jogador_procurado = j
            break

    if jogador_procurado:
        print("\n" + "-=" * 20)
        print(f"Jogador encontrado: {jogador_procurado}")
        print("-=" * 20)
    else:
        print("Jogador não encontrado.")
elif escolha1 == "nao":
    print("Até a próxima")
else:
    print("Valor Inválido")
