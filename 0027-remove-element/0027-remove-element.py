class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for num in nums[::-1]:
            if num == val:
                nums.remove(num)
        return len(nums)