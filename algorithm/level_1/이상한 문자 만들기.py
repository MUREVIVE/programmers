# TypeError: sequence item 0: expected str instance, bool found
# isupper(), islower() / upper(), lower() 차이 구분

# 각 단어의 짝수번째, 홀수번째를 찾는 것임.
# for i in range(len(s)):
#     if s[i].isalpha(): # 알파벳이라면
#         if i % 2 == 0:
#             # s[i] = s[i].isupper()
#             # print(s[i].upper())
#             answer.append(s[i].upper())
#         else:
#             # s[i] = s[i].islower()
#             answer.append(s[i].lower())
#     else:
#         answer.append(' ')






def solution(s):
    answer = []
    # for i in range(len(s)):
    #     if s[i].isalpha():
    #         if i % 2 == 0:
    #             print(s[i].isupper()) # -> s[i].isupper() 이게 True, False를 반환하는 것이었음.

    s = s.split(" ")  # 단어 별로 분리
    print(s)
    for i in range(len(s)):
        for j in range(len(s[i])):  # 각 단어에 대해
            if j % 2 == 0:
                # s[i] = s[i].isupper()
                # print(s[i].upper())
                answer.append(s[i][j].upper())
            else:
                # s[i] = s[i].islower()
                answer.append(s[i][j].lower())

        answer.append(' ')

    # return ''.join(answer) -> 문장 뒤에 공백 한칸이 남음.
    return ''.join(answer[:-1])  # 위 문제로 인해 [:-1]을 해준 것.