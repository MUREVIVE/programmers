

/*

동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디와 이름, 성별 및 중성화 여부를 조회하는 SQL 문을 작성해주세요.

*/

-- 내 풀이 방식
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS
-- WHERE NAME IS 'Lucy' OR NAME IS 'Ella' OR NAME IS 'Pickle' OR NAME IS 'Rogan' OR NAME IS 'Sabrina' -- OR NAME IS 'Mitty'
-- WHERE NAME is 'Lucy' NAME IS라고 사용하면 안되더라

WHERE NAME LIKE 'Lucy' OR NAME LIKE 'Ella' OR NAME LIKE 'Pickle' OR NAME LIKE 'Rogan' OR NAME LIKE 'Sabrina' OR NAME LIKE 'Mitty'
ORDER BY ANIMAL_ID;




-- 다른 풀이 방식 1 : NAME에 대하여 IN을 사용 

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')
ORDER BY ANIMAL_ID ASC;

