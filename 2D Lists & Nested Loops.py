#2 dimensional lists
#compounding lists within lists
#needs commas after each row.
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
#This finds a number in the above list
#at 0,0


#Finds the number 8 and prints it. 
print(number_grid[2][1])

#nested for loop which prints all numbers in a column.

for row in number_grid:
    for col in row:
        print(col)
