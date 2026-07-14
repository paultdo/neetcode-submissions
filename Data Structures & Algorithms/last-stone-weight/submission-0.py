class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            if x < y:
                y = y - x
                heapq.heappush_max(stones, y)
            elif y < x:
                x = x - y
                heapq.heappush_max(stones, x)
        
        if not stones:
            return 0
        
        return stones[0]
        