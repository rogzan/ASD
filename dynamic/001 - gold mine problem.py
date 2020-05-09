#Given a gold mine of n*m dimensions. Each field in this mine contains a positive integer
#which is the amount of gold in tons. Initially the miner is at first column but can be at any row.
#He can move only (right->,right up /,right down\) that is from a given cell, the miner can move to the cell
#diagonally up towards the right or right or diagonally down towards the right. Find out maximum amount of gold he can collect. 

def getMaxGold(gold, m, n):
    goldTable = [[0 for i in range(n)]
                 for j in range(m)]
    for col in range(n - 1, -1, -1):
        for row in range(m):
            if (col == n - 1):      # Gold collected on going to
                right = 0           # the cell on the rigth(->)
            else:
                right = goldTable[row][col + 1]

            if (row == 0 or col == n - 1):    # Gold collected on going to
                right_up = 0                  # the cell to right up (/)
            else:
                right_up = goldTable[row - 1][col + 1]
            if (row == m - 1 or col == n - 1):   # Gold collected on going to
                right_down = 0                   # the cell to right down (\)
            else:
                right_down = goldTable[row + 1][col + 1]

            # Max gold collected from taking
            # either of the above 3 paths
            goldTable[row][col] = gold[row][col] + max(right, right_up, right_down)
    res = goldTable[0][0]
    for i in range(1, m):
        res = max(res, goldTable[i][0])
    return res

gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]

m = 4
n = 4

print(getMaxGold(gold, m, n))
