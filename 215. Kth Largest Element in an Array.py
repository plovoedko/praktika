class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums1=sorted(nums)
        u=len(nums)-k
        return nums1[u]
