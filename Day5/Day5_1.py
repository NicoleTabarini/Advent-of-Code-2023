import pandas as pd

with open('input.txt', 'r') as file:
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


# map seed to soil
seed_to_soil = pd.DataFrame(columns=["soil", "seed"])

for el in mapping[names[0]]:

    # this doesn't work, so get the beginning and the end of the range and check if seed is inside
    # then do seed - beginning to find how much i had to add to the beginning of soil to get its matching number

    
    print(el[0], el[1], el[2])
    range_soil = [i for i in range(el[0], el[0]+el[2])]
    range_seed = [i for i in range(el[1], el[1]+el[2])]
    print(range_soil, range_seed)
    # for i in range(len(range_soil)):
    #     seed_to_soil.loc[len(seed_to_soil)] = [range_soil[i], new_list2[i]]
    seed_to_soil["soil"] = seed_to_soil["soil"].concat(range_soil)
    seed_to_soil["seed"] = seed_to_soil["seed"].concat(range_seed)

print(seed_to_soil)



# for seed in seeds:
#     print(seed)
#     if seed in list(seed_to_soil[1]):
#         print("hi")






