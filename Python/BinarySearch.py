lis = [1, 28, 34, 45, 47, 58, 59, 62, 74, 82, 87, 90]
def binary_search (ar, num):
    n=2
    min=0
    max=ar.__len__()

    i = max-min//2
    if ar[i] == num : return i
    elif ar[i] < num : min = i
    elif ar[i] > num: max = i
    return b

print(binary_search(lis))






