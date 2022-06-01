import random
options = {
    'S': 'Scissors',
    'R': 'Rock',
    'P': 'Paper'
}

def init(options={}):
    player_choice = input("Pick an option (S, R, P): ")
    
    computer_choice = random.choice(list(options))

    while player_choice.upper() not in list(options):
        print("Error: wrong input.")
        player_choice = input("Pick an option (S, R, P): ")
    

    return [player_choice.upper(), computer_choice]


def isTie(player='', computer=''):
    if player == computer:
        print('Tie: the same moves\n')
        return True

def decide_winner(options=options, player='', opponent=''):
    winningCombo = [['R', 'S'], ['S', 'P'], ['P', 'R']]

    for combo in winningCombo:
        output = "{} beats {}\n{} wins."
        
        if player in combo and opponent in combo:
            if combo.index(player) < combo.index(opponent):
                output = output.format(options[player], options[opponent], 'Player')
            else:
                output = output.format(options[opponent], options[player], 'Computer')

            print(output)
            break


player, computer = init(options)

print(f"Player({options[player]}) : Computer({options[computer]})\n")
if isTie(player, computer):
    player, computer = init(options)

# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rocks
decide_winner(options, player, computer)
