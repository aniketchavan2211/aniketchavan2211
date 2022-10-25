SELECT s.name, m.carbs, m.protein, m.fat
FROM snack AS s
LEFT JOIN macros AS m
ON s.id = m.id;
