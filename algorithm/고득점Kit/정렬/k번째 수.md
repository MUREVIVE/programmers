
```py
def solution(array, commands):
    answer = []
    """
    temp_list = []
    for i in range(len(commands)):
        for j in range(len(commands)):
            temp_list = array[commands[i][j]]
            print(temp_list)
    """
    # for문을 이렇게 사용하면 commands 2차원 배열에 더 수월하게 접근 가능
    # 이걸 제대로 활용 못했다.
    for command in commands:
        new_array = array[command[0] - 1:command[1]]
        new_array.sort()
        answer.append(new_array[command[2] - 1])

    return answer
```

```py
다시 푼 풀이
def solution(array, commands):
    answer = []
    
    # 설계는 제대로 됐으나, 구현을 좀 더 신경써야함.
    for l in commands:
        # 세 개의 변수에 대해 어떻게 처리해야 되나 고민했음. -> 아래 풀이에 나와있다.
        new_array = array[l[0] - 1 : l[1]]
        new_array.sort()
        print(new_array)
        # answer.append(new_array[2])
        answer.append(new_array[l[2] - 1])
            
    return answer
```

```py
# 다른 풀이
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
        # 일차원 배열에 대해 slicing한 다음 index 잡는 것도 가능하네
        print(list(sorted(array[i-1:j]))[k-1])
    return answer
```
