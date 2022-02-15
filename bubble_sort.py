def bubble_sort(array, reverse=False):
    """
    Function for sorting the list in ascending order.
    The reverse flag can be set to sort in descending order.
    Returns new list.
    """
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if reverse:
                if array[j] < array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    swapped = True
            else:
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    swapped = True
        if not swapped:
            break
    return array


if __name__ == '__main__':
    test_array = [7, 85, 49, 22, 85, 93, 1, 89, 48, 80]
    print(test_array)
    print("Ascending order:", bubble_sort(test_array))
    print("Descending order:", bubble_sort(test_array, reverse=True))
