def battleship(arr):
    count = 0
    
    for row in range(0, len(arr)):
        for col in range(0, len(arr[0])):
            if arr[row][col] == 'X':
                current = 1

                if row > 0 and arr[row - 1][col] == 'X':
                    current = 0
                
                if col > 0 and arr[row ][col - 1] == 'X':
                    current = 0
                
                count += current
    
    return count




arr = [['X','.','.','X'], ['.','.','.','X'], ['.','.','.','X']]
print(battleship(arr))
