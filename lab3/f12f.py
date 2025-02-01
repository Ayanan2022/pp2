def histogram():
    arr = input(" ").split()
    arr = [int(x) for x in arr]
    for i in range(len(arr)):
        print("*"*arr[i])

histogram()
