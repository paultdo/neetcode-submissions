class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = set()
        left = 0
        result = 0
        for r in range(len(s)):
            while s[r] in hash_map:
                hash_map.remove(s[left])
                left += 1
            hash_map.add(s[r])
            result = max(result, r - left + 1)
        
        return result

