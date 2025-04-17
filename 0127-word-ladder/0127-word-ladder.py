from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)
        
        queue = deque([(beginWord, 1)])
        
        visited = set()
        visited.add(beginWord)
        
        while queue:
            current_word, depth = queue.popleft()
            
            for i in range(len(current_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = current_word[:i] + char + current_word[i+1:]
                    
                    if new_word == endWord:
                        return depth + 1  
                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, depth + 1))
        
        return 0
