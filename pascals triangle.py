class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        if numRows == 0:
            return triangle

        # The first row is always [1]
        triangle.append([1])

        # Generate subsequent rows
        for i in range(1, numRows):
            previous_row = triangle[i - 1]
            current_row = [1]

            # Each number is the sum of the two numbers directly above it
            for j in range(len(previous_row) - 1):
                current_row.append(previous_row[j] + previous_row[j+1])
            
            current_row.append(1)
            triangle.append(current_row)
        
        return triangle