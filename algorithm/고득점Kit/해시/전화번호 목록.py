

# zip / startswith 이용
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

#################################################################

# hash를 이용한 풀이 /
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

#################################################################

# 그냥 전형적 브루트포스 풀이 / 다만 효율성이 아쉽다.
def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))

    """
    for i in range(len(phone_book)):
        j = 0

        if j in phone_book:
            if i == j:
                pass
            else:
                answer = False
        j += 1
    """

    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            # print(phone_book[j][0:len(phone_book[i])])

            if phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                return False

    return answer
#################################################################

# 해시 풀이에 대한 print 결과 확인하기
phone_book = ["119", "97674223", "1195524421"]

answer = True

hash_map = {}
for phone_number in phone_book:
    hash_map[phone_number] = 1
for phone_number in phone_book:
    temp = ""

    for number in phone_number:
        temp += number

        if temp in hash_map and temp != phone_number:
            answer = False

# 아 이런식으로.
# {'119': 1, '97674223': 1, '1195524421': 1}
print(hash_map)