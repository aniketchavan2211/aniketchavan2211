SELECT user.name, user.address, po.pizza
FROM pizza_order AS po
INNER JOIN user
ON po.user = user.id;
