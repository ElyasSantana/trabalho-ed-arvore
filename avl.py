#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    Árvore AVL em Python

    Copyright (c) 2009 Vindemiatrix Almuredin.
    É dada permissão para copiar, distribuir e/ou modificar este documento
    sob os termos da Licença de Documentação FAIL,
    Versão 97.545.668.112.666.002 Build 69 Release 42;
    Uma cópia da licença talvez esteja inclusa na seção entitulada
    "Licença de Documentação FAIL".
"""

from voo import Voo


class No:
    def __init__(self, data=None):
        self.data = data
        self.seta_filhos(None, None)

    def seta_filhos(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def balanco(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()
        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return prof_esq - prof_dir

    def profundidade(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()
        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return 1 + max(prof_esq, prof_dir)

    def rotacao_esquerda(self):
        self.data, self.direita.data = self.direita.data, self.data
        old_esquerda = self.esquerda
        self.seta_filhos(self.direita, self.direita.direita)
        self.esquerda.seta_filhos(old_esquerda, self.esquerda.esquerda)

    def rotacao_direita(self):
        self.data, self.esquerda.data = self.esquerda.data, self.data
        old_direita = self.direita
        self.seta_filhos(self.esquerda.esquerda, self.esquerda)
        self.direita.seta_filhos(self.direita.direita, old_direita)

    def rotacao_esquerda_direita(self):
        self.esquerda.rotacao_esquerda()
        self.rotacao_direita()

    def rotacao_direita_esquerda(self):
        self.direita.rotacao_direita()
        self.rotacao_esquerda()

    def executa_balanco(self):
        bal = self.balanco()
        if bal > 1:
            if self.esquerda.balanco() > 0:
                self.rotacao_direita()
            else:
                self.rotacao_esquerda_direita()
        elif bal < -1:
            if self.direita.balanco() < 0:
                self.rotacao_esquerda()
            else:
                self.rotacao_direita_esquerda()

    def insere(self, data):
        if data.distancia <= self.data.distancia:
            if not self.esquerda:
                self.esquerda = No(data)
            else:
                self.esquerda.insere(data)
        else:
            if not self.direita:
                self.direita = No(data)
            else:
                self.direita.insere(data)
        self.executa_balanco()

    def imprime_arvore(self, indent=0):
        print(" " * indent + str(self.data.capital_destino))
        if self.esquerda:
            self.esquerda.imprime_arvore(indent + 2)
        if self.direita:
            self.direita.imprime_arvore(indent + 2)


if __name__ == "__main__":
    voo1 = Voo("Aracaju", "Joao Pessoa", 1234)
    n1 = No(voo1)

    voo2 = Voo("Aracaju", "Recife", 687)
    n1.insere(voo2)

    voo3 = Voo("Aracaju", "São Paulo", 2090)
    n1.insere(voo3)

    voo4 = Voo("Aracaju", "Goiás", 1200)
    n1.insere(voo4)

    n1.imprime_arvore()