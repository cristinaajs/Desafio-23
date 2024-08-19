import random

def nome_jogador():
    nome = input("Insira o nome do jogador: ")
    return nome

def escolha_do_jogador():
    escolha = input("Escolha pedra, papel ou tesoura: ")
    return escolha

def computador_escolhe():
    opcoes = ["pedra", "papel", "tesoura"]
    return random.choice(opcoes)

def vencedor(jogador, jogada, computador):
    if jogada == computador: 
        return "empate"
    elif (jogada == "pedra" and computador == "tesoura") or \
         (jogada == "tesoura" and computador == "papel") or \
         (jogada == "papel" and computador == "pedra"):
        return jogador
    else:
        return "computador"
    
def jogo():
    vencido = 0
    perdido = 0
    empate = 0

    nome = nome_jogador()
    while True:
        
        jogada = escolha_do_jogador()
        computador = computador_escolhe()

        print(f"A escolha de {nome} foi: {jogada}")
        print(f"A escolha do computador foi: {computador}")

        resultado = vencedor(nome, jogada, computador)

        if resultado == "empate":
            print("Empate!")
            empate +=1
        elif resultado == nome:
            print(f"{nome}, você venceu!")
            vencido +=1
        else:
            print("Você perdeu!")
            perdido +=1

        jogar_novamente = input("Deseja jogar novamente? (sim/ não: ").lower()
        if jogar_novamente !=  'sim':
            break

        print(f"O vencedor é: {resultado}")
        print(f"Vitórias: {vencido}")
        print(f"Derrotas: {perdido}")
        print(f"Empates: {empate}")

    print(f"O vencedor é: {resultado}")
    print(f"Vitórias: {vencido}")
    print(f"Derrotas: {perdido}")
    print(f"Empates: {empate}")

jogo()



