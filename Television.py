import Electrodomestico

class Television(Electrodomestico.Electrodomestico):

    def __init__(self,precioBase=100.0,color="blanco",consumoEnergetico="F",peso=5.0,resolucion=20,fourK=False):
        super().__init__(precioBase,color,consumoEnergetico,peso)
        self.resolucion=resolucion
        self.fourK=fourK

    def get_resolucion(self):
        return self.resolucion

    def get_fourK(self):
        return self.fourK

    def precioFinal(self):
        if self.resolucion>40.0:
            self.precioBase=self.precioBase*1.3
        if self.fourK:
            self.precioBase = self.precioBase+50.0