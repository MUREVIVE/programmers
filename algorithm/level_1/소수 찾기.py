
# 효율성에서 탈락

def solution(n):
    answer = 0
    s = 0
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                s += 1
        if s == 0:
            answer += 1
        s = 0

    return answer

#############################################################

# 다른 풀이 - 에라토스테네스의 체

def solution(n):
    answer = 0

    check = [True] * (n + 1)  # 1 ~ n에 대해 소수라고 간주하고 시작
    m = int(n ** 0.5)  # n의 최대 약수가 sqrt(n)이하이므로

    for i in range(2, m + 1):
        if check[i] == True:
            # 소수의 배수들은 소수가 아니므로 False 처리.
            for j in range(i + i, n + 1, i):
                check[j] = False

    for i in range(2, n + 1):
        if check[i] == True:
            answer += 1

    return answer