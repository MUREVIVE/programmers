def solution(n):
    answer = -1

    m = int(n ** 0.5)
    print(m)
    for i in range(1, m + 1):
        # if n // i == i: # 이렇게 했을 때 테스트 케이스 18개 중 1개가 탈락됐다. 그게 어떤건지 모르겠음.
        if i ** 2 == n:
            answer = (i + 1) ** 2

    return answer