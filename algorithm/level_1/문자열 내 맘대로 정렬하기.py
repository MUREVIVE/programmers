


# for i in answer:
#     if answer.count(i[n]) >= 2:
#         answer.sort()
def solution(strings, n):
    answer = []

    # 첫번째 기준으로 정렬이 되지 않으면, 두번째 기준을 적용하여 정렬한다
    answer = sorted(strings, key=lambda x: (x[n:n + 1], x))

    print(answer)
    return answer



