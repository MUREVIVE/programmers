
def solution(s):
    answer = True

    if not len(s) == 4 or len(s) == 6:
        return False

    # ord(문자) : 아스키코드 반환
    # chr(숫자) : 숫자에 맞는 아스키코드 반환
    for i in s:
        if 97 <= ord(i) <= 122 or 65 <= ord(i) <= 90:
            answer = False

    return answer


#####################################################

# 다른 풀이

# isalpha함수는 문자열이 문자인지 아닌지를 True,False로 리턴해주고,
# isdigit함수는 문자열이 숫자인지 아닌지를 True,False로 리턴해줍니다.
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)