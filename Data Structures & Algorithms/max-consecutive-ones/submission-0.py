class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # test cases
        # [0], [1], [0,1,1], [1,0,1,1]
        # [1,1,0,1,1,1]
        max_number = 0
        current_number = 0
        for x in nums:
            if x == 1:
                current_number += 1
                if current_number > max_number:
                    max_number = current_number
            else:
                current_number = 0

        return max_number