

"""

입양 게시판에 동물 정보를 게시하려 합니다. 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 

이름이 없는 동물의 이름은 No name으로 표시해 주세요.

"""

-- 코드를 입력하세요
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') AS NAME, SEX_UPON_INTAKE FROM ANIMAL_INS;




#IF NAME IS NULL THEN "No name"
#ORDER BY ANIMAL_TYPE, NAME, SEX_UPON_INTAKE;