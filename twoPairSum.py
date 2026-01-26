#Two Sum / Pair Sum: Check if a pair exists in an array that equals a target sum.

def two_pair_sum(arr, target_sum):
    seen_numbers = set()
    
    for number in arr:
        # Calculate the complement that would sum with the current number to reach the target
        complement = target_sum - number
        # Check if we've already seen the complement
        if complement in seen_numbers:
            # Return the indices of the two numbers that add up to the target sum
            return arr.index(complement), arr.index(number)
        # Add the current number to the set of seen numbers
        seen_numbers.add(number)
    
    return False

# Example usage:
array = [10, 15, 3, 7]
target = 17
result = two_pair_sum(array, target)
if result:
    print(f"Pair found at indices: {result}")
else:
    print("No pair found")