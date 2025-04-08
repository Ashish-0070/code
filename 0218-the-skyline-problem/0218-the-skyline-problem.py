

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for L, R, H in buildings:
            events.append((L, -H, R))
            events.append((R, 0, 0))
        events.sort()

        result = [[0, 0]]
        heap = [(0, float('inf'))]  # (height, end)

        for x, negH, R in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)
            if negH:
                heapq.heappush(heap, (negH, R))
            if result[-1][1] != -heap[0][0]:
                result.append([x, -heap[0][0]])

        return result[1:]
