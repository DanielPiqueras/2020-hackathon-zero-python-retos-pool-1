from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):

    if player.lower() == options[0].lower() and ai.lower() == options[2].lower():
        return 'Ganaste!'
    elif player.lower() == options[1].lower() and ai.lower() == options[0].lower():
        return 'Ganaste!'
    elif player.lower() == options[2].lower() and ai.lower() == options[1].lower():
        return 'Ganaste!'
    elif player.lower() == options[0].lower() and ai.lower() == options[0].lower():
        return 'Empate!'
    elif player.lower() == options[1].lower() and ai.lower() == options[1].lower():
        return 'Empate!'
    elif player.lower() == options[2].lower() and ai.lower() == options[2].lower():
        return 'Empate!'
    
    return "Perdiste!"

# Entry Pointcd ..
def Game():

    winner = quienGana(player, ai)

    print(winner)
