import random

def game(pokusy, hraci, cislo, game_range):

    game = True
    while pokusy and game:
        for i in range(len(hraci)):
            if hraci[i]['is_person']:
                pokus = int(input(f'{hraci[i]["nickanem"]}: '))
                hraci[i]['wrong_answers'].append(str(pokus))
                if pokus == cislo:
                    print()
                    print()
                    print(f"{hraci[i]['nickanem']} vyhral, odpoved bola {cislo}")
                    print()
                    game = False
                    break

                elif pokus < cislo:

                    print('cislo je vacsie')

                elif pokus > cislo:

                    print('cislo je mensie')

            else:
                pokus = random.randint(game_range[0], game_range[1])
                print()
                print(f'hrac {hraci[i]["nickanem"]} (pocitac) hada: {pokus}')
                hraci[i]['wrong_answers'].append(str(pokus))
                if pokus == cislo:
                    print()
                    print()
                    print(f"{hraci[i]['nickanem']} vyhral, odpoved bola {cislo}")
                    print()
                    game = False
                    break
                elif pokus < cislo:

                    print('cislo je vacsie')

                elif pokus > cislo:

                    print('cislo je mensie')

        pokusy -= 1
    return hraci, pokusy


def start_game(pocet_ludi):

    hraci = []

    if pocet_ludi < 6 and pocet_ludi > 0:
        for j in range(pocet_ludi):
            clovek = True if int(
                input(f'{j + 1}. pocitac alebo clovek? (0/1) ')) else False
            # hraci.append(clovek)
            nickanem = input("nickanem: ")
            hraci.append(
                {
                    "nickanem": nickanem,
                    "is_person": clovek,
                    "wrong_answers": []
                }
            )
        return hraci
    


if __name__ == '__main__':

    pocet_ludi = int(input('pocet ludi (1-5): '))

    while not(pocet_ludi < 6 and pocet_ludi > 0):
        pocet_ludi = int(input('pocet ludi (1-5): '))

    hraci = start_game(pocet_ludi)

    game_range = tuple(map(int, input('min max : ').split()))

    tries_num = (game_range[1] - game_range[0]) // 2

    cislo = random.randint(game_range[0], game_range[1])

    print()
    print("zacala hra")
    print()

    hraci, pokusy = game(tries_num, hraci, cislo, game_range)

    print()

    if not pokusy:
        print('nikto nevyhral')
        print()

    for i in hraci:
        print(f"{i['nickanem']} pokusy: {','.join(i['wrong_answers'])}")
