import Electrodomestico

class Lavadora(Electrodomestico.Electrodomestico):

    def __init__(self,precioBase=100.0,color="blanco",consumoEnergetico="F",peso=5.0,carga=5.0):
        super().__init__(precioBase,color,consumoEnergetico,peso)
        self.carga=carga

    def get_carga(self):
        return self.carga

    def precioFinal(self):
        if self.carga>30:
            self.precioBase=self.precioBase+50.0