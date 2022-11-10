from random import randrange

game_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player_turn = True
game_is_on = True
turns_count = 0
x_axis = 0
y_axis = 0

print("Your element is X. Good luck;)")

while game_is_on:
    if turns_count == 9 and game_is_on:
        print("Draw")
        game_is_on = False
    else:
        if player_turn:
            x_axis = int(input("Player turn. Set X axis: "))
            y_axis = int(input("Player turn. Set Y axis: "))
            if game_field[x_axis][y_axis] == " ":
                game_field[x_axis][y_axis] = "X"
                turns_count = turns_count + 1
                if game_field[0][0] == "X" and game_field[0][1] == "X" and game_field[0][2] == "X":
                    print("Row strike. Player win")
                    game_is_on = False
                elif game_field[1][0] == "X" and game_field[1][1] == "X" and game_field[1][2] == "X":
                    print("Row strike. Player win")
                    game_is_on = False
                elif game_field[2][0] == "X" and game_field[2][1] == "X" and game_field[2][2] == "X":
                    print("Row strike. Player win")
                    game_is_on = False
                elif game_field[0][0] == "X" and game_field[1][0] == "X" and game_field[2][0] == "X":
                    print("Column strike. Player win")
                    game_is_on = False
                elif game_field[0][1] == "X" and game_field[1][1] == "X" and game_field[2][1] == "X":
                    print("Column strike. Player win")
                    game_is_on = False
                elif game_field[0][2] == "X" and game_field[1][2] == "X" and game_field[2][2] == "X":
                    print("Column strike. Player win")
                    game_is_on = False
                elif game_field[0][0] == "X" and game_field[1][1] == "X" and game_field[2][2] == "X":
                    print("Diagonal strike. Player win")
                    game_is_on = False
                elif game_field[0][2] == "X" and game_field[1][1] == "X" and game_field[2][0] == "X":
                    print("Diagonal strike. Player win")
                    game_is_on = False
                for cell in game_field:
                    print(cell)
                player_turn = False
            else:
                print("Try again")
        else:
            x_axis = randrange(0, len(game_field))
            y_axis = randrange(0, len(game_field))
            if game_field[x_axis][y_axis] == " ":
                game_field[x_axis][y_axis] = "O"
                turns_count = turns_count + 1
                if game_field[0][0] == "O" and game_field[0][1] == "O" and game_field[0][2] == "O":
                    print("Row strike. Computer win")
                    game_is_on = False
                elif game_field[1][0] == "O" and game_field[1][1] == "O" and game_field[1][2] == "O":
                    print("Row strike. Computer win")
                    game_is_on = False
                elif game_field[2][0] == "O" and game_field[2][1] == "O" and game_field[2][2] == "O":
                    print("Row strike. Computer win")
                    game_is_on = False
                elif game_field[0][0] == "O" and game_field[1][0] == "O" and game_field[2][0] == "O":
                    print("Column strike. Computer win")
                    game_is_on = False
                elif game_field[0][1] == "O" and game_field[1][1] == "O" and game_field[2][1] == "O":
                    print("Column strike. Computer win")
                    game_is_on = False
                elif game_field[0][2] == "O" and game_field[1][2] == "O" and game_field[2][2] == "O":
                    print("Column strike. Computer win")
                    game_is_on = False
                elif game_field[0][0] == "O" and game_field[1][1] == "O" and game_field[2][2] == "O":
                    print("Diagonal strike. Computer win")
                    game_is_on = False
                elif game_field[0][2] == "O" and game_field[1][1] == "O" and game_field[2][0] == "O":
                    print("Diagonal strike. Computer win")
                    game_is_on = False
                print("Computer turn:")
                for cell in game_field:
                    print(cell)
                player_turn = True
            game_is_on = True
