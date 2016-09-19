from components import GameCore
import utils


def main():
    game = GameCore()
    msgs = ["Type in the X coord (from 1 to 3)","Type in the Y coord (from 1 to 3)"]
    opts = ["1","2","3"]

    while True:
        while not game.game_over():
            correct_input = False
            while not correct_input:
                print game
                print "Player " + str(game.current_player()) + ", your turn!"
                x_coord = utils.get_input([msgs[0]],opts)
                y_coord = utils.get_input([msgs[1]],opts)
                correct_input = game.fill(
                    utils.to_position(x_coord,y_coord),
                    utils.to_value(game.current_player())
                )
        print game
        if game.has_winner():
            print "Congratulations Player " + str(game.current_player()) + " you are the winner!"
        else:
            print "Nobody wins this time..."
        if ask_to_play_again():
            game.new_game()
        elif ask_to_reset():
            game.reset()
        else:
            break

    #END main

def ask_to_play_again():
    msgs = ["Would you like to play again? (y/n):"]
    opts = ["y","Y","n","N"]
    response = utils.get_input(msgs,opts)
    return response in opts[0:2]

def ask_to_reset():
    msgs = ["Would you like to reset the game? (y/n):"]
    opts = ["y","Y","n","N"]
    response = utils.get_input(msgs,opts)
    return response in opts[0:2]


if __name__ == "__main__":
    main()
