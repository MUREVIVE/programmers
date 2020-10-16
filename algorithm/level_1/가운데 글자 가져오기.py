def solution(s):
    answer = ''

    if len(s) % 2 == 0:
        a = (len(s) // 2) - 1
        return s[a: a + 2]
    else:
        a = len(s) // 2
        return s[a: a + 1]