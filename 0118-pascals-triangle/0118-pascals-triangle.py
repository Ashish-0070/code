class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the Pascal's triangle with the first row
        result = [[1]]
        
        # Generate the remaining rows
        for i in range(1, numRows):
            row = [1]  # Start with the first element of the row being 1
            for j in range(1, i):
                # Each element is the sum of the two elements directly above it
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)  # End with the last element of the row being 1
            result.append(row)
        
        return result
