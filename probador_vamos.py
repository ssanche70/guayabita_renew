from vamos import *
from random import randrange


jugador1 = Jugador('Juan', 100)
jugador2 = Jugador('Andres', 200)


def lance(p,s):
    if s != 0:
        print('Primero lance', p)
        print('Segundo lanzamiento', s)

        if s > p:
            print('Retira lo que aposto')
            return (1)
        else:
            if p == s:
                print('Pierde, pone lo que hay en la mesa')
                return (0)
            else:
                print('Perdio, ponga lo apostado')
                return(0)

    else:
        if s == 1 or s == 6:
            print('El jugador pierde con ', p, 'ponga lo que hay en la mesa')
            return (0)
        else:
            return lance(p, randrange(1, 7))

