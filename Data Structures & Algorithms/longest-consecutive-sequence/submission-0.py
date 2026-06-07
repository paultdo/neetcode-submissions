class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        count = 0

        for n in nums:
            if (n - 1) not in seen:
                length = 0
                while(n + length) in seen:
                    length += 1
                
                if length > count:
                    count = length
        

        return count


                
