class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # assuming that the sorting algorithm takes O(logn) to run.
        temp = list(nums)
        temp.sort()

        startPointer = 0
        endPointer = len(temp) - 1 

        while startPointer < endPointer:
            if temp[startPointer] + temp[endPointer] > target:
                endPointer -= 1
            elif temp[startPointer] + temp[endPointer] < target:
                startPointer += 1
            else:
                startPointer = nums.index(temp[startPointer])
                nums[startPointer] = None
                endPointer = nums.index(temp[endPointer])

                return [startPointer, endPointer]