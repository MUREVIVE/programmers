#     for i in range(len(skill_trees)):
#         for j in range(len(skill_trees[i])):
#             if skill_trees[i][j] in skill[1:-1]:

#                 check = False
#                 break
#         if check == True:
#             answer += 1

def solution(skill, skill_trees):
    answer = 0
    # TypeError: object of type 'int' has no len()
    # for i in range(len(skill_trees)):
    for i in skill_trees:
        lst = []
        check = True

        for j in range(len(i)):  # 스킬트리내 스킬들에 대해
            if i[j] in skill:  # 스킬트리내 스킬의 글자가 skill에 있다면
                lst.append(i[j])

        for k in range(len(lst)):
            # if i[k] != lst[k]: 비교 대상이 틀림
            if lst[k] != skill[k]:
                check = False
                break

        if check == True:
            answer += 1

    return answer

##################################################################################

# 10-31 review

# for i in range(skill_trees):
#         visit = [0 for i in range(skill)]
#         if skill[i] in (skill_trees) and visit[i] == 0:
#             visit[i] = True
def solution(skill, skill_trees):
    answer = 0
        
    for st in skill_trees:
        lst = []
        check = True
        
        for j in range(len(st)): 
            if st[j] in skill: # skill_trees중 하나의 문자열의 문자가 skill에 있다면 append
                lst.append(st[j])
            
        for k in range(len(lst)):
            if lst[k] != skill[k]: 
                check = False
                break
                
        if check == True:
            answer += 1
            
    return answer
