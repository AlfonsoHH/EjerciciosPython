from random import randint
import random
import string

class Persona:

    def __init__(self,nombre="",edad=0,sexo="M",peso=0.0,altura=0.0):
        self.nombre=nombre
        self.edad=edad
        self.DNI=self.generarDNI()
        self.sexo=sexo
        self.peso=peso
        self.altura=altura

    def calcularIMC(self):
        pesoIdeal=self.peso/(self.altura*self.altura)

        if(pesoIdeal<18.5):
            print("Estas por debajo ideal")
            return -1
        elif (pesoIdeal>=18.5 and pesoIdeal<=24.9):
            print("Estas justo en tu peso ideal")
            return 0
        else:
            print("Estas por encima de tu peso ideal")
            return 1

        return self.peso/(self.altura*self.altura)

    def esMayorDeEdad(self):
        if(self.edad<18):
            return False
        else:
            return True

    def introducirSexo(self,sexo):
        if(sexo=="M" or sexo=="H"):
            self.sexo=sexo
        else:
            self.sexo="M"

    def toString(self):
        print(self.nombre+" "+str(self.edad)+" "+self.DNI+" "+self.sexo+" "+str(self.peso)+" "+str(self.altura))


    def generarDNI(self):

        numero=randint(1,99999999)

        if(numero<10000000):
            numeroString=str(numero)
            for i in range(8-len(numeroString)):
                numeroString="0"+numeroString
        else:
            numeroString = str(numero)

        numeroString=numeroString+random.choice(string.ascii_letters.upper())

        return numeroString

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def set_sexo(self, sexo):
        self.sexo = sexo

    def set_peso(self, peso):
        self.peso = peso

    def set_altura(self, altura):
        self.altura = altura

