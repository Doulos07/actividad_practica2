def segunda_palabra_vocal (zen_text) :
     text = ""
     zen_text = zen_text.split("\n") #creo listas que son creadas por cad salto de linea "\n"

     vocales = "AEIOUaeiou"

     for lineas in zen_text : 
         palabras = lineas.split() #Divido la linea en palabras 
         if (len(palabras) > 1 and palabras[1][0] and vocales) :
             text += lineas
     return text
         #verifico si por lo menos tiene una palabra, 2do renglon sin palabras y se incluye por salto de linea