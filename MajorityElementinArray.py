class Solution:
    def majorityElement(self, nums):

        max_frequency = 0
        max_pair = None

        for i in range(len(nums)):
            count = 0


            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count = count + 1
            if count > (len(nums) //2):
                highest_frequency = count
                max_pair = nums[i]


        return count, max_pair


nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
sol = Solution()
max_frequence, max_pair = sol.majorityElement(nums)
print(max_frequence, max_pair)


