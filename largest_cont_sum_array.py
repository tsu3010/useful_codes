# Given an array of integers (positive and negative), find the largest continuous sum.

# Soln : Start summing the numbers and store them in a variable called current sum. After adding each element,
# check if the current sum is greater than max sum encountered. If yes, replace the max sum with current sum.
# As long as current sum is positive, we keep adding numbers. When it becomes negative, we reset and start with the
# new current sum.

def largest_cont_sum_array(arr):
    """
    :param arr:
    :return:
    """
    if len(arr) == 0:
        raise ValueError("Array has no elements")
    current_sum = arr[0]
    max_sum = arr[0]
    for index,num in enumerate(arr[1:]):
        # Reset current sum to current number, if current sum turns negative
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
        print(f"Current sum at iteration {index}, number {num} is : {current_sum}")
        print(f"Max sum at iteration {index}, number {num} is : {max_sum}")
    return max_sum


arr1 = [1,2,3]
arr2 = [1,-10,2,3,-4,5]
arr3 = [-10,-1,-15,-2]
arr4 = [-10,-1,5,-12]
arr5 = [10,-1,5,-12]
arr6 = [10,-1,15,-12]

largest_cont_sum_array(arr1)
largest_cont_sum_array(arr2)
largest_cont_sum_array(arr3)
largest_cont_sum_array(arr4)
largest_cont_sum_array(arr5)
largest_cont_sum_array(arr6)