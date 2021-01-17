class Carro:
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def dirigir(self):
        acao = None
        while acao != "S":
            acao = input("...aguardando ação: (A:acelerar) (F:freiar) (VD:virar a direita) (VE: virar a esquerda) (S:sair)")
            if acao == "A":
                nivelaceleracao = self.motor.acelerar()
                if nivelaceleracao == "vc passou de 10 e perdeu o controle!":
                    print(nivelaceleracao)
                    break
                else:
                    print(nivelaceleracao)
            elif acao == "F":
                print(self.motor.freiar())
            elif acao == "VD":
                print(self.direcao.mudardirecao("VD"))
            elif acao == "VE":
                print(self.direcao.mudardirecao("VE"))
        return print("Voce parou de dirigir")

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1
        if self.velocidade <= 10:
            return "Sua velocidade é " + str(self.velocidade)
        else:
            return "vc passou de 10 e perdeu o controle!"

    def freiar(self):
        if self.velocidade == 1:
            self.velocidade = 0
            return "Sua velocidade é " + str(self.velocidade)
        elif self.velocidade >=2:
            self.velocidade -= 2
            return "Sua velocidade é " + str(self.velocidade)
        else:
            return "Vc já está parado, sua velocidade é " + str(self.velocidade)

class Direcao:
    def __init__(self):
        self.direcoes = ["Norte", "Leste", "Sul", "Oeste"]
        self.auxdirecoes = 0
        self.direcao_carro = self.direcoes[self.auxdirecoes]
    def mudardirecao(self, direcao_escolhida):
        if direcao_escolhida == "VD":
            if self.auxdirecoes < 3 and self.auxdirecoes >= -4:
                self.auxdirecoes += 1
                self.direcao_carro = self.direcoes[self.auxdirecoes]
                return "a direção é " + str(self.direcao_carro)
            else:
                self.auxdirecoes = 0
                self.direcao_carro = self.direcoes[self.auxdirecoes]
                return "a direção é " + str(self.direcao_carro)
        if direcao_escolhida == "VE":
            if self.auxdirecoes <= 3 and self.auxdirecoes > -4:
                self.auxdirecoes -= 1
                self.direcao_carro = self.direcoes[self.auxdirecoes]
                return "a direção é " + str(self.direcao_carro)
            else:
                self.auxdirecoes = 3
                self.direcao_carro = self.direcoes[self.auxdirecoes]
                return "a direção é " + str(self.direcao_carro)

meucarro = Carro(motor=Motor(),direcao=Direcao())
meucarro.dirigir()