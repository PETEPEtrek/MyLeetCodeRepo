class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        answer = 0
        count = 0
        for elem in nums:
            if elem == 0:
                count += 1
            else:
                count = 0
            answer += count
        return answer
