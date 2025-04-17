class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)  
        visited = [False] * n  
        
        def dfs(city: int):
            visited[city] = True 
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
        
        provinces = 0
        
        for city in range(n):
            if not visited[city]:  
                dfs(city)  # Perform DFS to visit all cities in this province
                provinces += 1 
        
        return provinces
