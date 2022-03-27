def stray(arr):
    return None if len(set(arr)) <= 1\
        else [num for num in arr if arr.count(num) == 1][0]