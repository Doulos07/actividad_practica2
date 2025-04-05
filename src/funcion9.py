"""
-Eliminar espacios extra en los nombres.
-Convertir todos los nombres a formato de título (primera letra en mayúscula y el resto en minúscula).
-Eliminar registros duplicados para evitar clientes repetidos.
-Eliminar valores vacíos o nulos, ya que no aportan información válida.
-Mostrar la lista limpia de clientes listos para usar en el sistema de facturación.
"""





"""
def eliminar_espacios (clients) :
      new_list = [cli.strip() if cli is not None else None for cli in clients  ]
      return new_list
      # if cli is not None -> Si no es None saco los espacios en blanco sino agrego None

def eliminar_None_vacio (clients) :
      new_list = [cli for cli in clients if cli] #Si cli no es Falso (None o cadena Vacia) lo agrego a la lista
      return new_list
"""

def eliminar_espacios_y_elementos_vacios (clients) :
      new_list = [cli.strip() for cli in clients if cli and cli.strip()]
      return new_list
      # if cli -> filtra los None porque PY los considera False pero no las caracteres con espacio "  "
      #if cli.strip() -> si tengo una cadena // True == "   " -> uso strip() == "" == False en python


def formato_title (clients) :
      new_list = [cli.title() for cli in clients if cli] #Verifico que no sea None
      return new_list


def eliminar_duplicados (clients) :
      new_list = []
      for cli in clients :
           if cli not in new_list :
                 new_list.append(cli)
      return new_list


def imprimir (clients) :
      print(clients)

def limpiar_datos (clients) :      
       clients = (eliminar_espacios_y_elementos_vacios(clients))
       clients = (formato_title (clients))
       clients = (eliminar_duplicados (clients))
       imprimir(clients)
