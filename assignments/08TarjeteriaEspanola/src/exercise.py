def tarjetas(pliegos,plumones):
    
    tarPliegos = pliegos*12
    tarPlumones = plumones*35

    if tarPliegos<=tarPlumones:
        return tarPliegos
    else:
        return tarPlumones

def main():
    #escribe tu código abajo de esta línea
    pli = int(input("Dame la cantidad de pliegos de papel albanene: "))
    plu = int(input("Dame la cantidad de plumones: "))

    r = tarjetas(pli,plu)

    print("El número máximo de tarjetas que se pueden hacer es:",r)

if __name__=='__main__':
    main()
