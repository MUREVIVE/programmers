
def solution(s):
    answer = ''
    answer = sorted(s, reverse = True)

    # return str(answer) 이렇게 하면 안됨
    return ''.join(answer)

############################################

# 다른 풀이
def solution(s):
    s = list(s)
    s.sort(reverse = True)
    answer = ""
    for i in s:
        answer = answer + i
    return answer