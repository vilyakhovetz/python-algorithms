def max_subarray_sum(array):
    """
    Function for finding the largest possible sum of a contiguous subarray.
    """
    local_max = global_max = 0
    for num in array:
        local_max = max(num, num + local_max)
        global_max = max(global_max, local_max)
    return global_max


if __name__ == '__main__':
    test_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print('The maximum sum of a contiguous subsequence =', max_subarray_sum(test_array))
