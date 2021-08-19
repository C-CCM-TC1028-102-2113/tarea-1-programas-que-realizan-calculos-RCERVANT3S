#DigitosPares
def main():
    #escribe tu código abajo de esta línea
    pass


lista = []
def digitospares(número):
    for i in número:
        a = i
        mod_calc = float(a) % 2

        if mod_calc % 2 == 0:
            lista.append(int(a))
       
   

número = input("Dame un número:")
digitospares(número)

par = len(lista)
if par == 0:
    print("no hay ningún número par")
else:    
    print("El número de digitos pares es:",par)

if __name__ == '__main__':
    main()
