def MergeSort(array):
    if len(array) < 2:return array
    out,mid = [],int(len(array)/2)
    left = MergeSort(array[:mid])
    right = MergeSort(array[mid:])
    while (len(left) > 0) and (len(right) > 0):
            if left[0] > right[0]:out.append(right.pop(0))
            else:out.append(left.pop(0))
    out.extend(left+right)
    return out
