class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = defaultdict(int)
        l, r = 0, 0
        count = 0
        while r < len(s):
            hash_map[s[r]] += 1
            windowLen = r - l + 1
            mostFrequent = max(hash_map.values()) if hash_map else 0

            if windowLen - mostFrequent < k:
                r += 1
                count = max(windowLen, count)
            elif windowLen - mostFrequent > k:
                hash_map[s[l]] -= 1
                l += 1
                r += 1
            else:
                r += 1
                count = max(windowLen, count)
        
        return count


