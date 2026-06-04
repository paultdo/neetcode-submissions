class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] 
        result = []
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        num = k
        i = len(freq) - 1
        while num:
            if len(freq[i]) == 0:
                i -= 1
                continue
            else:
                for j in freq[i]:
                    result.append(j)
                    num -= 1
                    if num == 0:
                        break
            if num == 0:
                break
            i -= 1

        return result




        

        
