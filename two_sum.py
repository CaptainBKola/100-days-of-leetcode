"""
Solution Tips
We can actually complete it
in a single pass. When iterating 
and adding elements to the hash table 
we additionally take a step back to see if
the complement of the already added element 
already exists there. If it does, 
we have a solution and may instantly return the indices.
"""

def twoSum(nums,target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i 
print(twoSum([2,3,5,5,1],3))

