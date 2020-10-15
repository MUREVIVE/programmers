def solution(numbers):
    answer = []
    # 서로 다른 인덱스에 있는 두개의 수 뽑아 더한 경우의 수
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    # set 자료형 사용하여 중복된 수 제거
    answer = list(set(answer))
    # 오름차순 정렬
    answer.sort()

    return answer

########################################################

from itertools import combinations

def solution(numbers):
    answer = []
    # itertools의 combinations 이용, numbers 리스트에 대해 2개 뽑는다.
    lst = list(combinations(numbers, 2))

    for l in lst:
        answer.append(l[0] + l[1])

    # set 자료형 사용하여 중복된 수 제거
    answer = list(set(answer))
    # 오름차순 정렬
    answer.sort()

    return answer