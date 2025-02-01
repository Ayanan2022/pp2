def unique_elements():
    arr = input("input your elements: ").split()
    arr = [int(x) for x in arr]

    unique_list = []
    for num in arr:
        if num not in unique_list: 
            unique_list.append(num) 
    return unique_list



print(unique_elements())
