## Формирование табеля
Вам дана таблица problem, в которой хранится:

* id - id задачи
* name - название задачи
* solution - решение задачи
* другие данные

Вам нужно написать запрос, который создаст заготовку табеля в формате «все месяцы - все задачи» (для каждого месяца
вывести каждую задачу).

Выведите:

* номер месяца
* id задачи

Пример:
```
code	problem
1	1
1	2
1	3
...	...
2	1
2	2
2	3
...	...
```

## Решение
```sql
SELECT
    months.month_code,
    problems.id
FROM
    (SELECT generate_series(1, 12) AS month_code) AS months
CROSS JOIN
    (SELECT DISTINCT id FROM problem) AS problems
ORDER BY
    months.month_code,
    problems.id;
```
- `generate_series(1, 12)` - генерирует последовательность чисел
- `CROSS JOIN` - создаёт все возможные комбинации между двумя наборами данных и соединяет каждый месяц с каждым id из problem

## Поиск вредоносного кода
Вам дана таблица CodeSubmit, в которой хранится информация:

user_id - какой пользователь
code - какой код отправил на проверку
created_at - в какое время это происходило
language_id - какой язык использовали
Иногда пользователи платформы любят «шалить» и пытаются сломать систему, отправив на проверку вредоносный код. Вам
нужно найти случаи таких атак:

Какой код написали
Какой язык использовали
Вывести нужно следующие нарушения:

в задачах, которые решались на SQL, есть команды drop, delete, truncate, insert, create. После них всегда идет пробел и минимум 1 символ. (DELETE FROM ClientBalance WHERE … FROM …)
в задачах, которые решались на Python, есть команды exec, eval. Будем считать, что после них может идти любой пробельный символ, а затем обязательно открывающаяся скобка и минимум 1 символ. Что перед этим и после - не так важно.

Примечание: Будьте осторожны с регистром букв.

Пример вредоносного кода на SQL:

`DROP users`
Пример вредоносного кода на Python:

`assert eval("os.system('rm -rf /')")`
Дополнительно тему поиска по шаблону можно изучить здесь: https://postgrespro.ru/docs/postgresql/9.6/functions-matching.

### Решение
```sql
SELECT code, 
       CASE 
           WHEN language_id = 1 THEN 'SQL'
           WHEN language_id = 2 THEN 'Python'
       END as language_id
FROM CodeSubmit
WHERE 
    (language_id = 1 AND 
     UPPER(code) LIKE '%DROP %' OR 
     UPPER(code) LIKE '%DELETE %' OR 
     UPPER(code) LIKE '%TRUNCATE %' OR 
     UPPER(code) LIKE '%INSERT %' OR 
     UPPER(code) LIKE '%CREATE %'
    )
    OR 
    (language_id = 2 AND 
     UPPER(code) LIKE '%EXEC(%' OR 
     UPPER(code) LIKE '%EVAL(%'
    );
```

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
