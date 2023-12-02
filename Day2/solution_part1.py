total = 0
cube_limits = {"red" : 12, "green" : 13, "blue" : 14}
with open("games.txt", 'r') as f:
    for game in f:
        game_index_str, sets_str = game.strip().split(':')
        game_index = int(game_index_str.replace('Game', ''))

        game_possible = True
        for game_set in sets_str.split(';'):
            for cubes in game_set.split(','):
                amount_str, color = cubes.strip().split(' ')
                amount = int(amount_str)

                if amount > cube_limits[color]:
                    game_possible = False
                    break
            
            if game_possible == False:
                break

        if game_possible:
            total += game_index
print(total)