import Electrodomestico
import Lavadora
import Television

e1 = Electrodomestico.Electrodomestico(200.0,"gris","B",34.0)
e2 = Electrodomestico.Electrodomestico(540.0,"negro","D",62.0)
l1 = Lavadora.Lavadora(700.0,"blanco","C",69.0,7.3)
e3 = Electrodomestico.Electrodomestico(450.0,"azul","F",17.0)
t1 = Television.Television(700.0,"negro","A",20.0,45,True)
l2 = Lavadora.Lavadora(370.0,"gris","D",47.0,5.0)
e4 = Electrodomestico.Electrodomestico(120.0,"rojo","C",24.0)
t2 = Television.Television(200.0,"gris","F",34.0,34.0,False)
e5 = Electrodomestico.Electrodomestico(340.0,"blanco","A",39.0)
t3 = Television.Television(560.0,"rojo","C",16.0,50.0,True)

lista=(e1,e2,l1,e3,t1,l2,e4,t2,e5,t3)

for elemento in lista:
    elemento.precioFinal()

precioFinal=0.0
precioFinalLV=0.0
precioFinalTV=0.0

for electro in lista:
    precioFinal=precioFinal+electro.precioBase
    if isinstance(electro,Lavadora.Lavadora):
        precioFinalLV = precioFinalLV + electro.precioBase
    if isinstance(electro,Television.Television):
        precioFinalTV = precioFinalTV + electro.precioBase

print("Todos los electrodomesticos valen en conjunto "+str(precioFinal))
print("Todas las lavadoras valen en conjunto "+str(precioFinalLV))
print("Todas las televisiones valen en conjunto "+str(precioFinalTV))