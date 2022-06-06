import random


def binary_search(low, high, answer, tentativa):
    # Check base case
    tentativa += 1
    if high >= low:

        mid = (high + low) // 2
        print(mid)
        # If element is present at the middle itself
        if mid == answer:
            return mid, tentativa

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif mid > x:
            return binary_search(low, mid - 1, answer, tentativa)

        # Else the element can only be present in right subarray
        else:
            return binary_search(mid + 1, high, answer, tentativa)

    else:
        # Element is not present in the array
        return -1


# Test array

x = random.randint(1, 100)

# Function call
result = binary_search(1, 100, x, 0)

if result != -1:
    print("Element is present at index", str(result[0]) + ' com ' + str(result[1]) + " tentativas")
else:
    print("Element is not present in array")
