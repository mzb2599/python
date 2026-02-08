# Sliding window algorithm implementation in Python
# This function calculates the sum of every contiguous subarray of size k in the given array. It uses a sliding 
# window approach to efficiently compute the sums without having to recalculate the sum for each subarray from scratch.
# Time complexity: O(n), where n is the length of the input array.
def sliding_window(arr, k):
    if not arr or k <= 0:
        return []

    result = []
    window_sum = sum(arr[:k])
    result.append(window_sum)

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        result.append(window_sum)

    return result

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 3
print(sliding_window(arr, k))  # Output: [6, 9, 12]