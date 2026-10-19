class Solution(object):
    def rotate(self, nums, k):

        temp = nums[:k] 

        for i in range(k, len(nums)):
            nums[i - k] = nums[i]
        j = 0

        for i in range((len(nums)-k),len(nums) ):
            nums[i] = temp[len(nums) -k]
            j +=1

