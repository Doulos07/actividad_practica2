import string


letras = string.ascii_letters
digitos = string.digits

def longitud_valida (usuario) :
       return len(usuario) >= 5

def contiene_numero (usuario) :
       global digitos
       for char in usuario :
             if char in digitos :
                   return True
       return False
              

def contiene_mayuscula(usuario) :
       for char in usuario :
             if char in string.ascii_uppercase :
                   return True
       return False
     
def solo_letras_numeros (usuario) :
       global letras, digitos
       for char in usuario :
             if char not in letras+digitos :
                   return False
       return True

def validacion(usuario) :
       return (longitud_valida(usuario) and contiene_numero(usuario) and contiene_mayuscula(usuario) and solo_letras_numeros(usuario))