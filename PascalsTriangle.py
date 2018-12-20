# --------------------------------+
# Tatum Gray                      |
# PascalsTriangle.py              |
# Last Updated: May 1, 2016       |
# --------------------------------|
# This program creates what is    |
# known as a Pascal's Triangle    |
#---------------------------------+

def combination(n, k):
    if k == 0 or k == n:
        return 1
    return combination(n-1,k-1) + combination(n-1,k)
def pascals_triangle(rows):
    for row in range(rows):
        answer = ""
        for column in range(row + 1):
            answer = answer + str(combination(row, column)) + "\t"
        print(answer)

pascals_triangle(20)
