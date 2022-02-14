def quicksort(array, reverse=False):
    """
    Function for sorting the list in ascending order.
    The reverse flag can be set to sort in descending order.
    Returns new list.
    """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        if reverse:
            left = [i for i in array[1:] if i >= pivot]
            right = [i for i in array[1:] if i < pivot]
            return quicksort(left, reverse=True) + [pivot] + quicksort(right, reverse=True)
        else:
            left = [i for i in array[1:] if i <= pivot]
            right = [i for i in array[1:] if i > pivot]
            return quicksort(left) + [pivot] + quicksort(right)


if __name__ == '__main__':
    test_array = [17, 30, 82, 39, 79, 98, 4, 53, 21, 32]
    print(test_array)
    print("Ascending order:", quicksort(test_array))
    print("Descending order:", quicksort(test_array, reverse=True))
