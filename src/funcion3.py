rules = """Respeta a los demás. No se permiten insultos ni lenguaje
ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""

incorrecto = """clave incorrecta"""

def ingresa_clave():
     clave = input("Ingrese la palabra clave: ").lower() #clave = calve.lower()
     reglas = rules.split('.')
     for regla in reglas :
         if clave in regla :
              print(regla)
              break

