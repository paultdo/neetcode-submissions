class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        result = []

        for s in strs:
            char_count = [0] * 26
            for c in s:
                char_count[ord(c) - ord('a')] += 1
            
            hash_map[tuple(char_count)].append(s)
        

        return list(hash_map.values())
