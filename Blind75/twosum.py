#Problem link: https://leetcode.com/problems/two-sum/submissions/887121573/

def twoSum(nums: list, target: int) -> list:
    prevMap = {} # val : index

    for i, n in enumerate(nums):
        diff = target-n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

    return 