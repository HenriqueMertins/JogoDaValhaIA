#HENRIQUE MERTINS
class JogoDaVelha:
    #tabuleiro
    tabuleiro = {'7': ' ', '8': ' ', '9': ' ',
                 '4': ' ', '5': ' ', '6': ' ',
                 '1': ' ', '2': ' ', '3': ' '}
    turno = None

    #decide quem vai comecar o jogo
    def __init__(self, jogador_inicial="X"):
        self.turno = jogador_inicial

    # print do tabuleiro
    def exibir_tabuleiro(self):
        print("┌───┬───┬───┐")
        print(f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
        print("└───┴───┴───┘")

    def verificar_jogada(self, jogada):
        if jogada in self.tabuleiro.keys():
            if self.tabuleiro[jogada] == " ":
                return True
        return False

    def verificar_tabuleiro(self):
        # Verificações das 3 verticais
        if self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != ' ':
            return self.tabuleiro['8']
        elif self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['9']

        # Verificações das 3 horizontais
        elif self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != ' ':
            return self.tabuleiro['8']
        elif self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['1']

        # Verificações das 2 diagonais
        elif self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['1'] == self.tabuleiro['5'] == self.tabuleiro['9'] != ' ':
            return self.tabuleiro['1']

        # Verificando empate
        if [*self.tabuleiro.values()].count(' ') == 0:
            return "empate"
        else:
            return None

    # inteligencia artificial tomada de desição
    # tabuleiro: estado atual, profundidade: arvore de busca, maximizando: indica o turno do maximizando ou minimizando
    # maximizando: x, true, minimizando: o, false

    #literalmente verifica o tabuleiro
    def minimax(self, tabuleiro, profundidade, maximizando):
        resultado = self.verificar_tabuleiro()

        if resultado is not None:
            if resultado == "empate":
                return 0
            elif resultado == "X":
                return 1
            elif resultado == "O":
                return -1

        if maximizando:
            melhor_pontuacao = -float("inf")
            for jogada in tabuleiro.keys():
                if tabuleiro[jogada] == ' ':
                    tabuleiro[jogada] = "X"
                    pontuacao = self.minimax(tabuleiro, profundidade + 1, False)
                    tabuleiro[jogada] = ' '
                    melhor_pontuacao = max(pontuacao, melhor_pontuacao)
            return melhor_pontuacao
        else:
            melhor_pontuacao = float("inf")
            for jogada in tabuleiro.keys():
                if tabuleiro[jogada] == ' ':
                    tabuleiro[jogada] = "O"
                    pontuacao = self.minimax(tabuleiro, profundidade + 1, True)
                    tabuleiro[jogada] = ' '
                    melhor_pontuacao = min(pontuacao, melhor_pontuacao)
            return melhor_pontuacao

    def jogada_computador(self):
        if self.turno == "X":
            melhor_pontuacao = -float("inf")
            melhor_jogada = None

            for jogada in self.tabuleiro.keys():
                if self.tabuleiro[jogada] == ' ':
                    self.tabuleiro[jogada] = "X"
                    pontuacao = self.minimax(self.tabuleiro, 0, False)
                    self.tabuleiro[jogada] = ' '

                    if pontuacao > melhor_pontuacao:
                        melhor_pontuacao = pontuacao
                        melhor_jogada = jogada

            self.tabuleiro[melhor_jogada] = "X"
        else:
            melhor_pontuacao = float("inf")
            melhor_jogada = None

            for jogada in self.tabuleiro.keys():
                if self.tabuleiro[jogada] == ' ':
                    self.tabuleiro[jogada] = "O"
                    pontuacao = self.minimax(self.tabuleiro, 0, True)
                    self.tabuleiro[jogada] = ' '

                    if pontuacao < melhor_pontuacao:
                        melhor_pontuacao = pontuacao
                        melhor_jogada = jogada

            self.tabuleiro[melhor_jogada] = "O"

    def jogar(self):

        while True:
            self.exibir_tabuleiro()

            print(f"Turno do {self.turno}, qual sua jogada?")

            if self.turno == "X":
                self.jogada_computador()
            else:
                jogada = input("Jogada: ")

                if not self.verificar_jogada(jogada):  # Se a jogada for válida...
                    break  # Encerra o loop
                

                self.tabuleiro[jogada] = self.turno

          

            estado = self.verificar_tabuleiro()

            if estado == "X":
                self.exibir_tabuleiro()
                print("X é o vencedor!!!")
                break

            elif estado == "O":
                self.exibir_tabuleiro()
                print("O é o vencedor!!!")
                break
            #empetaaaa (pra ficar bom sempre tem que dar empate)
            if estado == "empate":
                self.exibir_tabuleiro()
                print("EMPATE!!!")
                break

            # Troca o jogador do próximo turno
            self.turno = "X" if self.turno == "O" else "O"

# Iniciar o jogo
jogo = JogoDaVelha()
jogo.jogar()
