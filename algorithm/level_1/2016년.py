
# 내가 처음 푼 풀이 방식

def solution(a, b):
    answer = ''
    # 1월 1일 금요일부터 계산하는 것이므로 1월은 30일로 설정 - 이 설정은 틀린것.
    Months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    day_count = b

    for i in range(1, a):
        day_count += Months[i - 1]

    day_count %= 7
    answer = days[day_count]
    return answer

###########################################################################
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7] # 오. sum 함수를 이용했네. 깔끔하다 이거



###########################################################################

# dictionary 활용은 생각 못했네

def getDayName(a,b):
    day_name = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month_dict = {
        "1":31,
        "2":29,
        "3":31,
        "4":30,
        "5":31,
        "6":30,
        "7":31,
        "8":31,
        "9":30,
        "10":31,
        "11":30,
        "12":31
    }
    days = 0
    for i in range(1, a):
        # KeyError: 1 / 이 경우 index type이 잘못 됐음.
        # days += month_dict[i]
        days += month_dict[str(i)]
    days += b
    index = days % 7

    return day_name[index]
