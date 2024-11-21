## Задание №1
Вам дана таблица users с полями:
username
email

Вам нужно проверить гипотезу, что пользователи часто делают username на платформе таким же, как левая часть почты (до символа @).

Напишите запрос, который выведет:

1. username
2. email
3. левую часть email
4. `isEqual` - столбец `True`/`False`, который проверяет гипотезу

Примечание: Обратите внимание, что myUSERname и myusername для почтовых сервисов — одно и
то же, т.к. они не чувствительны к регистру.
## Решение
```sql
SELECT
    username,
    email,
    SUBSTRING(email, 1, POSITION('@' IN email) - 1) AS left_part,
    CASE
        WHEN LOWER(username) = SUBSTRING(LOWER(email), 1, POSITION('@' IN email) - 1) THEN TRUE
        ELSE FALSE
    END AS isequal
FROM
    users;
```
___
## Задание №2
Процент скидок от суммы продаж

Вы работаете с базой данных apteka. Обязательно указывайте имя БД при указании таблиц. Apteka содержит следующие таблицы:

Bonuscheques

* дата и время совершения транзакции - datetime

* название аптеки - shop

* номер бонусной карты - card

* количество начисленных бонусов - bonus_earned

* количество потраченных бонусов - bonus_spent

* сумма чека - summ

* сумма чека с учетом скидок и списаний бонусов - summ_with_disc

* номер документа - doc_id

Shops

* идентификатор аптеки - id

* название аптеки - name

 

Задача

Чтобы понимать, что бонусная система не работает нам во вред, определите процент, который сумма скидок составляет от общей суммы продаж в каждой аптеке.

Столбцы в результате

shop - Аптека в формате "Аптека 7"
pct - процент, округленный до двух знаков после запятой

## Решение
```sql
SELECT 
    r.shop,
    ROUND(r.all_summ_skid / r.all_summ * 100, 2) AS pct
FROM (
    SELECT 
        b.shop,
        SUM(b.summ - b.summ_with_disc) * 1.0 AS all_summ_skid,
        SUM(b.summ) * 1.0 AS all_summ
    FROM 
        apteka.Bonuscheques b
    GROUP BY 
        b.shop
) r
```
## Решение №2 
#### *Это решение без вложенного запроса, меньше, но чуть с более сложной формулой*
Умножение на 1.0 нужно для приведения к типу float, так как в обратом случае вычисления будут не точными и не пройдёт тесты 1 и 2
```sql
SELECT
    b.shop,
    ROUND(SUM((b.summ * 1.0) - (b.summ_with_disc * 1.0)) / SUM(b.summ) * 100, 2) AS pct
FROM apteta.Bonuscheques b
GROUP BY b.shop
```

---

## Задача №3

Клиенты с количеством заказов выше среднего
Вы работаете с базой данных apteka. Обязательно указывайте имя БД при указании таблиц. Apteka содержит следующие таблицы:

Bonuscheques

* дата и время совершения транзакции - datetime

* название аптеки - shop

* номер бонусной карты - card

* количество начисленных бонусов - bonus_earned

* количество потраченных бонусов - bonus_spent

* сумма чека - summ

* сумма чека с учетом скидок и списаний бонусов - summ_with_disc

* номер документа - doc_id

 

Задача

Напишите запрос, который выводит карты клиентов, участвующих в бонусной программе и их количество заказов, при условии, что количество их заказов превышает среднее значение по всем пользователям бонусной программы.

Столбцы в результате

card - номер бонусной карты
order_count - количество заказов по этой карте

## Решение
```sql
WITH order_counts AS (
  SELECT card, COUNT(DISTINCT doc_id) AS order_count
  FROM apteka.Bonuscheques
  WHERE card IS NOT NULL
  GROUP BY card
)
SELECT card, order_count
FROM order_counts
WHERE order_count > (SELECT AVG(order_count) FROM order_counts)
ORDER BY order_count DESC;
```
DESC сортирует результат по убыванию, можно его убрать (ASC), это не влияет на решение

