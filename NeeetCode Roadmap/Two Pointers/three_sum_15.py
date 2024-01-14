def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums = sorted(nums)
    print(nums)
    n =len(nums)
    res = []
    for i in range(n-2):
        if i>0 and nums[i-1] == nums[i]:
            continue
        l = i+1
        r = n-1
        sum = nums[i] * -1
        print(f"Sum required: {sum}")
        while l<r:
            curr_sum = nums[l] + nums[r]
            print(f"Current Sum: {curr_sum}")
            if curr_sum == sum:
                res.append([nums[i], nums[l], nums[r]])
                l=l+1
                while l<r and nums[l] == nums[l-1]:
                    l = l+1
            elif curr_sum > sum:
                r = r-1
            else:
                l = l+1
    return res
print(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))

[[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]