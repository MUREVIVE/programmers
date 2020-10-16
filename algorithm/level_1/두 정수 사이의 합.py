
def solution(a, b):
    answer = 0

    if a < b:
        for i in range(a, b+ 1):
            answer += i

    elif a >= b:
        for i in range(a, b - 1, -1):
            answer += i

    return answer


######################################################

# 다른풀이

def adder(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a

    return sum(range(a,b+1))