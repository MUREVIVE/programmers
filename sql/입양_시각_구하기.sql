

/*
ANIMAL_OUTS 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. 

ANIMAL_OUTS 테이블 구조는 다음과 같으며, 

ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다.

NAME	TYPE	NULLABLE
ANIMAL_ID	VARCHAR(N)	FALSE
ANIMAL_TYPE	VARCHAR(N)	FALSE
DATETIME	DATETIME	FALSE
NAME	VARCHAR(N)	TRUE
SEX_UPON_OUTCOME	VARCHAR(N)	FALSE

보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 

이때 결과는 시간대 순으로 정렬해야 합니다.

*/



-- 내 풀이방식

-- SELECT DATEPART(HOUR, DATETIME) FROM ANIMAL_OUTS / DATEPART는 여기서 왜 안되는지 잘 모르겠네.

-- SELECT EXTRACT(HOUR FROM DATETIME) FROM ANIMAL_OUTS

SELECT 
    EXTRACT(HOUR FROM DATETIME) AS HOUR, 
    COUNT(EXTRACT(HOUR FROM DATETIME)) AS COUNT_HOUR 
FROM ANIMAL_OUTS
GROUP BY HOUR -- GROUP BY를 사용해줘야 HOUR에 대한 ROW들이 나열된다.
HAVING HOUR >= 9 AND HOUR <= 19
ORDER BY HOUR ASC;



-- 다른 풀이방식 1 : HOUR, COUNT(*) 이용

SELECT  hour(datetime) hour,count(*)
from animal_outs
group by hour
having hour>=9 and hour<=19
order by hour asc


-- 다른 풀이방식 2 : ANIMAL_OUTS에 ALIASING을 이용.

SELECT HOUR(DATETIME) as 'HOUR', COUNT(a.ANIMAL_ID) as 'COUNT' FROM ANIMAL_OUTS as a
GROUP BY HOUR(DATETIME) HAVING HOUR BETWEEN 9 AND 19 
ORDER BY HOUR


-- 다른 풀이방식 3 : BETWEEN A AND B 이용

SELECT hour(datetime) as hour,count(datetime) as count
FROM ANIMAL_OUTS
where hour(datetime) between 9 and 19
group by hour
order by hour;


-- 다른 풀이방식 4 : SUBQUERY, date_format 이용


select hour, count(datetime) as cnt
from (select date_format(datetime,'%H') as hour, datetime
        from animal_outs
        ) as temp
where hour between 9 and 19
group by hour
order by hour


-- 다른 풀이방식 5 : SUBSTRING 이용

SELECT SUBSTRING(DATETIME, 12, 2) AS HOUR,
COUNT(DATETIME) AS HOURCOUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR
BETWEEN 9 AND 19
ORDER BY HOUR;