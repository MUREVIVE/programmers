

def solution(arr):
    answer = []

    if len(arr) <= 1:
        answer.append(-1)
    else:
        # mylist.pop(mylist.index(min(mylist)))
        arr.remove(min(arr))
        answer = arr
    return answer

################################################################

# 다른 풀이

def solution(arr):
    answer = []

    if len(arr) <= 1:
        answer.append(-1)
    else:
        arr.pop(arr.index(min(arr)))
        answer = arr
    return answer