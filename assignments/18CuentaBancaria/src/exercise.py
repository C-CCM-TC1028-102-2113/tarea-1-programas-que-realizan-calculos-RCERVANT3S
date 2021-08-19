#Cuenta Bancaria
def main():
    #escribe tu código abajo de esta línea
    pass

saldo = float(input("Dame el saldo del mes anterior:"))
ingresos = float(input("Dame los ingresos:"))
egresos = float(input("Dame los egresos:"))
cheques = int(input("Dame el número de cheques:"))

saldofinal = ((saldo + ingresos)) - (egresos + (cheques * 13)) 

saldofinal = saldofinal * .925
saldofinal = f'{saldofinal:.5f}'

print ("El saldo final de la cuenta es:",saldofinal)

if __name__ == '__main__':
    main()
