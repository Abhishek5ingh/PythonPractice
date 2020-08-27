class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums: 
            ind = nums.index(val)
            nums.pop(ind)
        len(nums)
