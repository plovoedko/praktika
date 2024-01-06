class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i]==nums[i]:
                nums.append(nums[i])
        return nums