from typing import List

def print_matrix(matrix):
    for i in matrix:
        print(i)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        matrix_width = len(matrix)
        row_start = col_start = 0
        row_end = col_end = matrix_width-1
        for i in range(1 if matrix_width==2 else matrix_width-2):
            row_start_pointer = row_start
            row_end_pointer = row_end
            col_start_pointer = col_start
            col_end_pointer = col_end
            inc = 0
            dic = 0
            for x in range(row_end-row_start):
                val = matrix[row_start_pointer][col_start_pointer+inc]
                
                # start, start -> start, end
                temp = matrix[row_start_pointer+inc][col_end_pointer]
                matrix[row_start_pointer+inc][col_end_pointer] = val
                val = temp
                print("Step 1")
                print_matrix(matrix)

                # start, end -> end, end
                temp = matrix[row_end_pointer][col_end_pointer-dic]
                matrix[row_end_pointer][col_end_pointer-dic] = val
                val = temp
                print("Step 2")
                print_matrix(matrix)

                # end, end -> end, start
                temp = matrix[row_end_pointer-dic][col_start_pointer]
                matrix[row_end_pointer-dic][col_start_pointer] = val
                val = temp
                print("Step 3")
                print_matrix(matrix)

                # end, start -> start, start
                # temp = matrix[row_start_pointer][col_end_pointer]
                matrix[row_start_pointer][col_start_pointer+inc] = val
                print("Step 4")
                print_matrix(matrix)
                print("------------------------")
                inc += 1
                dic += 1
                # break

            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1

sol = Solution()
sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])


