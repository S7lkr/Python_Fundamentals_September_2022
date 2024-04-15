card = input().split()

team_A = ['A-' + str(s) for s in range(1, 12)]    # [A-1, A-2......A-11] -> that's called LIST COMPREHENSION!
team_B = ['B-' + str(s) for s in range(1, 12)]
game_terminated = False

for player in card:
    if player in team_A:
        team_A.remove(player)
    elif player in team_B:
        team_B.remove(player)
    if len(team_A) < 7 or len(team_B) < 7:
        game_terminated = True
        break
print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if game_terminated:
    print('Game was terminated')