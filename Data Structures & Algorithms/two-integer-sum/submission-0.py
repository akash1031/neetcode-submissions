class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}

        for i, num in enumerate(nums):
            comp = target - num

            if comp in ind:
                return [ind[comp], i]
            
            ind[num] = i

        


        