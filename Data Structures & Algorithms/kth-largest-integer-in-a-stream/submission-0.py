class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums.copy()
        self.k = k


    def add(self, val: int) -> int:
        self.heap.append(val)
        temp_heap = self.heap.copy()
        res = -float("inf")
        heapq.heapify_max(temp_heap)
        for i in range(self.k):
            res = heapq.heappop_max(temp_heap)
        
        return res