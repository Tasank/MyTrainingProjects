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
