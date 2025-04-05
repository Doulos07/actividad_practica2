def rapido (tiempo) :
      return tiempo < 200

def normal (tiempo) :
      return 200 <= tiempo <= 500

def lento (tiempo) :
      return tiempo > 500

def categoria (tiempo) :
      if rapido(tiempo) :
           print("Categoria : Rapido")
      elif normal(tiempo) :
           print("Categoria : normal")
      else :     #elif lento(tiempo) :
           print("Categoria : lento")


