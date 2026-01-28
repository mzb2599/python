# Flatten array: Convert a nested array into a single-level array.

def flatten_array(nested_arr):
    flat_arr = []
    
    for element in nested_arr:
        if isinstance(element, list):
            # Recursively flatten the sub-array
            flat_arr.extend(flatten_array(element))
        else:
            # Append the non-list element to the flat array
            flat_arr.append(element)
    
    return flat_arr

# Example usage:
nested_array = [1, [2, [3, 4], 5], 6, [7, 8]]
flattened = flatten_array(nested_array)
print("Flattened array:", flattened)