def merge_sort(a_list):
    print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left = a_list[:mid]
        right = a_list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a_list[k] = left[i]
                i=i+1
            else:
                a_list[k] = right[j]
                j=j+1
                k=k+1
        while i < len(left):
            a_list[k] = left[i]
            i=i+1
            k=k+1
        while j < len(right):
            a_list[k] = right[j]
            j=j+1
            k=k+1
   print("Merging ", a_list)
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)
