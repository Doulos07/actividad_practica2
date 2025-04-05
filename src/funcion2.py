import palabra_larga

def palabra_larga (palabras) :
     mas_larga = ''
     for palabra in palabras :
         if len(palabra) > len(mas_larga) :
             mas_larga = palabra
     return mas_larga
