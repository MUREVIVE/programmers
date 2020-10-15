
# dfs 
def solution(numbers, target):
    answer = 0
    
    def dfs(sum, idx):
        # base case
        if idx == len(numbers): # numbers들을 다 체크한 경우
            if sum == target:
                nonlocal answer # nonlocal : dfs함수의 바깥쪽에 있는 지역 변수의 값을 변경
                answer += 1
        else:
            dfs(sum + numbers[idx], idx + 1)
            dfs(sum - numbers[idx], idx + 1)
    
    dfs(0, 0)
    return answer


#######################################################################

# bfs - deque에 익숙하지 않은듯.

from collections import deque

def solution(numbers, target):
    answer = 0
    # TypeError: 'type' object is not subscriptable
    # Q = deque[(0, 0)]
    Q = deque([(0, 0)])
    
    while Q:
        sum, idx = Q.popleft()
        
        if idx == len(numbers):
            if sum == target:
                answer += 1
        else:
            Q.append((sum + numbers[idx], idx + 1))    
            Q.append((sum - numbers[idx], idx + 1))    
            
    return answer
