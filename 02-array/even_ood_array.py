# reorder the arr to even entries appear first
def even_ood(arr):
    next_even, next_odd = 0, len(arr) - 1
    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd += 1

'''
NOTE: 2 pointers
space: o(1)
time: o(n), n = arr length
'''