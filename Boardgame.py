import Dice


class Board:

    def __init__(self, size):
        self.size = size
        self.board_list = []
        for i in range(self.size):
            self.board_list.append(0)

    def print_board(self):
        print(self.board_list)


class Player:
    current_position = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Game(Player, Board):
    play_game = True

    def win_check(self):
        if player_one.current_position == my_board.size - 1:
            self.play_game = False
            print(f'{player_one.name} Wins')
            return True
        elif player_two.current_position == my_board.size - 1:
            self.play_game = False
            print(f'{player_two.name} Wins')
            return True
        else:
            return False


if __name__ == '__main__':
    my_game = Game
    size_of_board = int(input("Enter the size of the board: "))
    if size_of_board == 0:
        my_game.play_game = False
    while my_game.play_game:
        my_board = Board(size_of_board)
        my_board.print_board()
        player_one = Player(input("Enter your name player one: "))
        print("Welcome to the game: " + player_one.name)
        player_two = Player(input("Enter your name player two: "))
        print("Welcome to the game: " + player_two.name)
        my_dice = Dice
        print("Let the Game Begin")
        player_turn = 1
        while my_board.board_list[size_of_board - 1] != 1 or my_board.board_list[size_of_board - 1] != 2:
            if my_game.win_check(my_game):
                break
            dice_outcome = my_dice.Dice.roll(my_dice)

            if player_turn == 1:
                print(f"Its your turn {player_one.name}")
                print(dice_outcome)
                if player_one.current_position + dice_outcome > my_board.size - 1:
                    continue
                player_one.current_position += dice_outcome
                my_board.board_list[player_one.current_position] = 1
                player_turn = 2
                my_board.print_board()
            else:
                print(f"Its your turn {player_two.name}")
                print(dice_outcome)
                if player_two.current_position + dice_outcome > my_board.size - 1:
                    continue
                player_two.current_position += dice_outcome
                my_board.board_list[player_two.current_position] = 2
                player_turn = 1
                my_board.print_board()
