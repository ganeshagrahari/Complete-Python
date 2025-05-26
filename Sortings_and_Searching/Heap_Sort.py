def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]  # Swap elements at indices i and j

def shiftdown(arr, i, upper):
    while True:
        left = 2 * i + 1       # Left child
        right = 2 * i + 2      # Right child
        largest = i

        # Check if left child is larger
        if left < upper and arr[left] > arr[largest]:
            largest = left

        # Check if right child is larger
        if right < upper and arr[right] > arr[largest]:
            largest = right

        # If no swaps needed, heap property is satisfied
        if largest == i:
            break

        swap(arr, i, largest)  # Swap with the larger child
        i = largest            # Continue shifting down

def heapsort(arr):
    n = len(arr)

    # Step 1: Build max heap
    for i in range(n // 2 - 1, -1, -1):  # Start from last non-leaf node
        shiftdown(arr, i, n)

    # Step 2: Extract max and sort
    for i in range(n - 1, 0, -1):
        swap(arr, 0, i)          # Move current max to the end
        shiftdown(arr, 0, i)     # Heapify the root element again

# Example usage
arr = [10, 3, 76, 34, 23, 32]
heapsort(arr)
print("Sorted array:", arr)
