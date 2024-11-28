
## Сглаживание DAU

Вам дана таблица UserEntry в которой фиксируется первый заход пользователя на платформу за текущий день.

Таблица UserEntry содержит:

id - уникальный id каждого входа в формате int.
entry_at - время входа пользователя в формате timestamp.
page_id - id страницы, на которую зашел пользователь. Формат int.
user_id - id пользователя в формате int.
Ваша задача:

Посчитать DAU за каждый день 2022 года на основании заходов пользователей на платформу (почитать про DAU можно здесь https://www.unisender.com/ru/glossary/mau-dau-ili-osnovnye-metriki-mobilnyh-prilozhenij/)
Сделать столбец, где значения DAU будут сглажены с помощью метода скользящего среднего (https://antonz.ru/window-rolling/#rolling-avg)
Сделать столбец, где значения DAU будут сглажены с помощью метода медианного сглаживания (https://studfile.net/preview/9931880/page:5/)
В результате должны получиться столбцы:

ymd - столбец с днем (в текстовом формате)
cnt - значение DAU
sliding_average - сглаживание средним
sliding_median - сглаживание медианой
Примечание: При сглаживании берем все значения DAU за предыдущие даты. Текущую дату также включаем.

Примечание: При расчете медианы рассчитанное значение не обязано входить в исходный набор данных.

```sql
WITH DailyActiveUsers AS (
    SELECT
        to_char(entry_at, 'YYYY-MM-DD') AS ymd,
        COUNT(DISTINCT user_id) AS cnt
    FROM
        UserEntry
    WHERE
        entry_at >= '2022-01-01' AND entry_at < '2023-01-01'
    GROUP BY
        to_char(entry_at, 'YYYY-MM-DD')
),
SlidingAverages AS (
    SELECT
        ymd,
        cnt,
        AVG(cnt) OVER (ORDER BY ymd ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS sliding_average
    FROM
        DailyActiveUsers
),
SlidingMedians AS (
    SELECT
        ymd,
        cnt,
        sliding_average,
        (SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY cnt) 
         FROM (SELECT cnt 
               FROM SlidingAverages 
               WHERE ymd <= sa.ymd) AS subquery) AS sliding_median
    FROM
        SlidingAverages sa
)
SELECT
    ymd,
    cnt,
    sliding_average,
    sliding_median
FROM
    SlidingMedians
ORDER BY
    ymd;
```

## Изменение пикового значения
На основании таблицы users, давайте посмотрим - как с каждым днем менялось пиковое значение количества регистраций за один день.

Давайте возьмем период с 01.01.2022 и последующие 110 дней. А потом найдем:

dt - какая дата
cnt - сколько людей зарегистрировалось в этот день
max_cnt - нарастающее значение максимума регистраций
diff - разница между текущим значением и актуальным максимумом
Примечание: Естественно, дни без регистраций мы тоже учитываем.

```sql
WITH daily_registrations AS (
    SELECT 
        generated_dates.date_time AS dt,
        COUNT(users.username) AS cnt
    FROM generate_series(
        '2022-01-01'::timestamp,
        '2022-01-01'::timestamp + interval '110 days',
        interval '1 day'
    ) AS generated_dates(date_time)
    LEFT JOIN users 
        ON generated_dates.date_time = users.date_joined::date::timestamp
    GROUP BY generated_dates.date_time
),
running_maximum AS (
    SELECT 
        dt,
        cnt,
        MAX(cnt) OVER (ORDER BY dt) AS max_cnt
    FROM daily_registrations
)
SELECT 
    dt,
    cnt,
    max_cnt,
    cnt - max_cnt AS diff
FROM running_maximum;
```
### Уменьшенный запрос (Кому удобнее)
```
WITH data AS (select g.dt, count(u.username) AS cnt
FROM generate_series('2022-01-01'::timestamp , '2022-01-01'::timestamp + interval '110 days', interval '1 day') g(dt)
LEFT JOIN users u
ON g.dt = u.date_joined::date::timestamp
GROUP BY g.dt),
max_cnt AS (select dt, cnt, max(cnt) OVER (order by dt) AS max_cnt
FROM data)
SELECT dt, cnt, max_cnt, cnt-max_cnt AS diff
FROM max_cnt
```