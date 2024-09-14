def stabilize_matrix(matrix, n, m):
    while True:
        max_val = float('-inf')
        max_pos = (-1, -1)
        # Find the cell with strictly greater value than all its neighbors
        for i in range(n):
            for j in range(m):
                if matrix[i][j] > max_val:
                    is_max = True
                    if i > 0 and matrix[i][j] <= matrix[i-1][j]:
                        is_max = False
                    if i < n-1 and matrix[i][j] <= matrix[i+1][j]:
                        is_max = False
                    if j > 0 and matrix[i][j] <= matrix[i][j-1]:
                        is_max = False
                    if j < m-1 and matrix[i][j] <= matrix[i][j+1]:
                        is_max = False
                    if is_max:
                        max_val = matrix[i][j]
                        max_pos = (i, j)

        
        if max_pos == (-1, -1):
            break
        
        # Decrease the value of the found cell
        i, j = max_pos
        matrix[i][j] -= 1
    
    return matrix

# Input reading
import sys
input = sys.stdin.read
data = input().split()
index = 0

t = int(data[index])
index += 1

results = []

for _ in range(t):
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    matrix = []
    for i in range(n):
        row = list(map(int, data[index:index + m]))
        matrix.append(row)
        index += m
    
    stabilized_matrix = stabilize_matrix(matrix, n, m)
    results.append(stabilized_matrix)

# Output results
for result in results:
    for row in result:
        print(' '.join(map(str, row)))
