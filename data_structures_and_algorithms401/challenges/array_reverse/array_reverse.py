def reverse_array(arr):
    """Reverses a list

    Args:
        arr (list): python list

    Returns:
        [list]: list in reversed form
    """
    # put your function implementation here
    lis2=[]
    for i in range(len(arr)-1,-1,-1):
       lis2.append(arr[i])
    return lis2

# print(reverse_array([11, 21, 32, 63, 84, 55]))