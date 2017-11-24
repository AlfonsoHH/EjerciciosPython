
class Serie:

    def __init__(self,titulo="",numeroTemporadas=3,entregado=False,genero="",creador=""):
        self.titulo=titulo
        self.numeroTemporadas=numeroTemporadas
        self.entregado=entregado
        self.genero=genero
        self.creador=creador

    def get_titulo(self):
        return self.titulo

    def get_numeroTemporadas(self):
        return self.numeroTemporadas

    def get_genero(self):
        return self.genero

    def get_creador(self):
        return self.creador

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_numeroTemporadas(self, numeroTemporadas):
        self.numeroTemporadas = numeroTemporadas

    def set_genero(self, genero):
        self.genero = genero

    def set_creador(self, creador):
        self.creador = creador

    def toString(self):
        print(self.titulo+" "+str(self.numeroTemporadas)+" "+self.genero+" "+self.creador)

    def entregar(self):
        self.entregado=True

