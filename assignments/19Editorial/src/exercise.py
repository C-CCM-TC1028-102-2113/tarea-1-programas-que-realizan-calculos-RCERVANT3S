#Publicación en una editorial
import math
def main():
    #escribe tu código abajo de esta línea
    pass

palabras=int(input("Dame el número de palabras:"))
 

páginas = 1

if palabras > 475:
    
    redondeado = math.ceil(palabras / 475)
    páginas = redondeado * páginas
    páginas = páginas * 60
    páginas = páginas * .9
    print("El costo de la publicación es:",páginas)


else:
    
    páginas = 60
    páginas = páginas * .9

    print("El costo de la publicación es:",páginas)


if __name__ == '__main__':
    main()
