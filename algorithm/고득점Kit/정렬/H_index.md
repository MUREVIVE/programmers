
```py
# 문제를 제대로 이해하지 못하고 적은 풀이
def solution(citations):
    answer = 0
    # num = 0
    # for i in range(len(citations)):
    #     num += citations[i]
    # num //= 5
    
    citations.sort()
    result = -1
    i = 0
    
    while i != len(citations):
        num = citations[i]
        Max_count = 0    
        Min_count = 0
        
        for j in range(0, len(citations)):
            if num == citations[j]:
                continue
            elif num > citations[j]:
                Max_count += 1
            else:
                Min_count += 1
        
        if Max_count >= num and Min_count <= num:
            result = max(result, num)
            
        i += 1
        
    return result
```

<br>

```py
# 문제가 잘 이해가 안됐다. 다른 풀이 가져온 것.
def solution(citations):
    answer = 0
    
    # 편 수 의 최댓값을 구해야 한다. (문제를 제대로 이해해야 함.)
    # 그러므로 len(citations)에 대해 -1씩 감소하는 방식으로 구한다.
    citations.sort()
    n = len(citations)
    
    while True:
        for i, value in enumerate(citations):
            # value가 n번 이상 인용됐고,
            if value >= n and len(citations[i:]) >= n:
                return n
            else:
                n -= 1
                
        break
    return answer
```

<br>

```py
# 다른 풀이
def solution(citations):
  sorted_citations = sorted(citations, reverse=True)
  for i in range(len(sorted_citations)):
    if sorted_citations[i] <= i: 
      return i
  return len(sorted_citations)
```

<br>

기본적인 내용은 쉬웠지만 문제를 이해하기가 어려운 문제였습니다. 그리고 2가지 경우를 생각하기가 어려웠습니다.

* [22, 42]인 경우 결과값이 2인데 이 케이스
* [0] * 100000000000000000000으로 같은 값으로 반복되는 경우

풀이는 min값부터 max값 까지 모두 순회하면서 H-Index를 찾고 최댓값을 찾는 방법입니다.

```py
def solution(citations):
    # [22, 42] , 2인 경우 
    if min(citations) >= len(citations): answer = len(citations)
    else: answer = 0
    citations = sorted(citations)

    # [0] * 10000000 인 경우 
    for i in range(min(citations), max(citations) + 1):
        left = 0
        right = 0
        for j in citations:
            if j <= i: left += 1
            if j >= i: right += 1
        if (left <= i) & (right >= i):
            answer = max(answer, i)
    return answer
```
