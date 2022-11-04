# def two_sum(arr, target):
#     for first_element in range(len(arr)):
#         for second_element in range( len(arr) + 1):
    
    
#             return first_element, second_element
#             # if first_element + second_element == target:
#     #             first_index = arr[first_element]
#     #         else:
#     #             second_index = arr[second_element]
    
#     # return first_index, second_index

# print(two_sum([1,2,4,3,3], 6))

# arr = [23,2,3,3,4,3,2], 4
# dict = {}
# for i in range(len(arr)):
#     if arr[i] in dict:
#         dict[arr[i]] += 1
#     else:
#         dict[arr[i]] = 1
# print(dict)
def twoSum(nums,target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i 
print(twoSum([2,3,5,5,1],3))
