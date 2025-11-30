-- second_tableda score ve namei gosteren kod
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name !='' ORDER BY score DESC;
