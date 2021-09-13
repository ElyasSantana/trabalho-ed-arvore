class Voo:
    vooId = 1

    def __init__(self, capital_origem, capital_destino, distancia):
        self.voo_id = Voo.vooId
        Voo.vooId = self.voo_id + 1
        self.capital_origem = capital_origem
        self.capital_destino = capital_destino
        self.distancia = distancia


class ArvoreDeVoos:
    def __init__(self, voo=None):
        if voo:
            self.root = voo
        else:
            self.root = None

    def voo_raiz(self, voo=None):
        if voo is None:
            voo = self.root
            print(voo.voo_id)
