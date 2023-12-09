# CMSC398L Final Presentation
Dalton Pang

## Problem - kSum
Given an array nums of $n$ integers, return an array of all the unique combinations of $k$ numbers such that:

- $0\le i < k$ for $a_i$,  where $a_i$ is the $ith$ number in the array
- all $i$ are distinct in the combination
- the sum of the combination of $a_i$'s is equal to the target
- The answer can be in any order

## What I Like About This Problem
This is a problem that builds off a classic leetcode problem that most if not all of us have started out with when grinding to get a SWE internship or job. The original version of this problem is called 2Sum where we very similarly try to find pairs of numbers in an array that add up to a target. After solving this "base case" you can actually build on top of it, doing 3Sum, 4Sum, and so on and so forth. What I like about this problem is that you can implement a general solution that works for all kSum problems. I found it really cool that one of our first leetcode problems that we have done has a general solution that works for all $k$. 

## Solution
A very important part in the implementing the solution to this problem is that fact that we find all unique combinations that add up to the target. The first thought is to just keep track of all the numbers we have gone through to see if we have visited them already, but that requires extra space and may even require a significant amount of time if $k$ gets large. The solution for the unique combinations is to sort the whole array before processing so that when we traverse it from start to end we can rule out duplicates since duplicates of numbers will all be next to each other.

The next step is to actually find the combinations of $k$ unique numbers in the array. To actually do this we just look at all combinations of $k-2$ unique numbers in the array then apply the base case to that combination. What is the base case? Well it is just 2Sum! I mentioned that 2Sum is the base problem for the series of kSum problems, and it is exactly that. It is the base case for the kSum problem! This means we will have to recurse through the array until we picked $k-2$ numbers, and then apply 2Sum to see if we can find the last two unqiue number that adds up to our target number. Go through the whole array doing this, and we have found all the unique combinations of $k$ numbers that sum up to our target!

Here is a Python implementation
```python
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
```

Examples
```python
#2Sum, nums = [2,7,11,15], target = 9
solution(2,[2,7,11,15],9) == [[2,7]]

#3Sum, nums = [-1,0,1,2,-1,-4], 0
solution(3,[-1,0,1,2,-1,-4],0) == [[-1,-1,2],[-1,0,1]]

#4Sum, nums = [1,0,-1,0,-2,2], target = 0
solution(4,[1,0,-1,0,-2,2],0) == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```
## Time and Space Complexity

### Time Complexity
$O(n^{k-1})$ where n is the number of numbers in the input array and k is the kSum. The higher the k value the more loops we do in our algorithm.

### Space Complexity 
$O(n)$ where n is the number of numbers in the input array. We need at least $O(k)$ space to keep track of the current combination we are looking at in our recursion. $k$ can be equal to n in the worst case.