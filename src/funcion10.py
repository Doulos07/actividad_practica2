
actions_points = {
    'kills': 3,
    'assists' : 1,
    'deaths' : -1
}

puntos_jugadores = {
'Shadow': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp' : 0, 'puntos' : 0},
'Blaze': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp' : 0, 'puntos' : 0},
'Viper': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp' : 0, 'puntos' : 0},
'Frost': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp' : 0, 'puntos' : 0},
'Reaper': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp' : 0, 'puntos' : 0}
}



#formato = f"Ranking ronda {ronda} \n jugador    kills   asistencias     Muertes    Puntos "

"""
    recorro diccionaario -> recorro por jugador -> de cada jugador recorro sus acciones
    sumar_actions -> sumo las acciones para el ranking total // Ignoro mvp y puntos
    sumar_puntos -> sumo puntos ganados en esta ronda con las anteriores
    MVPs -> como obtengo el mvp del la ronda?

"""


 
#Menos El MVP 
def sumar_actions (jugador, actions, puntos_jugadores) : 
     global actions_points
     point = 0
     #recorro el diccionario de los jugadores {action : cantidad}
     for action, value in actions.items() :
         #round_point[jugador][action] = value #Muerte True = 1 and False = 0
         puntos_jugadores[jugador][action] += value 
         point += actions_points[action] * value
     puntos_jugadores[jugador]["puntos"] += point
     return point


def imprimir_ronda(jugador, actions) :
     cadena = jugador
     point = 0
     mvp = ""
     max_point = 0
     for value in actions.values() :
         cadena += f"{" "*7}{value}"
     print(cadena)

def imprimir_resultado_final (puntos_jugadores) :
     print(f"ranking Final : \nPlayer    Kills   Assists    Deaths      MVPs    Puntos\n{'-'*55}")
     for key, value in puntos_jugadores.items() :
         puntos = ""
         for punto in value.values() :
             puntos += f"{' '*8}{punto}"
         print(f"{key}{puntos}") #
     print(f"{'-'*55}")
     
#main(rounds, puntos_jugadores)