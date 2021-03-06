# from enum import Enum     # for enum34, or the stdlib version
# from aenum import Enum  # for the aenum version

IMG = "https://dl.dropboxusercontent.com/u/1751704/igames/img/"


def enum(**enums):
    return type('Enum', (), enums)


# Ponto = enum('Ponto', 'x y')
class Ponto:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __repr__(self):
        return self.x, self.y


class Recurso:    
    def __init__(self, n, y, dx=0., dy=0., size=0):
        self.n, self.recurso, self.dx, self.dy, self.size = n, y, dx, dy, size

    def __repr__(self):
        return self.n

    def all(self):
        return self.n, self.recurso, self.dx, self.dy, self.size

    def img(self):
        return self.n, self.recurso


class Folha:
    coisa = Recurso("objeto", IMG + "cacarecos.png", 32, 32, 16 * 16)
    comida = Recurso("objeto", IMG + "cacarecos.png", 32, 32, 16 * 16)
    arma = Recurso("objeto", IMG + "cacarecos.png", 32, 32, 16 * 16)
    objeto = Recurso("objeto", IMG + "cacarecos.png", 32, 32, 16 * 16)
    fruta = Recurso("fruta", IMG + "fruit.png", 65, 65, 8 * 8)
    animal = Recurso("animal", IMG + "largeemoji.png", 47.5, 47, 14 * 9)
    arvore = Recurso("arvore", IMG + "treesprites1.png", 123.5, 111, 4 * 3)
    homem = Recurso("homem", IMG + "caveman.png", 130, 130, 5 * 2)
    fala = Recurso("chave", IMG + "balooni.png")
    chave = Recurso("fala", IMG + "jogo_chaves.jpg")
    mundo = Recurso("pensa", IMG + "thought.png")
    eica = Recurso("fundo", IMG + "eicamundo.png")

    @classmethod
    def all(cls):
        return Folha.coisa, Folha.fruta, Folha.animal, Folha.arvore

    @classmethod
    def allThing(cls):
        return Folha.fruta, Folha.comida, Folha.animal, Folha.arma, Folha.objeto
