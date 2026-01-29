# Remove duplicates from a list while preserving the order of first occurrences

def remove_duplicates(input_list):
    seen = set()
    output_list = []
    
    for item in input_list:
        if item not in seen:
            seen.add(item)
            output_list.append(item)
    
    return output_list
# Example usage:
input_list = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list = remove_duplicates(input_list)
print(unique_list)