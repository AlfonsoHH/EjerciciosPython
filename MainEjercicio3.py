import Serie
import Videojuego

listaSeries = [None] * 5
listaVideojuegos = [None] * 5

s1 = Serie.Serie("Madmen",7,True,"Drama","Matthew Weiner")
s2 = Serie.Serie("Game of Thrones",8,False,"Fantasia","George RR Martin")
s3 = Serie.Serie("Vikings",5,False,"Historica","Michael Hirst")
s4 = Serie.Serie("The Office",9,True,"Comedia","Greg Daniels")
s5 = Serie.Serie("The Wire",5,False,"Policiaca","	David Simon")

listaSeries = (s1,s2,s3,s4,s5)

v1 = Videojuego.Videojuego("Journey",8,False,"Exploración","Thatgamecompany")
v2 = Videojuego.Videojuego("Rogue Legacy",50,True,"Plataformas","Cellar Door Games")
v3 = Videojuego.Videojuego("Lemmings",40,False,"Puzzle","DMA Design")
v4 = Videojuego.Videojuego("Day of Tentacle",16,True,"Aventura Gráfica","LucasArts")
v5 = Videojuego.Videojuego("The Last of Us",30,False,"Aventura","Naughty Dog")

listaVideojuegos = (v1,v2,v3,v4,v5)

s2.entregar()
s5.entregar()
v1.entregar()
v3.entregar()

contarSeries = 0
for element in listaSeries:
    if element.entregado:
        print("La serie "+element.titulo+" ha sido entragada.")
        contarSeries=contarSeries+1

contarVideojuegos = 0
for element in listaVideojuegos:
    if element.entregado:
        print("El videojuego " + element.titulo + " ha sido entragado.")
        contarVideojuegos = contarVideojuegos+1

print("Hay "+str(contarSeries)+" series entregadas y "+str(contarVideojuegos)+" videojuegos entregados")

titulo = ""
horasMax = 0
for element in listaVideojuegos:
    if element.horasEstimadas>horasMax:
        horasMax = element.horasEstimadas
        titulo = element.titulo

print(titulo+" es el videojuego con más horas estimadas de juego, con "+str(element.horasEstimadas)+" horas de juego.")

