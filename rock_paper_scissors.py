
rolls = {
    'rock': {
        'defeats': ['scissors'],
        'defeated_by': ['paper']
    },
    'paper': {
        'defeats': ['rock'],
        'defeated_by': ['scissors']
    },
    'scissors': {
        'defeats': ['paper'],
        'defeated_by': ['rock']
    },
}


def main():
    qtd = get_number_of_players()
    i = 0
    victories = {}
    roll_names = list(rolls.keys())
    while i < qtd:
        victories = get_player_data(i, victories, roll_names)
        i += 1

    players = list(victories.keys())
    qtd_players = len(players) - 1
    while not find_winner(victories):
        winner = players[0]
        i = 0
        while i < qtd_players+1:
            player = players[i]
            player_roll = get_roll(player, roll_names)
            victories[player][1] = player_roll
            i += 1
        i = 0
        while i < qtd_players:
            initial_text = f"Round between {winner} and {players[i+1]}"
            winner = check_for_winning_throw(winner, players[i+1],victories)
            if winner:
                victories[winner][0] += 1
            print( initial_text + f" and the winner is: {winner}")
            i += 1
    print(victories)


def find_winner(wins):
    best_of = 3
    for name in wins.keys():
        if wins.get(name)[0] >= best_of:
            return name

    return None


def check_for_winning_throw(player1, player2,wins):
    roll1 = wins[player1][1]
    roll2 = wins[player2][1]
    winner = None
    if roll1 == roll2:
        print("The round tied")
    outcome = rolls.get(roll1, {})
    if roll2 in outcome.get('defeats'):
        winner = player1
    elif roll2 in outcome.get('defeated_by'):
        winner = player2
    return winner


def get_roll(player_name, roll_names):
    print("Available rolls:")
    for index, r in enumerate(roll_names, start=1):
        print(f"{index}. {r}")

    text = input(f"{player_name}, what is your roll? ")
    selected_index = int(text) - 1

    if selected_index < 0 or selected_index >= len(rolls):
        print(f"Sorry {player_name}, {text} is out of bounds!")
        get_roll(player_name, roll_names)

    return roll_names[selected_index]


def get_number_of_players():
    number_players = int(input("Enter the number of players:"))
    if number_players > 0:
        return number_players
    else:
        get_number_of_players()


def get_player_data(i, wins,roll_names):
    player = input(f"Player {i +1}, what´s your name?")
    if player in wins.keys():
        print("There is already a player with that name choose a different name")
        get_player_data(i, wins)
    else:
        wins[player] = [0, '']

    return wins


main()
