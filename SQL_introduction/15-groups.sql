-- Eyni socre sahib olanlari tapan kod
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
