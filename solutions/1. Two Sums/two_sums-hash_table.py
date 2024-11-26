class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i in range(len(nums)):
            numbers[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numbers and i != numbers[complement]:
                return [numbers[complement], i]