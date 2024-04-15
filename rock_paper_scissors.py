import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class Game:
    def __init__(self, p1, p2, rounds=3):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0
        self.rounds = rounds

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print("It's a tie!")
        elif beats(move1, move2):
            print("Player 1 wins!")
            self.p1_score += 1
        else:
            print("Player 2 wins!")
            self.p2_score += 1
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(self.rounds):
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over!")
        print(f"Final scores - Player 1: {self.p1_score}, Player 2: {self.p2_score}")


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Enter your move (rock, paper, or scissors): ").lower()
            if move in moves:
                return move
            else:
                print("Invalid move. Please enter 'rock', 'paper', or 'scissors'.")


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.last_opponent_move = None

    def learn(self, my_move, their_move):
        self.last_opponent_move = their_move

    def move(self):
        if self.last_opponent_move:
            return self.last_opponent_move
        else:
            return random.choice(moves)


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.last_move_index = -1

    def learn(self, my_move, their_move):
        pass

    def move(self):
        self.last_move_index = (self.last_move_index + 1) % len(moves)
        return moves[self.last_move_index]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def determine_winner(p1_score, p2_score):
    if p1_score > p2_score:
        return "Player 1"
    elif p2_score > p1_score:
        return "Player 2"
    else:
        return "It's a tie!"


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
    print("Winner:", determine_winner(game.p1_score, game.p2_score))
