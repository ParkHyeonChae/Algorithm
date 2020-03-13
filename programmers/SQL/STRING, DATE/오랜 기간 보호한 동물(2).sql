SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS A
JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.ANIMAL_ID IS NOT NULL
ORDER BY A.DATETIME - B.DATETIME
-- LIMIT 2