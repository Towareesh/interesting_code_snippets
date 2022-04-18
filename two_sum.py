from random import randint

def two_sum(lst, k):
    hash_set = sorted([i for i in lst if k - i in lst])
    len_hash_set = len(hash_set)

    if len_hash_set == 2:
        return hash_set
    if len_hash_set == 0 or len_hash_set == 1:
        return [0]

    def binarySearch(hash_set, item):
        midpoint = len(hash_set)//2
        if hash_set[midpoint] == item:
            return item
        else:
            if item < hash_set[midpoint]:
                return binarySearch(hash_set[:midpoint], item)
            else:
                return binarySearch(hash_set[midpoint + 1:], item)

    for i in hash_set:
        search_result = binarySearch(hash_set, k - i)
        if search_result in hash_set:
            return [i, search_result]





lst = [randint(-50,100) for i in range(1000)]
k   = [randint(-100,100) for i in range(500)]

for i in k:
    se = two_sum(lst, i)
    if len(se) != 1:
        log = (se[0]+se[1]==i)
        print(i, se, log)