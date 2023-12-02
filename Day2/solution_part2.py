total = 0
with open("games.txt", 'r') as f:
    for game in f:
        cube_minimums = {"red" : 0, "green" : 0, "blue" : 0}

        game_index_str, sets_str = game.strip().split(':')
        game_index = int(game_index_str.replace('Game', ''))

        for game_set in sets_str.split(';'):
            for cubes in game_set.split(','):
                amount_str, color = cubes.strip().split(' ')
                amount = int(amount_str)

                if amount > cube_minimums[color]:
                    cube_minimums[color] = amount
        
        power = 1
        for value in cube_minimums.values():
            power *= value

        total += power
print(total)