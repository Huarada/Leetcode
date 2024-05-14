
#Given an integer array nums, 
# returns all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #num1 = nums[0]
        #num2 = num[1]
        #num3 = num[2]
        sums = []
        for i in range(len(nums)) :
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if( (nums[i] + nums[j] + nums[k]) == 0 and (i != j and i != k and j != k ) ):
                        if( i >j and i > k and j > k): #only 1 iteration of the result in the list
                        
                            sums.append([nums[i],nums[j],nums[k]])
        
    
        result = [] 
        for i in sums: 
            if i not in result: 
                result.append(i) 

        return result
