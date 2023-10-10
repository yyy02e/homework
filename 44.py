def shellsort(nums):
    step = len(nums)//2
    while step > 0:
        for i in range(step, len(nums)):
            index = i
            while index >= step and nums[index-step] > nums[index]:
                nums[index], nums[index - step] = nums[index - step], nums[index]
                index -= step
        step //= 2
    print(nums)

nums = []
for i in range(0,8):
    a = int(input())
    nums.append(a)
shellsort(nums)
#时间复杂度为o(n^1.5) 空间复杂度