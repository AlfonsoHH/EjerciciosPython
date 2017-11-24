import Persona

nombre = input("Nombre del sujeto: ")
edad = int(input("¿Qué edad tiene el sujeto?"))
sexo = input("Sexo del sujeto (Responde con H para hombre y M para mujer: ")
peso = float(input("¿Cuánto pesa el sujeto?"))
altura = float(input("¿Cuánto mide el sujeto?"))

p1 = Persona.Persona(nombre, edad, sexo, peso, altura)

nombre = input("Nombre del segundo sujeto: ")
edad = int(input("¿Qué edad tiene el segundo sujeto?"))
sexo = input("Sexo del segundo sujeto (Responde con H para hombre y M para mujer: ")

p2 = Persona.Persona(nombre, edad, sexo)
p2.set_peso(65)
p2.set_altura(1.65)

p3 = Persona.Persona()
p3.set_nombre(input("Nombre del tercer sujeto: "))
p3.set_edad(int(input("¿Qué edad tiene el tercer sujeto?")))
p3.set_sexo(input("Sexo del tercer sujeto (Responde con H para hombre y M para mujer: "))
p3.set_peso(float(input("¿Cuánto pesa el tercer sujeto?")))
p3.set_altura(float(input("¿Cuánto mide el tercer sujeto?")))

p1.calcularIMC()
p2.calcularIMC()
p3.calcularIMC()

p1.toString()
p2.toString()
p3.toString()

