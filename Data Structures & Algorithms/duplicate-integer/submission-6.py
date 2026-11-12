class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mutable = set(nums)
        if (len(nums) != len(mutable)):
            return True
        else:
            return False