
with open('Day1/input_1.txt', 'r') as file:
    # Read all the lines in the file and store them in a list
    lines = file.readlines()

numbers = ''
final_numbers = []

for line in lines:
    numbers = [char for char in line if char.isdigit()]
    final_numbers.append(int(numbers[0]+numbers[-1]))
print(sum(final_numbers))