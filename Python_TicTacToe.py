 #Ref: https://pythonprogramming.net/introduction-learn-python-3-tutorials/
import itertools
from colorama import Fore, Back, Style

def game_board(game_map, player=0, row=0, column=0, just_display =  False):
    try:
        if game_map[row][column]!=0:
            print("This position is occupied. Please choose another!!")
            return game_map, False
        if not just_display:
            game_map[row][column] = player
        print("   " + "  ".join([str(x) for x in range(len(game_map))]))


        for count, row in enumerate(game):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row+="   "
                elif item == 1:
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item == 2:
                    colored_row+= Fore.MAGENTA + ' O ' + Style.RESET_ALL

            print(count,colored_row)

        return game_map, True
    except IndexError as e:
        print("Error: Make sure you input row/column as 0,1 0r 2", e)
        return game_map, False
    except Exception as e:
        print("Something went very wrong!!", e)
        return game_map, False

def win(current_game):
    def all_same(L):
        if L.count(L[0]) == len (L) and L[0]!=0:
            return True
        else:
            return False


#vertically
    for col in range(len(current_game)):       
        check = []
        for row in current_game:
            check.append(row[col])
        if all_same(check):
            return True

#Diagonally
    diags = []
    for ix in range(len(game)):
        diags.append(current_game[ix][ix])

    diags_rev = []
    cols = reversed(range(len(game)))
    for r,c in enumerate(cols):
        diags_rev.append(game[r][c])

    if all_same(diags_rev):
        return True

    if all_same(diags):
        return True

#Horizontallly
    for row in game:
        if row.count(row[0]) == len(row) and row[0]!=0:
            return True
# win(game)
# game_board()
play = True
players = [1,2]
while play:
    game_size = int(input("What size game of tic tac toe you want to play?"))
    game = [[0 for i in range(game_size)]for i in range(game_size)]
 
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False
        while not played:
            column_choice = int(input("What column do you want to play? (0,1,2): "))
            row_choice = int(input("What row do you want to play? (0,1,2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)
   
        if win(game):
            print(f"Player {current_player} wins the game!!!")
            game_won = True
            again = input("The game is over, would you like to play again?(y/n) ")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("Byeee")
                play = False
            else:
                print("Not a valid answer, so see you laterrr.. aligatorrr!!")
                play = False



