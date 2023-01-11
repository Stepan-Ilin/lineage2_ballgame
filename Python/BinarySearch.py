lis = [1, 28, 34, 45, 47, 58, 59, 62, 74, 82, 87, 90]
def binary_search (ar, num):

    _min = 0
    _max = ar.__len__() - 1
    while  (_max - _min) != 1:
       i = _min + (_max - _min)//2
       if ar[i] == num:
           return str(i)
       elif ar[i] < num:
           _min = i
       elif ar[i] > num:
           _max = i
    return "null"

print(binary_search(lis, 83))






