class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = 0
        hash_map = {}

        l, r = 0, 0

        while r < len(fruits):
            if len(hash_map.keys()) < 2 or fruits[r] in hash_map:
                if fruits[r] in hash_map:
                    hash_map[fruits[r]] += 1
                else:
                    hash_map[fruits[r]] = 1

                count = max(count, r - l + 1)
                r += 1
            elif len(hash_map.keys()) == 2:
                while len(hash_map.keys()) == 2:
                    hash_map[fruits[l]] -= 1
                    if hash_map[fruits[l]] == 0:
                        del hash_map[fruits[l]]
                    l += 1
                

        return count



