zen_text = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

zen_text = zen_text.split("\n") #creo listas que son creadas por cad salto de linea "\n"

vocales = "AEIOUaeiou"

for lineas in zen_text : 
    palabras = lineas.split() #Divido la linea en palabras 
    print(lineas) if len(palabras) > 1 and palabras[1][0] in vocales else None
 
#verifico si por lo menos tiene una palabra, 2do renglon sin palabras y se incluye por salto de linea