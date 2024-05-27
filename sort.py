def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def replace_elements(arr, target, replacement):
    return [replacement if x == target else x for x in arr]

def main():
    # Prompt the user to input an array of integers
    input_array = input("Enter an array of integers separated by spaces: ")
    
    # Store the elements in an array in a Python list
    arr = list(map(int, input_array.split()))

    print(f"Array: {arr}")
    # Sort the array using quick sort
    sorted_arr = quick_sort(arr)
    print(f"Sorted array: {sorted_arr}")
    
    # Allow the user to specify a target element to search for in the sorted array
    target = int(input("Enter the element to search for: "))
    
    # If the target element is found, prompt the user to input a replacement element
    if target in sorted_arr:
        replacement = int(input("Enter the replacement element: "))
        
        # Replace all occurrences of the target element with the replacement element
        modified_arr = replace_elements(sorted_arr, target, replacement)
        
        # Display the modified array after replacing the elements
        print(f"Modified array after replacing: {modified_arr}")
    else:
        print("Element not found in the iven array.")

if __name__ == "__main__":
    main()
