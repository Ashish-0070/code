class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""  
        
        for char in s:
            if char.isalnum():
                temp += char.lower()
        
        reversed_temp = temp[::-1]
        
        return temp == reversed_temp
