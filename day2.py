shape_score = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
outcome_score = {'win': 6, 'draw': 3, 'loss': 0}
shape = { 'A': 'rock', 'X': 'rock', 'B': 'paper', 'Y': 'paper', 'C': 'scissor', 'Z': 'scissor'}

score = 0
with open('input.txt') as f:
    i = 1
    for line in f.readlines():
        round_score = 0
        opponent = line[0]
        you = line[2]

        if opponent == 'A':
            if you == 'X':
                outcome = 'loss'
                you = 'C'
            elif you == 'Y':
                outcome = 'draw'
                you = 'A'
            elif you == 'Z':
                outcome = 'win'
                you = 'B'
        if opponent == 'B':
            if you == 'X':
                outcome = 'loss'
                you = 'A'
            elif you == 'Y':
                outcome = 'draw'
                you = 'B'
            elif you == 'Z':
                outcome = 'win'
                you = 'C'
        if opponent == 'C':
            if you == 'X':
                outcome = 'loss'
                you = 'B'
            elif you == 'Y':
                outcome = 'draw'
                you = 'C'
            elif you == 'Z':
                outcome = 'win'
                you = 'A'
        round_score = shape_score[you] + outcome_score[outcome]
        score += round_score

        # print("round {}: ".format(i))
        # print("elf played {}, you played {}".format(shape[opponent], shape[you]))
        # print("shape points: {} outcomepoints: {}".format(shape_score[you], outcome_score[outcome]))
        # print("score: {} total score: {}\n".format(round_score,score))

        # i += 1
print("total score {}".format(score))
