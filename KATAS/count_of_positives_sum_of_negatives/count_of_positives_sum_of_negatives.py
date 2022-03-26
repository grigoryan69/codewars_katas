def count_positives_sum_negatives(arr):
    conut_positive = 0
    count_negative = 0
    for i in arr:
        if i > 0: 
            conut_positive += 1
        elif i < 0:
            count_negative += i
    x = [conut_positive, count_negative]
    if len(arr) == 0:
        x = []
    return x