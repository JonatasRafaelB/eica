from braser.vitollino import Actor
from . import Ponto

IMG = "https://dl.dropboxusercontent.com/u/1751704/igames/img/"
BALONX, BALONY = 0, 70
TABUAX, TABUAY, TABUAS = 400, 120, 90
FALAX, FALAY, FALASEPARA = 100, 550, 100
ABAS = 80


class Aba(Actor):
    def __init__(self, chave, tab, x=BALONX, y=BALONY):
        super().__init__()  # super é invocado aqui para preservar os poderes recebidos do Circus
        self.aba = tab
        self.celula = None
        self.chave, self.x, self.y = chave, x, y

    def create(self):
        self.celula = self.sprite(self.chave.ladrilho_coisa, self.x, self.y)
        self.celula.scale.setTo(2.5, 2.5)
        self.celula.inputEnabled = True
        self.celula.frame = 0  # 160
        self.celula.events.onInputDown.add(lambda _=0, __=0: self.mostra_abas(self.chave, self.aba), self)
        self.chave.jogo.add(self.celula)

    def mostra_abas(self, chave, proxima):
        """Aqui colocamos o sprite do homem e selecionamos o frame que o representa"""
        print("mostra_abas", proxima.nome, chave.aba_corrente.nome)
        chave.aba_corrente.mostra(False)
        proxima.mostra(True)
        self.score(evento=Ponto(x=self.x, y=self.y), carta=chave.aba_corrente.nome, ponto="_ABAS_", valor=proxima.nome)
        chave.aba_corrente = proxima


class Celula(Actor):
    def __init__(self, chave, tab, x=BALONX, y=BALONY):
        super().__init__()  # super é invocado aqui para preservar os poderes recebidos do Circus
        self.celula = tab
        self.chave, self.x, self.y = chave, x, y

    def create(self):
        self.celula = self.sprite(self.chave.ladrilho_coisa, self.x, self.y)
        self.celula.scale.setTo(2.5, 2.5)
        self.celula.inputEnabled = True
        self.celula.frame = 160
        self.celula.events.onInputDown.add(lambda _=0, __=0: self.recebe(self.chave.aba_corrente.seleto), self)

    def recebe(self, item):
        if not item:
            return
        item.x, item.y = self.x + 40, self.y + 40
        self.score(evento=Ponto(x=item.x, y=item.y), carta="0", ponto="_CHAVE_", valor=item.frame)


