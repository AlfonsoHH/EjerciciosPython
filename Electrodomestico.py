

class Electrodomestico(object):

    def __init__(self,precioBase=100.0,color="blanco",consumoEnergetico="F",peso=5.0):
        self.precioBase=precioBase
        self.color=color
        self.consumoEnergetico=consumoEnergetico
        self.peso=peso

    def get_precioBase(self):
        return self.precioBase

    def get_color(self):
        return self.color

    def get_consumoEnergetico(self):
        return self.consumoEnergetico

    def get_peso(self):
        return self.peso

    def comprobarCosumoEnergetico(self, letra):
        correcto = False

        letraCorrecta = {'A': True, 'B': True, 'C': True, 'D': True, 'E': True, 'F': True}

        correcto = letraCorrecta[letra]

        if correcto:
            return letra
        else:
            return"F"

    def comprobarColor(self, color):
        if color.lower()=="blanco" or color.lower()=="negro" or color.lower()=="rojo" or color.lower()=="azul" or color.lower()=="gris":
            return color
        else:
            return "blanco"

    def precioFinal(self):
        tipoAumento = {'A': 100.0, 'B': 80.0, 'C': 60.0, 'D': 50.0, 'E': 30.0, 'F': 10.0}

        aumento = tipoAumento[self.consumoEnergetico]

        self.precioBase=self.precioBase+aumento

        if self.peso<20:
            aumento=10.0
        elif self.peso>19 and self.peso<50:
            aumento=50.0
        elif self.peso > 49 and self.peso < 80:
            aumento = 80.0
        else:
            aumento=100.0

        self.precioBase = self.precioBase + aumento





