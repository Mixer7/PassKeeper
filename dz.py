import random
import subprocess
from time import sleep


def input_team():
    b = list(set(input().split()))
    if len(b) < 2:
        print('No teams to play with! Quitting..')
        sleep(3)
        clear()
        exit(1)
    return b


def set_scoreTable(teamtuple, num):
    scoreTable1 = [] * num
    for i in range(num):
        scoreTable1.append([0] * (num + 6))
    for i in range(num):
        scoreTable1[i][i] = teamtuple[i]
    return scoreTable1


def output_scoreboard(table, teams):
    scores = dict()
    for i in range(len(teams)):
        scores[teams[i]] = table[i][len(teams) + 5]
    for i in range(len(teams)):
        printing_elem = teams.index(max(scores, key=scores.get))
        print('{0:12} - {1:3} points {2:3} wins {3:3} loses {4:3} ties {5:3} goals {6:3} missed'.format(
            table[printing_elem][printing_elem],
            str(scores.get(teams[printing_elem])),
            table[printing_elem][len(teams)],
            table[printing_elem][len(teams) + 1],
            table[printing_elem][len(teams) + 2],
            table[printing_elem][len(teams) + 3],
            table[printing_elem][len(teams) + 4]))
        scores[teams[printing_elem]] = -1


def output_results(someString, teams, scoretable):
    if len(someString) != 3:
        print('\n\nWrong. See input rules above!')
        return
    elif someString[1] != '-' or someString[0] not in teams or someString[2] not in teams or someString[0] == \
            someString[2]:
        print('\n\nWrong. See input rules above!')
        return
    teamaIndex = teams.index(someString[0])
    teambIndex = teams.index(someString[2])
    print('\n' + someString[0] + ' - ' + someString[2] + '\n' + str(scoreTable[teamaIndex][teambIndex]))


def clear():
    try:
        subprocess.call(['cls'])
    except OSError:
        subprocess.call(['clear'])


def get_choice(choice):
    while (choice == []):
        try:
            choice = input().split()
            if choice == []:
                1 / 0
        except ZeroDivisionError:
            print('You didnt type anything. To exit type \"none\"')
    return choice


def dialog(choice):
    choice = get_choice(choice)
    while choice != [] and choice[0] != 'none' and choice[0] != 'no':
        clear()
        output_scoreboard(scoreTable, teams)
        output_results(choice, teams, scoreTable)
        print('\n')
        print('Any match else? Type "no" to exit')
        choice = []
        choice = get_choice(choice)


if __name__ == "__main__":
    clear()
    print('Input teams:')
    teams = input_team()
    number_of_teams = len(teams)
    scoreTable = set_scoreTable(teams, number_of_teams)
    for i in range(number_of_teams):
        for j in range(number_of_teams):
            if scoreTable[i][j] == 0 and scoreTable[j][i] == 0:
                scA = random.randint(0, 5)
                scB = random.randint(0, 5)
                scoreTable[i][number_of_teams + 3] += scA
                scoreTable[i][number_of_teams + 4] += scB
                scoreTable[j][number_of_teams + 3] += scB
                scoreTable[j][number_of_teams + 4] += scA
                if scA < scB:
                    scoreTable[j][number_of_teams + 5] += 3
                    scoreTable[j][number_of_teams] += 1
                    scoreTable[i][number_of_teams + 1] += 1
                elif scA == scB:
                    scoreTable[i][number_of_teams + 2] += 1
                    scoreTable[j][number_of_teams + 2] += 1
                    scoreTable[i][number_of_teams + 5] += 1
                    scoreTable[j][number_of_teams + 5] += 1
                elif scA > scB:
                    scoreTable[i][number_of_teams + 5] += 3
                    scoreTable[i][number_of_teams] += 1
                    scoreTable[j][number_of_teams + 1] += 1
                scoreTable[i][j] = str(scA) + '-' + str(scB)
                scoreTable[j][i] = str(scB) + '-' + str(scA)
    clear()
    output_scoreboard(scoreTable, teams)
    print('\n\nWhich match do you wanna see?')
    print('Just input it like \"TeamA\" - \"TeamB\"')
    print('Input \"none\" if you dont want to see anything')

    choice = []
    dialog(choice)

    clear()
