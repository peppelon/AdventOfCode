# Data content
seeds = []
seed_to_soil_data = {'dst':[], 'src':[], 'range':[]}
soil_to_fertilizer_data = {'dst':[], 'src':[], 'range':[]}
fertilizer_to_water_data = {'dst':[], 'src':[], 'range':[]}
water_to_light_data = {'dst':[], 'src':[], 'range':[]}
light_to_temperature_data = {'dst':[], 'src':[], 'range':[]}
temperature_to_humidity_data = {'dst':[], 'src':[], 'range':[]}
humidity_to_location_data = {'dst':[], 'src':[], 'range':[]}

# Extract info from data file
with open("data.txt", 'r') as data:

    # Get seed
    seed_line = data.readline()
    _, seeds = seed_line.strip().split(':')
    seeds = seeds.split(' ')
    seeds = [int(s) for s in seeds if s.isdigit()]

    data.readline() # remove empty line
    data.readline() # remove header

    # seed-to-soil map
    while True:
        line = data.readline()
        numbers = line.strip().split(' ')
        if len(numbers) != 3: # empty line
            break
        seed_to_soil_data['dst'].append(int(numbers[0]))
        seed_to_soil_data['src'].append(int(numbers[1]))
        seed_to_soil_data['range'].append(int(numbers[2]))

    data.readline() # remove header

    # soil-to-fertilizer map
    while True:
        line = data.readline()
        numbers = line.strip().split(' ')
        if len(numbers) != 3: # empty line
            break
        soil_to_fertilizer_data['dst'].append(int(numbers[0]))
        soil_to_fertilizer_data['src'].append(int(numbers[1]))
        soil_to_fertilizer_data['range'].append(int(numbers[2]))

    data.readline() # remove header

    # fertilizer-to-water map
    while True:
        line = data.readline()
        numbers = line.strip().split(' ')
        if len(numbers) != 3: # empty line
            break
        fertilizer_to_water_data['dst'].append(int(numbers[0]))
        fertilizer_to_water_data['src'].append(int(numbers[1]))
        fertilizer_to_water_data['range'].append(int(numbers[2]))

    data.readline() # remove header

    # water-to-light map
    while True:
        line = data.readline()
        numbers = line.strip().split(' ')
        if len(numbers) != 3: # empty line
            break
        water_to_light_data['dst'].append(int(numbers[0]))
        water_to_light_data['src'].append(int(numbers[1]))
        water_to_light_data['range'].append(int(numbers[2]))

    data.readline() # remove header

    # light-to-temperature map
    while True:
        line = data.readline()
        numbers = line.strip().split(' ')
        if len(numbers) != 3: # empty line
            break
        light_to_temperature_data['dst'].append(int(numbers[0]))
        light_to_temperature_data['src'].append(int(numbers[1]))
        light_to_temperature_data['range'].append(int(numbers[2]))

    data.readline() # remove header

    # temperature-to-humidity map
    while True:
        line = data.readline()
        numbers = line.strip().split(' ')
        if len(numbers) != 3: # empty line
            break
        temperature_to_humidity_data['dst'].append(int(numbers[0]))
        temperature_to_humidity_data['src'].append(int(numbers[1]))
        temperature_to_humidity_data['range'].append(int(numbers[2]))

    data.readline() # remove header

    # humidity-to-location map
    while True:
        line = data.readline()
        numbers = line.strip().split(' ')
        if len(numbers) != 3: # empty line
            break
        humidity_to_location_data['dst'].append(int(numbers[0]))
        humidity_to_location_data['src'].append(int(numbers[1]))
        humidity_to_location_data['range'].append(int(numbers[2]))

locations = []

def get_mapped_value(map_data, input_val):
    dst = map_data['dst']
    source = map_data['src']
    range_length = map_data['range']

    mapped_val = -1
    number_of_maps = len(dst)

    for i in range(number_of_maps):
        source_val = source[i]
        if input_val >= source_val and input_val < (source_val + range_length[i]):
            diff = input_val - source_val
            mapped_val = dst[i] + diff
            break

    if mapped_val == -1:
        mapped_val = input_val

    return mapped_val

# Now to look for the locations
for seed in seeds:
    soil = get_mapped_value(seed_to_soil_data, seed)
    fertilizer = get_mapped_value(soil_to_fertilizer_data, soil)
    water = get_mapped_value(fertilizer_to_water_data, fertilizer)
    light = get_mapped_value(water_to_light_data, water)
    temperature = get_mapped_value(light_to_temperature_data, light)
    humidity = get_mapped_value(temperature_to_humidity_data, temperature)
    location = get_mapped_value(humidity_to_location_data, humidity)

    locations.append(location)

print(min(locations))

