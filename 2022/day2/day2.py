shape_score = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
outcome_score = {'win': 6, 'draw': 3, 'loss': 0}
WIN = 6
DRAW = 3
LOSS = 0

score = 0
with open('input.txt') as f:
    i = 1
    for line in f.readlines():
        round_score = 0
        player1 = line[0]
        player2 = line[2]

        if player1 == 'A':
            if player2 == 'X':
                print('draw')
                outcome = 'draw'
            elif player2 == 'Y':
                print('player2 wins')
                outcome = 'loss'
            else:
                print('you win!')
                outcome = 'win'
        if player1 == 'B':
            if player2 == 'Y':
                print('draw')
                outcome = 'draw'
            elif player2 == 'Z':
                print('player2 wins')
                outcome = 'loss'
            else:
                print('you win!')
                outcome = 'win'
        if player1 == 'C':
            if player2 == 'Z':
                print('draw')
                outcome = 'draw'
            elif player2 == 'X':
                print('player2 wins')
                outcome = 'loss'
            else:
                print('you win!')
                outcome = 'win'
        round_score = shape_score[player1] + outcome_score[outcome]
        score += round_score

        print('round {} => score: {} total score:
                {}'.format(i,round_score,score))

