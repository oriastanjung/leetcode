class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {}
            # from Answer Google  using heap map
        # for index, items in enumerate(nums):
        #     diff = target-items
        #     if(diff in prevMap):
        #         return [prevMap[diff], index]
        #     prevMap[items] = index
        # return
        
        for i in range (len(nums)):
            diff = target - nums[i]
            if(diff in prevMap):
                return [prevMap[diff], i]
            prevMap[nums[i]] = i
        return