class Chaves(Actor):
    """Essa  é a classe Chaves que recebe os poderes da classe Circus de poder criar um jogo"""

    def __init__(self, x=BALONX, y=BALONY):
        super().__init__()  # super é invocado aqui para preservar os poderes recebidos do Circus
        self.aba_corrente = self.aba = None
        # self.abas = "fruta objeto animal arma"
        self.ladrilho_coisa = "objeto"
        self.ladrilho_fruta = "fruta"
        self.ladrilho_animal = "animal"
        self.ladrilho_arvore = "arvore"
        self.ladrilho_fala = "chave"
        self.fala = self.falou = self.pensa = None
        self.fruta = self.animal = self.comida = None
        self.arvore = self.arma = self.objeto = None
        self.x, self.y = x, y
        self.jogo = None
        self.cria_tabuleiro()
        self.take_propils()
        self.abas = [self.fruta, self.animal, self.comida, self.arma, self.objeto,
                     self.fruta, self.animal, self.comida, self.arma, self.objeto]
        self.ativo = True

    def ativa(self):
        """Abre o balão de conversa"""
        self.score(evento=Ponto(x=0, y=0), carta="0", ponto="_CHAVES_", valor=self.ativo)
        self.jogo.visible = self.ativo
        # self.tween(self.fala, 2000, repeat=0, alpha=1)
        for aba in self.abas:
            aba.mostra(False)
        self.aba_corrente.mostra(self.ativo)
        self.ativo = not self.ativo

    def preload(self):
        """Aqui no preload carregamos a imagem mundo e a folha de ladrilhos dos homens"""
        self.spritesheet(self.ladrilho_fruta, IMG + "fruit.png", 65, 65, 8 * 8)
        self.spritesheet(self.ladrilho_animal, IMG + "largeemoji.png", 47.5, 47, 14 * 9)
        self.spritesheet(self.ladrilho_coisa, IMG + "cacarecos.png", 32, 32, 16 * 16)
        self.spritesheet(self.ladrilho_arvore, IMG + "treesprites1.png", 123.5, 111, 4 * 3)
        self.image(self.ladrilho_fala, IMG + "jogo_chaves.jpg")

    def take_propils(self):
        """Jogador escreve: hominídeo comer fruta_vermelha."""
        self.fruta = Take(self, self.ladrilho_fruta, 0, self.x + FALAX, self.y + FALAY)
        self.animal = Take(self, self.ladrilho_animal, 4 * 14 + 7, self.x + FALAX, self.y + FALAY)
        self.comida = Take(self, self.ladrilho_coisa, 5 * 16 + 6, self.x + FALAX, self.y + FALAY)
        # self.arvore = Take(self, self.ladrilho_arvore, 0, self.x+FALAX+FALASEPARA*2, self.y+FALAY)
        self.arma = Take(self, self.ladrilho_coisa, 16 * 4, self.x + FALAX, self.y + FALAY)
        self.objeto = Take(self, self.ladrilho_coisa, 16 + 7, self.x + FALAX, self.y + FALAY)
        self.aba_corrente = self.fruta

    def mostra_abas(self, corrente, proxima):
        """Aqui colocamos o sprite do homem e selecionamos o frame que o representa"""
        print("mostra_abas", proxima.nome)
        corrente.mostra(False)
        proxima.mostra(True)

        self.aba_corrente = proxima

    def cria_abas(self):
        """Aqui colocamos o sprite do homem e selecionamos o frame que o representa"""
        for x in range(10):
            Aba(self, self.abas[x], FALAX - ABAS + x * ABAS, FALAY - 50)

    def cria_tabuleiro(self):
        """Aqui colocamos o sprite do homem e selecionamos o frame que o representa"""
        for x in range(4):
            for y in range(4):
                pass
                tab = None  # self.sprite(self.ladrilho_coisa, TABUAX + x * TABUAS * 1.1, TABUAY + y * TABUAS)
                Celula(self, tab, TABUAX + x * TABUAS * 1.1, TABUAY + y * TABUAS)

    def create(self):
        """Aqui colocamos o sprite do homem e selecionamos o frame que o representa"""
        self.fala = self.sprite(self.ladrilho_fala, self.x, self.y)
        self.jogo = self.group()
        self.fala.scale.setTo(2, 2)
        self.jogo.add(self.fala)
        self.jogo.visible = False

        def up(_=None, __=None):
            self.aba_corrente.rola(-1)

        def down(_=None, __=None):
            self.aba_corrente.rola(1)

        self.aba = self.group()
        self.aba.visible = False
        sobe = self.sprite(self.ladrilho_animal, self.x, self.y + FALAY - 20)
        sobe.inputEnabled = True
        desce = self.sprite(self.ladrilho_animal, self.x + 750, self.y + FALAY - 20)
        sobe.frame = 14 * 9 - 4
        desce.inputEnabled = True
        desce.frame = 14 * 9 - 5
        sobe.events.onInputDown.add(up, self)
        desce.events.onInputDown.add(down, dict(b=1))
        self.jogo.add(sobe)
        self.jogo.add(desce)
        self.cria_abas()
        self.jogo.visible = False


class Take(Actor):
    """Essa  é a classe Take que controla os personagens do jogo"""

    def __init__(self, chaves, nome, frame, x, y):
        super().__init__()
        self.chaves, self.nome, self.frame, self.x, self.y = chaves, nome, frame, x, y
        self.aba = self.coisas = self.fala = self.jogo = None
        self.seleto = None

    def mostra(self, muda):
        """ Mostra esta aba

        :param muda: booleano que diz se é para mostar ou ocultar a aba
        :return: None
        """
        self.aba.visible = muda

    def rola(self, desloca):
        """Aqui rolamos o conjunto de sprites mudando o frame de cada sprite"""
        self.frame = self.frame + desloca if self.frame + desloca > 0 else 0
        for frame, coisa in enumerate(self.coisas):
            print(frame, coisa.frame)
            coisa.frame = self.frame + frame

    def create(self):
        """Aqui colocamos o sprite do homem e selecionamos o frame que o representa"""
        self.aba = self.group()
        self.aba.visible = False
        self.coisas = [self._create(coisa) for coisa in range(0, 8)]

    def _create(self, frame):
        """Aqui colocamos o sprite do icon e adicionamos no seletor de aba"""
        coisa = self._copy(frame)
        self.aba.add(coisa)
        # self.chaves.jogo.add(coisa)
        return coisa

    def _copy(self, frame):
        """Aqui colocamos o sprite do icon e selecionamos o frame que o representa"""
        coisa = self.sprite(self.nome, self.x + 50 * frame, self.y)
        coisa.frame = self.frame + frame
        coisa.inputEnabled = True
        coisa.input.useHandCursor = True
        coisa.events.onInputDown.add(lambda a=None, b=frame, c=frame: self._click(b, c), dict(b=frame))
        coisa.anchor.setTo(0.5, 0.5)
        return coisa

    def activate(self):
        self.aba.visible = True

    def _click(self, _=None, d=None):
        """ Seleciona o ícone que vai mover

        :param d:
        :return:
        """
        print("action", d)
        self.seleto = self._copy(d)
        self.chaves.jogo.add(self.seleto)

    def update(self):
        pass
