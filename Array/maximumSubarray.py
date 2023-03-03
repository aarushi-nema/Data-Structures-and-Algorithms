def maximumSubarray(arr):
    maxSoFar =  arr[0]
    currSum = 0

    for element in arr:
        if currSum < 0:
            curSum = 0
        curSum += element
        maxSoFar = max(currSum, maxSoFar)
    
    return maxSoFar

