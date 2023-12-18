with open('Day5/input.txt', 'r') as file:
    data = file.read()

# Split the data into groups based on empty lines
groups = data.split('\n\n')

# Separate each group into a list
separated_lists = [group.split('\n') for group in groups]

mapping = {}
names = []


for i, group_list in enumerate(separated_lists):
    if i != 0:
        names.append(group_list[0])
        mapping[group_list[0]] = [tuple(map(int, line.split())) for line in group_list[1:]]
        group_list.pop(0)
    else:
        group_list[i] = group_list[i].split()
        group_list[i].pop(0)
        seeds = group_list[i]



range_seed = []
range_soil = []
range_fertilizer = []
range_water  = []
range_light  =  []
range_temperature = []
range_humidity  = []
humindity_to_location = set()


for el in mapping[names[0]]:
    range_seed.append((el[1], el[1]+el[2], el[0]))

for el in mapping[names[1]]:
    range_soil.append((el[1], el[1]+el[2], el[0]))

for el in mapping[names[2]]:
    range_fertilizer.append((el[1], el[1]+el[2], el[0]))

for el in mapping[names[3]]:
    range_water.append((el[1], el[1]+el[2], el[0]))

for el in mapping[names[4]]:
    range_light.append((el[1], el[1]+el[2], el[0]))

for el in mapping[names[5]]:
    range_temperature.append((el[1], el[1]+el[2], el[0]))

for el in mapping[names[6]]:
    range_humidity.append((el[1], el[1]+el[2], el[0]))




for seed in seeds:
    seed = int(seed)

    for i in range(len(range_seed)):
        if seed >= range_seed[i][0] and seed <= range_seed[i][1]:
            diff = seed - range_seed[i][0]
            seed_to_soil = range_seed[i][2] + diff
            break
        else:
            seed_to_soil = seed
            
    
    for i in range(len(range_soil)):
        if seed_to_soil >= range_soil[i][0] and seed_to_soil <= range_soil[i][1]:
            diff = seed_to_soil - range_soil[i][0]
            soil_to_fertilizer = range_soil[i][2] + diff
            break
        else:
            soil_to_fertilizer = seed_to_soil
            

    for i in range(len(range_fertilizer)):
        if soil_to_fertilizer >= range_fertilizer[i][0] and soil_to_fertilizer <= range_fertilizer[i][1]:
            diff = soil_to_fertilizer - range_fertilizer[i][0]
            fertilizer_to_water = range_fertilizer[i][2] + diff
            break
        else:
            fertilizer_to_water = soil_to_fertilizer
    

    for i in range(len(range_water)):
        if fertilizer_to_water >= range_water[i][0] and fertilizer_to_water <= range_water[i][1]:
            diff = fertilizer_to_water - range_water[i][0]
            water_to_light = range_water[i][2] + diff
            break
        else:
            water_to_light = fertilizer_to_water


    for i in range(len(range_light)):
        if water_to_light >= range_light[i][0] and water_to_light <= range_light[i][1]:
            diff = water_to_light - range_light[i][0]
            light_to_temperature = range_light[i][2] + diff
            break
        else:
            light_to_temperature = water_to_light


    for i in range(len(range_temperature)):
        if light_to_temperature >= range_temperature[i][0] and light_to_temperature <= range_temperature[i][2]:
            diff = light_to_temperature - range_temperature[i][0]
            temperature_to_humidity = range_temperature[i][1] + diff
            break
        else:
            temperature_to_humidity = light_to_temperature


    for i in range(len(range_humidity)):
        if temperature_to_humidity >= range_humidity[i][0] and temperature_to_humidity <= range_humidity[i][1]:
            diff = temperature_to_humidity - range_humidity[i][0]
            humindity_to_location.add(range_humidity[i][2] + diff)
            print("ADD",seed, range_humidity[i][2] + diff)
        else:
            if i == len(range_humidity):
                print('NO ADd',temperature_to_humidity)
                humindity_to_location.add(temperature_to_humidity)


print(min(humindity_to_location))
print(humindity_to_location)



# for seed in seeds:
#     print(seed)
#     if seed in list(seed_to_soil[1]):
#         print("hi")






