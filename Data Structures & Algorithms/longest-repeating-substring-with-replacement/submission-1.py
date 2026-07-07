class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        res = 0
        hash_map = defaultdict(int)
        while right < len(s):
            hash_map[s[right]] += 1
            windowLength = right - left + 1
            if windowLength - max(hash_map.values()) <= k:
                res = max(res, windowLength)
            else:
                hash_map[s[left]] -= 1
                left += 1
            
            right += 1
        
        return res
