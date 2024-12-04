# Теория
# Вопросы и Ответы

В этом разделе представлены 9 изображений с вопросами. Нажмите на ответы, чтобы увидеть ответы и объяснения.


1. ![Вопрос 1](img/1_question.jpg)
   <details>
   <summary>Ответ</summary>
   json
   </details>
---
2. ![Вопрос 2](img/2_question.jpg)
   <details>
   <summary>Ответ</summary>
   integer check(age>0)
   </details>
---
3. ![Вопрос 3](img/3_question.jpg)
   <details>
   <summary>Ответ</summary>
   Подойдёт запрос: alter table some_table alter column id type bigserial
   Объяснение: alter table - изменение структуры таблицы, alter column - изменение структуры одного столбца
   </details>
---
4. ![Вопрос 4](img/4_question.jpg)
   <details>
   <summary>Ответ</summary>
   alter table person add column fullname text generated always as (first_name || ' ' || second_name) stored
   
   </details>
---
5. ![Вопрос 5](img/5_question.jpg)
   <details>
   <summary>Ответ</summary>
   Последовательность 'my_sequence'
   </details>
---
6. ![Вопрос 6](img/6_question.jpg)
   <details>
   <summary>Ответ</summary>
   limit и offset.
   Пагинация - это механизм, который используется для упрощения работы с большими данными. Суть которого в том, что мы делаем выборку не из всех данных, а из определенного количества.
   limit - в пагинации выполняет роль поиска нескольких элементов в таблице.
   offset - в пагинации выполняет роль сдвига на определенное количество элементов в таблице.
   </details>
---
7. ![Вопрос 7](img/7_question.jpg)
   <details>
   <summary>Ответ</summary>
   901, 902, 903
   </details>
---
8. ![Вопрос 8](img/8_question.jpg)
   <details>
   <summary>Ответ</summary>
   reference - в бд это ссылка на другую таблицу
    PRIMARY KEY (то есть  unique, not null)
   </details>
---
9. ![Вопрос 9](img/9_question.jpg)
   <details>
   <summary>Ответ</summary>
   ON DELETE RESTRICT
   RESTRICT отличается от CASCADE тем, что она запрещает удаление, если есть связанные данные в других таблицах.
   А CASCADE удаляет данные вместе с связанными данными.
   </details>
---