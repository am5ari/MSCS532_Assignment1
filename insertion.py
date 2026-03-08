
# Define the monotonic insertion sort function
def monotonic_insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

