
# 내 풀이 / 이중 for문 / 의외인게 효율성 테스트를 통과했더라
def solution(prices):
    answer = []

    for i in range(len(prices)):
        check = True
        count = 0
        for j in range(i + 1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                answer.append(count)
                check = False
                break

        if check == True:
            answer.append(count)
    return answer

########################################################

# deque를 이용한 풀이

from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer