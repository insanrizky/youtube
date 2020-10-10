def singleNumber(nums):
    temp = []
    for item in nums:
        if item not in temp:
            temp.append(item)
        else:
            temp.remove(item)
    return None if len(temp) == 0 else temp.pop()

def singleNumber2(nums):
    temp = {}
    nonDuplicateNum = None
    for item in nums:
        if temp.get(item) is None:
            temp[item] = 1
            nonDuplicateNum = item
        else:
            temp[item] = temp[item] + 1
            if nonDuplicateNum == item:
                nonDuplicateNum = None
    return nonDuplicateNum

def singleNumber3(nums):
    temp = nums.pop()
    if nums.count(temp) > 0:
        nums.remove(temp)
        return singleNumber3(nums)
    return temp

def singleNumber4(nums):
    if len(nums) == 0: return 0
    return nums.pop() ^ singleNumber4(nums)

testCase = [4, 3, 2, 4, 1, 3, 2]
# print singleNumber(testCase)
# print singleNumber2(testCase)
# print singleNumber3(testCase)
print singleNumber4(testCase)
# 1