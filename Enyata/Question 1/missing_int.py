def findFirstMissingPositive(arr):
    n = len(arr)

    # Rearrange the list so each number occupies its correct position
    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
            # Swap elements to their correct positions
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]

    # This loop identifies the first missing positive integer
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1

    # If all numbers are in the correct positions,return the next positive integer
    return n + 1


# Tests:
print(findFirstMissingPositive([3, 4, -1, 1]))  # Output = 2
print(findFirstMissingPositive([1, 2, 0]))  # Output = 3
print(findFirstMissingPositive([1, 2, 0, 5, 4, 7, 9, 11, 13, 3, 6]))  # Output = 8
