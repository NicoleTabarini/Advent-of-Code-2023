
ints = {'one' : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}

with open('Day1/input_1.txt', 'r') as file:
    lines = file.readlines()

final_numbers = []
#numbers = []

for line in lines:
    numbers = []
    for i in range(len(line)):
        if line[i].isdigit():
            numbers.append((int(line[i]),i))

    for i in range(len(line)-3):
        if line[i:i+3] in ints.keys():
            numbers.append((ints[line[i:i+3]],i))

    for i in range(len(line)-4):
        if line[i:i+4] in ints.keys():
            numbers.append((ints[line[i:i+4]],i))

    for i in range(len(line)-5):
        if line[i:i+5] in ints.keys():
            numbers.append((ints[line[i:i+5]],i))

    min_index = numbers[0][1]
    min_num = numbers[0][0]
    max_index = numbers[0][1]
    max_num = numbers[0][0]

    for n in numbers:
        if n[1] < min_index:
            min_num = n[0]
            min_index = n[1]
        if n[1] > max_index:
            max_num = n[0]
            max_index = n[1]

    #print(line, numbers, min_num, min_index, max_num, max_index, "\n")
    final_numbers.append(int(str(min_num) + str(max_num)))
print(sum(final_numbers))

    #print(numbers)