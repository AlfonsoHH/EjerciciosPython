class Videojuego:

    def __init__(self,titulo="",horasEstimadas=10,entregado=False,genero="",compania=""):
        self.titulo=titulo
        self.horasEstimadas=horasEstimadas
        self.entregado=entregado
        self.genero=genero
        self.compania=compania

    def get_titulo(self):
        return self.titulo

    def get_horasEstimadas(self):
        return self.horasEstimadas

    def get_genero(self):
        return self.genero

    def get_compania(self):
        return self.compania

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_horasEstimadas(self, horasEstimadas):
        self.horasEstimadas = horasEstimadas

    def set_genero(self, genero):
        self.genero = genero

    def set_compania(self, compania):
        self.compania = compania

    def entregar(self):
        self.entregado=True