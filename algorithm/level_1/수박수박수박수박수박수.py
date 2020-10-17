

# 처음 내가 푼 풀이
def solution(n):
    answer = ''

    for i in range(1, n + 1):
        if i % 2 == 0:
            answer += '박'
        else:
            answer += '수'
    return answer

######################################################

# 다른 풀이 - 와 str type answer에 대해 slice로 할 수 있다는걸 생각 못했네

def solution(n):
    answer = '수박' * n
    return answer[:n]