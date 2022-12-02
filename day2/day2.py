class OpponentAction:
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'

class PlayerAction:
    ROCK = 'X'
    PAPER = 'Y'
    SCISSORS = 'Z'

class PlayerIntent:
    LOSE = 'X'
    DRAW = 'Y'
    WIN = 'Z'

ROCK = 1
PAPER = 2
SCISSORS = 3

def play(strategy: list, intent_mode: bool = False) -> int:
    score = 0
    for round in strategy:
        opponent_action = {
            OpponentAction.ROCK: ROCK,
            OpponentAction.PAPER: PAPER,
            OpponentAction.SCISSORS: SCISSORS
        }[round[0]]

        if not intent_mode:
            player_action = {
                PlayerAction.ROCK: ROCK,
                PlayerAction.PAPER: PAPER,
                PlayerAction.SCISSORS: SCISSORS
            }[round[1]]

            if (opponent_action == player_action):
                score += 3
            elif not ((((1 << 2) | opponent_action) - player_action) % 3):
                score += 6

            score += player_action
        else:
            player_intent = round[1]
            match player_intent:
                case PlayerIntent.LOSE:
                    player_action = ((opponent_action - 2) %3) +1
                    score += player_action
                case PlayerIntent.DRAW:
                    player_action = opponent_action
                    score += player_action + 3
                case PlayerIntent.WIN:
                    player_action = ((opponent_action) %3) +1
                    score += player_action + 6
    return score

with open('day2/data.txt') as f:
    strategy = [line.split() for line in f.read().strip().split('\n')]

part1 = play(strategy, False)
part2 = play(strategy, True)

print(f"Part1: {part1} Part2: {part2}")
