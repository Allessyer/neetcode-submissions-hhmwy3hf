class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        idx = 0
        nums_len = len(nums)
        while idx < nums_len:
            if nums[idx] == val:
                nums.pop(idx)
                nums_len = len(nums)
            else:
                idx += 1
        
        
        return len(nums)