
# Define the monotonic insertion sort function
def monotonic_insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    # Main function to execute the sorting
    user_input = input("Enter numbers separated by spaces: ")

    # Convert the input string into a list of integers
    numbers = list(map(int, user_input.split()))

    print("Original list:", numbers)

    # Sort the numbers
    monotonic_insertion(numbers)

    print("Sorted list in monotonically decreasing order:", numbers)