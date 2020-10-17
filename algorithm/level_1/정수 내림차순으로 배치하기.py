def solution(n):
    # TypeError: sequence item 0: expected str instance, int found
    # answer = 0
    answer = []

    # TypeError: 'int' object is not iterable
    # answer = list(map(str, n))
    # answer = list(map(int, str(n))).sort() -> None 결과가 나옴

    # AttributeError: 'list' object has no attribute 'sorted'
    # answer = list(map(int, str(n))).sorted()

    # answer = list(map(int, str(n))) # -> map을 굳이 할 필요가 없었음.
    answer = list(str(n))
    answer.sort(reverse=True)
    print(answer)

    # answer = [str(i) for i in answer] # 이렇게 하면 결과와 일치하긴 하나 틀렸다고 나옴.

    # TypeError: 'int' object is not iterable
    # answer = list(map(str, n))

    # TypeError: sequence item 0: expected str instance, int found
    # return ''.join(answer)

    return int(''.join(answer))  # -> int로 해줘야 정답이 됨.



#############################################################################

# 다른 풀이

def solution(n):
    answer = ''
    lst = []

    while n > 0:
        r = n % 10
        n = n // 10
        lst.append(r)

    lst.sort()
    lst.reverse()

    for j in range(0, len(lst)):
        answer += str(lst[j])

    return int(answer)


#############################################################################

# 다른 풀이 - merge sort / 한번 이렇게 풀어볼 것.

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] >= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def solution(n):
    arr = list(str(n))
    n = int(''.join(mergeSort(arr)))
    return n

#############################################################################

# 다른 풀이 - quick sort


def quicksort(x):
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return   quicksort(more)+ equal +quicksort(less)

def solution(n):
    n = str(n)
    new = []
    for i in n :
        new.append(int(i))
    result = quicksort(new)

    answer = ''
    for i in result :
        answer += str(i)
    return int(answer)