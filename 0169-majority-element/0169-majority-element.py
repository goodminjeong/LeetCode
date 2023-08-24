class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = 0
        nums_set = set(nums)
        for num in nums_set:
            if nums.count(num) >= nums.count(answer):
                answer = num
        return answer
            