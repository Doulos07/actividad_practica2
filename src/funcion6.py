menciones = {'música' : 0, 'charla' : 0, 'entretenimiento' : 0}

def cant_menciones (descriptions) :
      for lineas in descriptions :
           lineas = lineas.lower()
           palabras = lineas.split()
           for mencion in menciones.keys() :
                if mencion in palabras :
                     menciones[mencion] += 1
      print(menciones)
      return menciones


     