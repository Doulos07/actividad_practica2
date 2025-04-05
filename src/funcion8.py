def son_anagrama (arg1, arg2) :
     arg1 = arg1.lower()
     arg2 = arg2.lower()
     if len(arg1) == len(arg2) : 
         arg2 = arg2[::-1] #me devuelve la cadena arg2 invertida
         if arg1 == arg2 :
              return "Son anagrama"
     return "No son anagramas."



