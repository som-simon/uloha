import random

def win(players):
    if players[0]["choice"] == players[1]["choice"]:
        pass

    elif players[0]["choice"] == 'r':

        if players[1]["choice"] == 'p':
            players[1]["score"] += 1
        elif players[1]["choice"] == 's':
            players[0]["score"] += 1

    elif players[0]["choice"] == 'p':

        if players[1]["choice"] == 'r':
            players[0]["score"] += 1
        elif players[1]["choice"] == 's':
            players[1]["score"] += 1

    elif players[0]["choice"] == 's':

        if players[1]["choice"] == 'p':
            players[0]["score"] += 1
        elif players[1]["choice"] == 'r':
            players[1]["score"] += 1
    return players


def game(winning_rounds, is_comp):
    players = [{
        "player": 1,
        "is_comp": False,
        "score": 0,
        "choice": ''
    }, {
        "player": 2,
        "is_comp": is_comp,
        "score": 0,
        "choice": ''
    }]
    log = []
    choices = ['r', 'p', 's']
    loop = True

    while loop:
        round = len(log) + 1
        temp = []

        print()
        print(f"round {round}")

        for i in range(len(players)):

            if players[i]["is_comp"]:
                players[i]["choice"] = random.choice(choices)
                print(f'computers choice: {players[i]["choice"]}')
                temp.append(players[i]["choice"])
            else:
                players[i]["choice"] = input(
                    "rock, paper or scissors? (r/p/s) ")
                temp.append(players[i]["choice"])

        log.append(temp)

        players = win(players)

        print(f'score: {players[0]["score"]} : {players[1]["score"]}')

        for player in players:
            if player["score"] == winning_rounds:
                print(f'player {player["player"]} wins')
                loop = False
                break

    print()
    for i in range(len(log)):
        print(f"{i+1}. round: {', '.join(log[i])}")


if __name__ == "__main__":
    winning_rounds = int(input("num of winning_rounds: "))
    is_comp = True if input("computer or person? ") in (
        "computer", 'c') else False
    game(winning_rounds, is_comp)
