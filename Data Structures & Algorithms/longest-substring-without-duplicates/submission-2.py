class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        l, r = 0, 0
        hash_set = set()

        while r < len(s):
            if s[r] not in hash_set:
                hash_set.add(s[r])
                r += 1
                count = max(r - l, count)
            else:
                hash_set.remove(s[l])
                l += 1
        
        return count