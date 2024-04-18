# nums = [3,6,9,1]
# diffs = []
# def sort_diff(nums):
#     l = len(nums)
#     for i in range(l):
#             for j in range(0,l-i-1):
#                 if nums[j] < nums[j+1]:
#                         nums[j],nums[j+1] = nums[j+1],nums[j]
#     print(nums)
#     for i in range(0,l-1):
#         diff = (nums[i]- nums[i+1])
#         diffs.append(diff)
#     print("Maximum Difference:",max(diffs))
# sort_diff(nums)




nums = [2,5,6,3,9]

def sort_diff(nums):
    l = len(nums)
    for i in range(l):
        for j in range(0,l-i-1):
            if nums[j]<nums[j+1]:
                nums[j],nums[j+1]= nums[j+1],nums[j]
    max_difference = float("-inf")
    for i in range(0,l-1):
        difference = nums[i] - nums[i+1]
        if difference > max_difference:
            max_difference = difference
    print(nums)
    print(max_difference)

sort_diff(nums)