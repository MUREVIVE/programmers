

# 처음 내가 푼 풀이
def solution(s):
    answer = int(s)
    return answer

#####################################################

# 다른 풀이 - 와 대박이다 ㄹㅇ

def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result