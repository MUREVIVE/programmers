
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

from collections import deque

def solution(prices):
    answer = []
    # print(prices) # [1, 2, 3, 2, 3]
    prices = deque(prices)
    # print(prices) # deque([1, 2, 3, 2, 3])
    
    while prices:
        c = prices.popleft() 
        # print(c) # 1 // 2 // 3 // 2 // 3
        count = 0
        
        for i in prices:
            count += 1
            if c > i:    
                break
    
        answer.append(count)
        
    return answer

# 시행착오
# answer = [(p, i) for i, p in enumerate(prices)] 이건 굳이 이렇게 안해도 되겠다.
    
    # for i, p in enumerate(prices):
    #     # print(prices[i+1:])
    #     if p <= min(prices[i+1:]):
    #         answer.append(len(prices) - 1 - i)
    #     else:
    #         answer.append(prices.index(i+1) - i - 1)

## 시간 초과(enumerate 때문에)
# def solution(prices): 
#     answer = []
    
#     for i, p in enumerate(prices):
#         count = 0
#         pos = i
        
#         while pos < len(prices) and p <= prices[pos]:
#             pos += 1
#             if pos < len(prices):
#                 count += 1
        
#         answer.append(count)
#     return answer
