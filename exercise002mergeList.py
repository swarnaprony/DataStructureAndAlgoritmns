def mergeList(list_1, list_2):

    merge_list = []
    i=0
    j=0
    while (i < len(list_1) and j < len(list_2)):
        if list_1[i] <= list_2[j]:
            merge_list.append(list_1[i])
            i = i+1
        else:
            merge_list.append(list_2[j])
            j = j+1
    if i == len(list_1) and j == len(list_2):
        return merge_list
    if i == len(list_1):
        while j < len(list_2):
            merge_list.append(list_2[j])
            j=j+1
        return merge_list

    if i == len(list_2):
        while i < len(list_1):
            merge_list.append(list_1[i])
            i=i+1
        return merge_list

l1 = [2, 3, 6, 8, 11, 12.5,14, 15, 16]
l2 = [4, 6, 10, 11, 12, 13, 19, 20, 21, 25]

print(mergeList(l1, l2))