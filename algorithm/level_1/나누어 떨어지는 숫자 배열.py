


def solution(arr, divisor):
    answer = []

    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])

    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()

    return answer


#####################################################################

# 다른 풀이

def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    arr.sort()
    return arr if len(arr) != 0 else [-1]