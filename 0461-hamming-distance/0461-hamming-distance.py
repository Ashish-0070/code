class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR the two numbers and count the number of 1s in the result
        return bin(x ^ y).count('1')
