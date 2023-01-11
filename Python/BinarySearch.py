lis = [1, 28, 34, 45, 58, 58, 58, 62, 74, 82, 87, 90]
def binary_search (ar, num):

    _min = 0
    _max = ar.__len__() - 1
    if ar[0] == num: return _min + 1
    if ar[_max] == num: return _max + 1
    while  (_max - _min) != 1:
       i = _min + (_max - _min)//2
       if ar[i] == num:
           return str(i+1)
       elif ar[i] < num:
           _min = i
       elif ar[i] > num:
           _max = i
    return "null"

print(binary_search(lis, 58))






