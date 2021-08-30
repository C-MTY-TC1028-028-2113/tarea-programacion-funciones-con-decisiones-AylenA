def calcula_grado(grado):
    if grado < 0.0 or grado > 1.0:
        cali = "score incorrecto"
    elif grado > 0.9:
        cali = "A"
    elif grado > 0.8:
        cali = "B"
    elif grado > 0.7:
        cali = "C"
    elif grado > 0.6:
        cali = "D"
    else:
        cali = "F"
    return cali


def main():
    #escribe tu código abajo de esta línea
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    print(calcula_grado(x))

if __name__=='__main__':
    main()
