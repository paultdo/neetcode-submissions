class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [cnt for cnt in count.values()]
        heapq.heapify_max(maxHeap)

        time = 0

        queue = deque() # pairs of (cnt, idle time)

        while maxHeap or queue:
            time += 1

            if maxHeap:
                cnt = heapq.heappop_max(maxHeap) - 1
                if cnt:
                    queue.append([cnt, time + n])
            
            if queue and queue[0][1] == time:
                heapq.heappush_max(maxHeap, queue.popleft()[0])
        
        return time
        