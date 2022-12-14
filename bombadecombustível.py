# -*- coding: utf-8 -*-
"""bombadecombustível.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ujhNYtOK01h_noHOxbdKfsy9VyiIH5t8
"""

class BombaPosto:

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abstecerPorValor(self, valor):
        litros = valor/self.valorLitro
        self.abstecerPorLitro(litros)

    def abstecerPorLitro(self, litros):
        if litros > 0 and (self.quantidadeCombustivel - litros >= 0):
            self.quantidadeCombustivel -= litros

    def alterarValor(self, valor):
        if valor > 0:
            self.valorLitro = valor

    def alterarCombustivel(self, tipo):
        self.tipoCombustivel = tipo

    def alterarQuantidadeCombustivel(self, quantidade):
        if quantidade >= 0:
            self.quantidadeCombustivel = quantidade

    def __str__(self):
        return "Tipo de combustivel: {}\nPreço: R${:.2f} \nQuantidade: {:.2f}l".\
            format(self.tipoCombustivel, self.valorLitro, self.quantidadeCombustivel)

if __name__ == '__main__':
    bomba = BombaPosto("Gasolina", 7, 100)
    while True:
        try:
            print("---------------Menu-------------------")
            print("1 - Abastecer por litro")
            print("2 - Abstecer por valor")
            print("3 - Alterar quantidade de combustivel")
            print("4 - Alterar  tipo do combustivel")
            print("5 - Alterar preço do combustivel")
            print("6 - Informação")
            print("0 - sair")
            opcao = int(input(">>> "))
            if opcao == 1:
                while True:
                    try:
                        quantidade = float(input("Digite a quantidade de combustivel(l): "))
                        if quantidade > 0:
                            bomba.abstecerPorLitro(quantidade)
                            print("Quantindade de combustivel restante: %.2fl"%(bomba.quantidadeCombustivel))
                            break
                        else:
                            print("Valor inválido, tente novamente")
                    except ValueError:
                        print("Valor inválido, tente novamente")
            elif opcao == 2:
                while True:
                    try:
                        valor = float(input("Digite o Valor(R$): "))
                        if valor > 0:
                            bomba.abstecerPorValor(valor)
                            print("Quantindade de combustivel restante: %.2fl"%(bomba.quantidadeCombustivel))
                            break
                        else:
                            print("Valor inválido, tente novamente")
                    except ValueError:
                        print("Valor inválido, tente novamente")
            elif opcao == 3:
                while True:
                    try:
                        quantidade = float(input("Digite a quantidade de combustivel(l): "))
                        if quantidade > 0:
                            bomba.alterarQuantidadeCombustivel(quantidade)
                            break
                        else:
                            print("Valor inválido, tente novamente")
                    except ValueError:
                        print("Valor inválido, tente novamente")

            elif opcao == 4:
                while True:
                    tipo = input("Digite o tipo de combustivel: ")
                    if tipo != "":
                        bomba.alterarCombustivel(tipo)
                        break
                    else:
                        print("Entrada vazia, tente novamente")
            elif opcao == 5:
                while True:
                    try:
                        valor = float(input("Digite o preço(R$): "))
                        if valor > 0:
                            bomba.alterarValor(valor)
                            break
                        else:
                            print("Valor inválido, tente novamente")
                    except ValueError:
                        print("Valor inválido, tente novamente")
            elif opcao == 6:
                print(bomba)
            elif opcao == 0:
                break
            else:
                print("Opção inválida")
        except ValueError:
            print("Opção inválida")