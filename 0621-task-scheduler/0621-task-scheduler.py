import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        
        max_heap = [-count for count in task_count.values()]
        heapq.heapify(max_heap)
        
        time = 0
        cooldown = []
        
        while max_heap or cooldown:
            time += 1  
            if max_heap:
                count = -heapq.heappop(max_heap)
                count -= 1 
                if count > 0:
                    cooldown.append((count, time + n))  
            
            if cooldown and cooldown[0][1] == time:
                count, _ = cooldown.pop(0)
                heapq.heappush(max_heap, -count)
        
        return time
