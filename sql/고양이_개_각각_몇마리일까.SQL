

"""

동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 

이때 고양이를 개보다 먼저 조회해주세요.

"""

-- 코드를 입력하세요
#SELECT * FROM ANIMAL_INS

SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) AS count FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE # GROUP BY에 대해 생각 못했음.
ORDER BY ANIMAL_TYPE ASC;


#만약 column 종류가 개, 고양이 말고도 더 있을 경우에 -> HAVING 이용

SELECT animal_type, COUNT(animal_id) AS count FROM animal_ins
GROUP BY animal_type
HAVING animal_type = 'cat' or animal_type = 'dog'
ORDER BY animal_type ASC ;

