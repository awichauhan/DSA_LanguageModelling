class Solution(object):
    def majorityElement(self, nums):

        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for key in freq:
            if freq[key] > len(nums) / 2:
                return key

        return None


nums = [2, 2, 1, 1, 1, 2, 2]
sol = Solution()
print(sol.majorityElement(nums))