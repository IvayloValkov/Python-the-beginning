days = int(input())

all_money = 0
all_wins = 0
all_loses = 0

for day in range(1, days + 1):
    sport = input()
    total_money = 0
    wins = 0
    loses = 0

    while sport != 'Finish':
        game = sport
        result = input()
        if result == 'win':
            total_money += 20
            wins += 1
        elif result == 'lose':
            total_money += 0
            loses += 1

        sport = input()

    if wins > loses:
        total_money = total_money + (total_money * 0.10)

    all_money += total_money
    all_wins += wins
    all_loses += loses

if all_wins > all_loses:
    all_money += (all_money * 0.20)
    print(f'You won the tournament! Total raised money: {all_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {all_money:.2f}')