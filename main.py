def intersectionOfSets(list1, list2, list3):
    s1 = set(list1)
    s2 = set(list2)
    s3 = set(list3)
    s1 = s1.intersection(s2)
    final_set = s1.intersection(s3)
    final_list = list(final_set)
    return final_list

list1 = [12, 3, 40, 56, 67]
list2 = [12, 31, 40, 36, 68]
list3 = [12, 3, 40, 564, 69]
print(intersectionOfSets(list1, list2, list3))