#two sum array
# This function takes an array of integers and a target sum, and returns the indices of the two numbers that add up to the target sum.

def two_sum(arr, target):
    num_to_index = {}

    for index, num in enumerate(arr):
        complement = target - num

        if complement in num_to_index:
            return [num_to_index[complement], index]

        num_to_index[num] = index

    return []  # Return an empty list if no solution is found
# Example usage:
arr = [2, 7, 11, 15]
target = 9
result = two_sum(arr, target)
print(f"Indices of numbers that add up to {target}: {result}")