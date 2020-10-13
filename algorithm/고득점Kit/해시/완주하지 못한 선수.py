

# 효율성이 안좋음. list.remove()의 time complexity : O(N)
def solution(participant, completion):
    for ppl in completion:
        if ppl in participant:
            participant.remove(ppl)
        else:
            pass
    return participant[0]



# sort() 2번을 한 후 participant list의 길이가 completion보다 1 긴것을 이용.
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[i+1]



# collection의 Counter 기법 이용
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer)[0]



# 정수형의 hash()값을 이용한 덧셈과 뺄셈.
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer