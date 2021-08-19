def main():
    #escribe tu código abajo de esta línea
    pass
mensajes = int(input("Dame el número mensajes:"))
megas = float(input("Dame el número megas:"))
minutos = int(input("Dame el número minutos:"))


mensajes = 0.80 * mensajes 
megas = 0.80 * megas 
minutos = 0.80 * minutos 

coste = mensajes + megas + minutos

print("El coste mensual es:",coste)


if __name__ == '__main__':
    main()
