def solution(k,nums,target):
    comb = [] #combs is used to keep track of the current combination of numbers
    res = [] #list that we will be updating with combinations that add up to target
    nums.sort() #sort so that we do not get duplicate combinations
    def kSum(k,start,target):
        if k == 2: #2Sum base case
            res.extend(twoSum(start,target,comb))
            return

        #Loop through to find all unique combinations 
        for i in range(start,len(nums) - k + 1): 
            #if the current number that is not start is the same as the previous then it is going to be a duplicate combination
            if i > start and nums[i] == nums[i-1]:
                continue
            comb.append(nums[i])
            kSum(k-1,i+1,target-nums[i]) #subtracts nums[i] from target so that we can find the last two numbers
            comb.pop()

    #finds the two numbers that add up to target
    def twoSum(start,target,comb):
        l,r = start, len(nums)-1
        ans = []
        while l<r:
            if nums[l] + nums[r] > target:
                r-=1
            elif nums[l] + nums[r] < target:
                l+=1
            else:
                ans.append(comb + [nums[l],nums[r]])
                l+=1
                while l < r and nums[l] == nums[l-1]:
                    l+=1   
        return ans
    

    kSum(k,0,target)
    return res