
def reverse_list(my_list):
    """
    Reverse the values in a list containing exactly two numbers.

    Input:
    lst (list): A list containing exactly two numbers.

    Returns:
    list: The list with its two values swapped.
    
    Example:
    --------
    >>> reverse_list([5, 10])
    [10, 5]

    """
   
    # Reverse the values in the list
    # Complete your code here...
    for i in range(len(my_list)):
        if i < int(len(my_list)/2):
            temp = my_list[i]
            my_list[i] = my_list[(len(my_list)-1) - i]
            my_list[(len(my_list)-1) - i] = temp
    return my_list

list = [5,10]
#list.reverse()
list = reverse_list(list)
print(list)