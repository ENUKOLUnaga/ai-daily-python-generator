def two_sum(nums, target):
    # create a dictionary to store the numbers we've seen so far and their indices
    num_dict = {}
    # iterate over the list of numbers with their indices
    for i, num in enumerate(nums):
        # calculate the complement of the current number
        complement = target - num
        # check if the complement is in the dictionary
        if complement in num_dict:
            # return the indices of the current number and its complement
            return [num_dict[complement], i]
        # if not, add the current number and its index to the dictionary
        num_dict[num] = i
    # if no solution is found, return None
    return None

# test the function
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]