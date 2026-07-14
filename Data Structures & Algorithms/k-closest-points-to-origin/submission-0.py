class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in range(len(points)):
            dist = ((points[i][0] ** 2) + (points[i][1] ** 2)) ** 0.5
            distances.append((dist, i))
        
        heap = []
        for dist in distances:
            heap.append(dist)
        

        heapq.heapify(heap)

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap))
        
        for i in range(len(res)):
            res[i] = points[res[i][1]]
        

        return res
