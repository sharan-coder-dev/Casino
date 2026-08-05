

player_file = open("Players.txt", "r")
lines = player_file.readlines()
player_file.close()
players = [line.strip() for line in lines]

wallets = {player: 0 for player in players}


try:
    wallet_read = open("Wallets.txt", "r")
    for line in wallet_read:
        if ':' in line and '$' in line:
            parts = line.strip().split(':')
            name = parts[0].strip()
            amount_str = parts[1].strip().replace('$', '')
            if name in wallets:
                wallets[name] = int(amount_str)
    wallet_read.close()
except FileNotFoundError:
    pass

casino_balance = 0

try:
    casino_file = open("Casino_Balance.txt", "r")
    line = casino_file.read()
    pieces = line.split(":")
    pieces[1] = pieces[1].strip().replace("$", "")
    casino_balance = int(pieces[1])
    casino_file.close()

except FileNotFoundError:
    pass

import random
for i in range(len(players)):
    player1 = players[i]
    for j in range(i+1, len(players)):
        player2 = players[j]

        rounds_won_p1 = 0
        rounds_won_p2 = 0
        round_number = 1

        while rounds_won_p1 < 2 and rounds_won_p2 < 2 and round_number <= 3:
            dice_roll1 = random.randint(1, 6)
            dice_roll2 = random.randint(1, 6)
            if dice_roll1 > dice_roll2:
                won_by = dice_roll1 - dice_roll2
                print("Round " + str(round_number) + ": " + player1 + " rolled " + str(
                    dice_roll1) + " and " + player2 + " rolled " + str(
                    dice_roll2) + " so " + player1 + " won by " + str(won_by))
                rounds_won_p1 += 1
                round_number += 1
            elif dice_roll2 > dice_roll1:
                won_by = dice_roll2 - dice_roll1
                print("Round " + str(round_number) + ": " + player2 + " rolled " + str(
                    dice_roll2) + " and " + player1 + " rolled " + str(
                    dice_roll1) + " so " + player2 + " won by " + str(won_by))
                rounds_won_p2 += 1
                round_number += 1
            else:
                print("Round " + str(round_number) + " (tie): It's a tie, they both got " + str(
                    dice_roll1) + " going again...")

        if rounds_won_p1 == 2:
            wallets[player1] += 9
            wallets[player2] -= 10
            casino_balance += 1
            print(f"{player1} wins the game against {player2}!\n")
        elif rounds_won_p2 == 2:
            wallets[player2] += 9
            wallets[player1] -= 10
            casino_balance += 1
            print(f"{player2} wins the game against {player1}!\n")

try:
    counter_file = open("session_count.txt", "r")
    session_number = int(counter_file.read().strip()) + 1
    counter_file.close()
except FileNotFoundError:
    session_number = 1

counter_file = open("session_count.txt", "w")
counter_file.write(str(session_number))
counter_file.close()

wallet_file = open("Wallets.txt","a")
wallet_file.write(f"\n--- Game #{session_number} Results ---\n")
for player, balance in wallets.items():
    wallet_file.write(f"{player}: ${balance}\n")
wallet_file.close()

casino_file = open("Casino_Balance.txt", "w")
casino_file.write(
    "Casino: $" + str(casino_balance)
)

casino_file.close()