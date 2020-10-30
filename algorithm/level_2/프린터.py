def solution(priorities, location):
    answer = 0
    
    array1 = [c for c in range(len(priorities))]
    array2 = priorities.copy()
    
    i = 0
    while True:
        if array2[i] < max(array2[i+1:]): # 더 중요도 높은 문서가 존재한다면
            array1.append(array1.pop(i))
            array2.append(array2.pop(i))
        else:
            i += 1
        
        if array2 == sorted(array2, reverse=True):
            break
        
    return array1.index(location) + 1


###################################################################################

# 다른 풀이

def solution(priorities, location):
  answer = 0
  from collections import deque

  d = deque([(v,i) for i,v in enumerate(priorities)])

  while len(d):
      item = d.popleft()
      if d and max(d)[0] > item[0]:
          d.append(item)
      else:
          answer += 1
          if item[1] == location:
              break
  return answer
