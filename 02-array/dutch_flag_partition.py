'''
2 pass, 2 pointers
Time: O(n)
Space: O(1)


def dutch_flag_partition(pivot_index: int, A: list[int]) -> None:
    pivot = A[pivot_index]
    # first pass: group elements smaller than pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    # second pass: group elements larger than pivot
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        # Stop when reach an element smaller than pivot, since the first pass moved them to the start of the array
        if A[i] < pivot:
            break
        else:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1
    print(A)
'''

'''
1 pass, 2 pointers
Time: O(n)
Space: O(1)
'''

def dutch_flag_partition(pivot_index: int, A: list[int]) -> None:
    pivot = A[pivot_index]
    smaller, current, larger = 0, 0, len(A)
    while current < larger:
        if A[current] < pivot:
            A[current], A[smaller] = A[smaller], A[current]
            smaller += 1
            current += 1
        elif A[current] == pivot:
            current += 1
        else:
            larger -= 1
            A[current], A[larger] = A[larger], A[current]

    print(A)


print(dutch_flag_partition(4, [-2, 0, -1, 1, 1, 3, 4, 5, 2]))