-- SET @hour = -1;

-- SELECT @hour := @hour + 1 AS HOUR,
-- (
--     SELECT COUNT(DATETIME)
--     FROM ANIMAL_OUTS B
--     WHERE HOUR(DATETIME) = @hour
-- ) AS COUNT
-- FROM ANIMAL_OUTS A
-- WHERE @hour < 23