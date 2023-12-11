
matrix = []

okay = []

with open('Day3/input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    l = line.strip()
    matrix.append([char for char in l])

for i in range(len(matrix)): #rows
    j = 0
    row = i
    
    while j < len(matrix[0]): #element
        if matrix[i][j].isdigit():
            k = j
            while matrix[row][k].isdigit():
                k += 1
                if k == len(matrix[0]):
                    break


            if i == 0:
                if j == 0:
                    if matrix[i][k] != "." or any(element != '.' for element in matrix[i+1][j-1:k+1]):
                        okay.append(''.join(matrix[i][j:k]))
                if k == len(matrix[0]):
                    if matrix[i][j-1] != "." or any(element != '.' for element in matrix[i+1][j-1:k+1]):
                        okay.append(''.join(matrix[i][j:k]))
                else:
                    if matrix[i][j-1] != "." or matrix[i][k] != "." or any(element != '.' for element in matrix[i+1][j-1:k+1]):
                        okay.append(''.join(matrix[i][j:k]))



            elif i == len(matrix)-1:
                if j == 0:
                    if matrix[i][k] != "." or any(element != '.' for element in matrix[i-1][j-1:k+1]):
                        okay.append(''.join(matrix[i][j:k]))
                if k == len(matrix[0]):
                    if matrix[i][j-1] != "." or any(element != '.' for element in matrix[i-1][j-1:k+1]):
                        okay.append(''.join(matrix[i][j:k]))
                else:
                    if matrix[i][j-1] != "." or matrix[i][k] != "." or any(element != '.' for element in matrix[i-1][j-1:k+1]):
                        okay.append(''.join(matrix[i][j:k]))



            elif k == len(matrix[0]):
                if matrix[i][j-1] != "." or any(element != '.' for element in matrix[i-1][j-1:k+1]) or any(element != '.' for element in matrix[i+1][j-1:k+1]):
                    okay.append(''.join(matrix[i][j:k]))
            


            elif j == 0:
                if matrix[i][k] != "." or any(element != '.' for element in matrix[i-1][j:k+1]) or any(element != '.' for element in matrix[i+1][j:k+1]):
                    okay.append(''.join(matrix[i][j:k]))




            else:
                if matrix[i][j-1] != "." or matrix[i][k] != "." or any(element != '.' for element in matrix[i-1][j-1:k+1]) or any(element != '.' for element in matrix[i+1][j-1:k+1]):
                    okay.append(''.join(matrix[i][j:k]))


            j = k
        else: 
            j += 1

okay = [int(x) for x in okay]
print(sum(okay))