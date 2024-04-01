'''
Time: O(n)
Space: O(1)
'''

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    # first pass: group elements smaller than pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    # second pass: group elements larger than pivot
    larger = len(A) - 1
    for i in reversed(len(A)):
        # Stop when reach an element smaller than pivot, since the first pass moved them to the start of the array
        if A[i] < pivot:
            break
        else:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1

    return
