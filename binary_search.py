def binary_search(array, value):
    """
    Function for finding an element in a sorted array (vector) using array splitting in half.
    Returns first index of value.
    Raises ValueError if the value is not present.
    """
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == value:
            return mid
        if guess > value:
            high = mid - 1
        else:
            low = mid + 1
    raise ValueError('%s is not in list' % value)


if __name__ == '__main__':
    test_array = [5, 18, 19, 24, 40, 49, 49, 56, 62, 97]
    test_value = 49
    print(test_array)
    print("Element %s is present at index %s" % (test_value, binary_search(test_array, test_value)))
