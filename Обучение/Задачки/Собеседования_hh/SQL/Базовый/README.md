# Теория
# Вопросы и Ответы

В этом разделе представлены 10 изображений с вопросами. Нажмите на ответы, чтобы увидеть ответы и объяснения.


1. ![Вопрос 1](img/1_question.jpg)
   <details>
   <summary>Ответ</summary>
   DROP TABLE (используется для удаления таблицы)
   </details>
---
2. ![Вопрос 2](img/2_question.jpg)
   <details>
   <summary>Ответ</summary>
   ALTER TABLE (используется для изменения структуры таблицы)
   
   DROP COLUMN (используется для удаления столбца)
   
   - ALTER TABLE Clients DROP COLUMN old_email;
   </details>
---
3. ![Вопрос 3](img/3_question.jpg)
   <details>
   <summary>Ответ</summary>
   
   - SELECT first_name, last_name FROM Employees WHERE job_title = 'Analyst' 
   
   </details>
---
4. ![Вопрос 4](img/4_question.jpg)
   <details>
   <summary>Ответ</summary>
   
   - Максимальную зарплату
   - Минимальную зарплату
   - Общее кол-во сотрудников (COUNT(*)) в таблице Employees
   
   </details>
---
5. ![Вопрос 5](img/5_question.jpg)
   <details>
   <summary>Ответ</summary>
   Уникальный id посетителя сайта
   
   Primary key или UNIQUE NOT NULL
   </details>
---
6. ![Вопрос 6](img/6_question.jpg)
   <details>
   <summary>Ответ</summary>
   
    Типы соединений существующие только в SQL:
   * INNER JOIN - возвращает только совпадающие записи из двух таблиц (Внутреннее)
   * OUTER JOIN - возвращает все записи из двух таблиц (Внешнее)
   * LEFT OUTER JOIN - возвращает все записи из левой таблицы и соответствующие записи из правой таблицы (Левый)
   * RIGHT OUTER JOIN - возвращает все записи из правой таблицы и соответствующие записи из левой таблицы (Правый)

   </details>
---
7. ![Вопрос 7](img/7_question.jpg)
   <details>
   <summary>Ответ</summary>
   
   (DESC тут играет роль сортировки по убыванию, то есть от большей к меньшей и от последней к первой)
   * SELECT * FROM Sales ORDER BY date DESC, sale_amount DESC;
   </details>
---
8. ![Вопрос 8](img/8_question.jpg)
   <details>
   <summary>Ответ</summary>
    
   Правильный ответ:
   
   * WHERE сначала выбирает строки, затем группирует их и вычисляет агрегатные функции, а HAVING — сначала группирует строки, вычисляет агрегатные функции и только потом выбирает строки

   WHERE используется для фильтрации строк до группировки данных. HAVING применяется для фильтрации после группировки, чаще всего с агрегатными функциями.
   
   </details>
---
9. ![Вопрос 9](img/9_question.jpg)
   <details>
   <summary>Ответ</summary>
   
   Чтобы найти регионы со средним рейтингом городов выше 3.0, используйте следующий SQL-запрос:
   
   - SELECT region_id, rating
   - FROM Cities
   - GROUP BY region_id
   - HAVING AVG(rating) > 3.0;

   </details>
---

10. ![Вопрос 10](img/10_question.jpg)
   <details>
   <summary>Ответ</summary>

   Первые 10 записей из таблицы Food, отсортированных по столбцу price в порядке убывания
   
   </details>

---