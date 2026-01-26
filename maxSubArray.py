def max_sub_array(arr):
    # max_current = local maximum sum ending at the current index
    # max_global = absolute maximum sum found in the entire array so far
    max_current = max_global = arr[0]
    
    for i in range(1, len(arr)):
        # DECISION POINT: Does adding the previous running sum help?
        # If max_current was negative, it would decrease the value of arr[i].
        # In that case, we start fresh at arr[i].
        max_current = max(arr[i], max_current + arr[i])
        
        # Keep track of the highest local maximum we've ever seen
        if max_current > max_global:
            max_global = max_current
            
    return max_global

# Example usage:
array = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sub_array(array))  # Output: 6