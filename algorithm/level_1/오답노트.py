# 2016.py
## dictionary 풀이 관련 KeyError / Key는 str type이어야 한다.
month_dict = { "1":31, "2":29, "3":31, "4":30, "5":31, "6":30, "7":31, "8":31, "9":30,
        "10":31, "11":30, "12":31 }
    days = 0
    for i in range(1, a):
        # KeyError: 1 / 이 경우 index type이 잘못 됐음.
        # days += month_dict[i]
