class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            if i == 0:
                num += digits[i]
            else:
                num *= 10
                num += digits[i]
        
        num += 1
        tempNum = num
        count = 0
        while tempNum:
            tempNum = tempNum // 10
            count += 1
        
        result = [0] * count

        for i in range(len(result) - 1, -1, -1):
            digit = num % 10
            result[i] = digit
            num = num // 10
        
        return result
