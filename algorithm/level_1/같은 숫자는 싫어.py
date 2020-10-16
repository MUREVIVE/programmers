

# 인형뽑기 (카카오 문제) 풀이를 응용하여 해결.
def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(arr)):
        answer.append(arr[i])

        if len(answer) > 1:
            if answer[-1] == answer[-2]:
                # answer.pop(-1)
                answer.pop(-1)


    return answer

##################################################################

# a[-1:]가 인상적인 코드.
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a


###################################################################

def solution(s):
    # slicing은 index값이 범위 초과해도 오류 안뜬다.
    return [s[i] for i in range(len(s)) if [s[i]] != s[i+1:i+2]]