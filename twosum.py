def twosum(nums, target):
    hm = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in hm :
            return [hm[complement], index]
        hm[value] = index

print(twosum([2,7,11,15], 9))
print(twosum([3,2,4], 6))
print(twosum([3,3],6))