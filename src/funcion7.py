import string
import random


funcion = lambda x, y:  x + "-" + y + "-" + numeros_aleatorios()


def numeros_aleatorios (longitud=9) :
     caracteres = string.ascii_letters + string.digits
     return ''.join(random.choices(caracteres, k=longitud))





