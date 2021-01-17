input_text = input()

win_counter = 0
loss_counter = 0
game_counter = 0
total_game_counter = 0

while input_text != "End of tournaments":
    number_of_games = int(input())

    for x in range(0, number_of_games):
        game_counter += 1
        total_game_counter += 1

        desi_team = int(input())
        other_team = int(input())

        if desi_team > other_team:
            win_counter += 1
            print(f"Game {game_counter} of tournament {input_text}: win with {desi_team - other_team} points.")

        if desi_team < other_team:
            loss_counter += 1
            print(f"Game {game_counter} of tournament {input_text}: lost with {other_team - desi_team} points.")

    game_counter = 0
    input_text = input()

win_percentage = win_counter * 1.00 / total_game_counter * 100
loss_percentage = loss_counter * 1.00 / total_game_counter * 100

print(f"{win_percentage:.2f}% matches win")
print(f"{loss_percentage:.2f}% matches lost")