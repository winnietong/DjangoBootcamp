from board import Board
from player import Player
__author__ = 'winnie'


def check_and_update_move(game, player):
    valid_move = False
    while (valid_move == False):
        place_marker = raw_input(("{}, Where would you like to place {} (x y)? ").format(player.name, player.marker))
        location = place_marker.split(" ")
        valid_move = game.check_move(player.marker, int(location[0]), int(location[1]))
    return None


def play_again():
    action = raw_input("Do you want to play again (y/n)? ").lower()
    if action == 'y':
        game()


def game():
    game = Board()
    game.print_help_board()
    place_marker = ''
    game_win = False

    while place_marker != 'q' or game_win != True:
        check_and_update_move(game, player1)
        game_win = game.check_wins(player1.marker)
        if game_win == True:
            player1.wins += 1
            print "Player 1 has won {} time(s)".format(player1.wins)
            return
        else:
            check_and_update_move(game, player2)
            game_win = game.check_wins(player2.marker)
            if game_win == True:
                player2.wins += 1
                print "Player 2 has won {} time(s)".format(player2.wins)
                return
    return None


player1 = Player("Player 1", "X")
player2 = Player("Player 2", "O")
game()
play_again()