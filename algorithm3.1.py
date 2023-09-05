

# 3. 算法
#     1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.
#       Example1:
#       Input: nums = [2,7,11,15], target = 9
#       Output: [0,1]
#       Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#       Constraints:
#       2 <= nums.length <= 104
#       -109 <= nums[i] <= 109
#       -109 <= target <= 109
#       Only one valid answer exists.

numlist = input("nums=")
target = int(input("target="))
nums = []

print(numlist,target)

str1 = numlist.replace('[','').replace(']','')

str2 = str1.split(',')
for i in str2:
    nums.append(int(i))

num1 = None
num2 = None
result = []
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]<target:
                if (nums[j] < target):
                    if nums[i] + nums[j] == target:
                        result.append(i)
                        result.append(j)
                        break

print(result)