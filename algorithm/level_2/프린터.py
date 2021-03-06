
def solution(priorities, location):
    answer = 0
    
    array1 = [c for c in range(len(priorities))]
    # array2 = array1.copy() # array1은 priorities배열이라고 착각해서;;
    array2 = priorities.copy()
    i = 0
    print(array1, array2)
    while True:
        if array2[i] < max(array2[i+1:]):
            # pop : 젤 앞의 원소 / append : 젤 뒤에다가
            array1.append(array1.pop(i)) # [0, 1, 2, 3] -> [1, 2, 3, 0]
            array2.append(array2.pop(i))
            print(array1, array2)
        else:
            i += 1
        
        if array2 == sorted(array2, reverse=True): # 내림차순 정렬 형태가 된다면
            break
        
    return array1.index(location) + 1




###################################################################################

# 다른 풀이
## - deque 사용법 - popleft(), append
## - deque 내에서 enumerate 사용법 
from collections import deque
def solution(priorities, location):
    answer = 0
    
    # enumerate : 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환
    d = deque([(value,i) for i,value in enumerate(priorities)])
    while len(d):
        # d의 맨 앞 제거
        item = d.popleft() # ex : (2, 0) / (1, 1) / (3, 2) / (2, 3) -> (1, 1) / (3, 2) / (2, 3)
        # print(max(d)[0]) 
        print(d)
        if len(d) != 0 and max(d)[0] > item[0]:
            # d의 맨 뒤에 추가
            d.append(item) # ex : (1, 1) / (3, 2) / (2, 3) -> (1, 1) / (3, 2) / (2, 3) / (2, 0)
        else:
            answer += 1
            if item[1] == location:
                break
                
    return answer


