import csv

from avl import No
from voo import Voo


if __name__ == "__main__":
    capital_origem = ""
    arvore = No()

    with open("capitais.csv", encoding="utf-8") as arquivo_capitais:
        tabela = csv.reader(arquivo_capitais, delimiter=",")
        tabela.__next__()
        for linha in tabela:
            capital_destino = str(linha[0])
            distancia = int(linha[1])

            if distancia == 0:
                capital_origem = str(linha[0])
                # print(f"{capital_origem} - {capital_destino} - {distancia}Km")

                voo = Voo(capital_origem, capital_destino, distancia)
                arvore.data = voo
            else:
                # print(f"{capital_origem} - {capital_destino} - {distancia}Km")
                voo = Voo(capital_origem, capital_destino, distancia)
                arvore.insere(voo)

        arvore.imprime_arvore()
        arvore.rotacao_esquerda()
        arvore.imprime_arvore()