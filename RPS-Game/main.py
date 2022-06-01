import random
# Game options
options = {
    'S': 'Scissors',
    'R': 'Rock',
    'P': 'Paper'
}

# Init function
def init(options={}):
    player_choice = input("Pick an option (S, R, P): ")
    
    computer_choice = random.choice(list(options))

    while player_choice.upper() not in list(options):
        print("Error: wrong input.")
        player_choice = input("Pick an option (S, R, P): ")
    

    return [player_choice.upper(), computer_choice]

# Check for tie (same moves between player and opponent)
def isTie(player='', computer=''):
    if player == computer:
        print('Tie: the same moves\n')
        return True

# Decide the winner between player and opponent
def decide_winner(options=options, player='', opponent=''):
    # Possible winning configuration
    winningCombo = [['R', 'S'], ['S', 'P'], ['P', 'R']]

    for combo in winningCombo:
        output = "{} beats {}\n{} wins."
        
        # Select winner by R > S, S > P, or P > R
        if player in combo and opponent in combo:
            if combo.index(player) < combo.index(opponent):
                output = output.format(options[player], options[opponent], 'Player')
            else:
                output = output.format(options[opponent], options[player], 'Computer')

            print(output)
            break

# Initialize both player and opponent
player, computer = init(options)

# Print players moves
print(f"Player({options[player]}) : Computer({options[computer]})\n")
if isTie(player, computer):
    player, computer = init(options)

# Choose winner 
decide_winner(options, player, computer)
