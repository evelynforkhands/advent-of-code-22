from helper import read_input


def get_score_part2(game):
    score = 0
    player1 = game[0]
    player2 = game[1]
    if player2 == "X":
        score += 0
        player2 = "A" if player1 == "B" else "B" if player1 == "C" else "C"
    elif player2 == "Y":
        score += 3
        player2 = player1
    elif player2 == "Z":
        score += 6
        player2 = "A" if player1 == "C" else "B" if player1 == "A" else "C"
    addition_for_second_player = 1 if player2 == "A" else 2 if player2 == "B" else 3
    return score + addition_for_second_player



def get_score(game):
    # get the first player's score
    score = 0
    addition_for_second_player = 1 if game[1] == "X" else 2 if game[1] == "Y" else 3
    if game[0] == "A" and game[1] == "X" or game[0] == "B" and game[1] == "Y" or game[0] == "C" and game[1] == "Z":
        score += 3
    elif game[0] == 'C' and game[1] == 'X':
        score += 6
    elif game[0] == 'A' and game[1] == 'Y':
        score += 6
    elif game[0] == 'B' and game[1] == 'Z':
        score += 6
    print(
        f"score: {score}, addition_for_second_player: {addition_for_second_player}, {'Scissors' if game[0] == 'C' else 'Rock' if game[0] == 'B' else 'Paper'} vs {'Scissors' if game[1] == 'C' else 'Rock' if game[1] == 'X' else 'Paper'}")
    return score + addition_for_second_player


input = sum([get_score_part2(game.split(' ')) for game in read_input()])

print(input)
