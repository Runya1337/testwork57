test_list = [1, 2, 3, 4, 5, 1, 2]

def unique_elements(lst):
    return list(set(lst))

def unique_elements_for(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

def unique_elements_list_comprehension(lst):
    return [item for i, item in enumerate(lst) if item not in lst[:i]]

print(unique_elements(test_list))
print(unique_elements_for(test_list))
print(unique_elements_list_comprehension(test_list))