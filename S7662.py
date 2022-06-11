from sys import stdin as st

t = int(st.readline())

min_num = 2 ** 32
max_num = -min_num
q = []

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    sub_arr1 = merge_sort(arr[:mid])
    sub_arr2 = merge_sort(arr[mid:])

    merged_arr = []
    idx1, idx2 = 0, 0

    while idx1 < len(sub_arr1) and idx2 < len(sub_arr2):
        if sub_arr1[idx1] < sub_arr2[idx2]:
            merged_arr.append(sub_arr1[idx1])
            idx1 += 1
        else:
            merged_arr.append(sub_arr2[idx2])
            idx2 += 1
    merged_arr += sub_arr1[idx1:]
    merged_arr += sub_arr2[idx2:]
    return merged_arr

for _ in range(t):
    k = int(st.readline())
    for __ in range(k):
        work, num = st.readline().rstrip().split()

        if work == 'I':
            q.append(int(num))
            q = merge_sort(q)
        elif work == 'D':
            if q:
                if num == '-1':
                    del q[0]
                else:
                    del q[-1]

    if q:
        print(q[-1], q[0])
    else:
        print('EMPTY')