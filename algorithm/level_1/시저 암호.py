# if 97 <= ord(s[i]) <= 122 or 65 <= ord(s[i]) <= 90:
# ord(s[i]) = ord(s[i] + n)
def solution(s, n):
    answer = []

    for i in range(len(s)):
        if s[i].isalpha():  # 알파벳 여부 확인
            if 65 <= ord(s[i]) <= 90:
                if ord(s[i]) + n > 90:  # 'z' 를 넘어가게 될 경우
                    answer.append(chr(ord(s[i]) - 26 + n))
                else:
                    answer.append(chr(ord(s[i]) + n))

            else:
                if ord(s[i]) + n > 122:  # 'Z'를 넘어가게 될 경우
                    answer.append(chr(ord(s[i]) - 26 + n))
                else:
                    answer.append(chr(ord(s[i]) + n))

        else:  # 알파벳이 아니라면
            answer.append(' ')

    # ''.join(list) : 리스트에서 문자열으로
    return ''.join(answer)


#################################################################

# 다른 풀이

def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)