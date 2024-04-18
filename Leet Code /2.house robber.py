# def rob(nums):
#     if not nums:
#         return 0
#     if len(nums) == 1:
#         return nums[0]
    
#     # Initialize two variables to store the maximum amount of money robbed with or without robbing the current house
#     rob_current = nums[0]
#     rob_next = max(nums[0], nums[1])
    
#     for i in range(2, len(nums)):
#         # Calculate the maximum amount of money if the current house is robbed
#         current_rob = rob_current + nums[i] 
#         # Update rob_current to be the maximum between the previous rob_next and the current_rob
#         rob_current = rob_next 
#         # Update rob_next to be the maximum between the previous rob_next and current_rob
#         rob_next = max(rob_next, current_rob)
    
#     return rob_next

# # Test cases
# nums1 = [1, 2, 3, 1]
# nums2 = [2, 7, 9, 3, 1]

# print(rob(nums1))  # Output: 4
# print(rob(nums2))  # Output: 12

####################################################################
# num = [2, 7, 9, 3, 1,3,4]
# n = len(num)

# for i in range(2, n):
#     print(i)
#     print(num[i])
#     num[i] += max(num[i - 2], 0)  # Add the maximum amount from two houses before the current house
#     print(num[i])
#     print("---------")

# print(max(num[-1], num[-2]))  # Output the maximum amount of money that can be robbed

def rob(nums):
    prev_max = 0  # Maximum amount of money that can be robbed from the previous house
    curr_max = 0  # Maximum amount of money that can be robbed considering the current house

    for money in nums:
        temp = curr_max  # Store the current maximum amount of money temporarily
        print(money, "Money")
        print(temp,"Temp")
        curr_max = max(prev_max + money, curr_max)  # Update the current maximum amount of money
        print(curr_max,"Curr Max")
        prev_max = temp  # Update the previous maximum amount of money for the next iteration
        print(prev_max,"Prev Max")
        print("------")
    return curr_max

# Test cases
nums2 = [2, 7, 9, 3, 1]
print(rob(nums2))  # Output: 12

