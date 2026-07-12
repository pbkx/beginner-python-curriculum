nums = [9, 10, 4, 1, 3, 7, 2]
print(nums)

# You can use built-in Python functions to find the biggest and smallest items.
biggest_item = max(nums)
smallest_item = min(nums)

print("The biggest item:", biggest_item)
print("The smallest item:", smallest_item)

print("Our algorithm:")

biggest = nums[0]  # Start by assuming the first item is the biggest
for i in range(len(nums)):  # Go throug each item in the list
    if nums[i] > biggest:  # If we find something bigger, update our guess
        biggest = nums[i]

print("The biggest item:", biggest)