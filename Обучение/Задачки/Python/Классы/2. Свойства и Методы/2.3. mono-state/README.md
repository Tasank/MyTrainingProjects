
"динамическое наследование" или "динамическое связывание".
В коде можно указать создание свойства  __dict__ при создании объекта.
Свойство __dict__ содержит словарь с информацией о состоянии объекта.

Это означает, что если мы создадим несколько экземпляров класса,
они все будут иметь один и тот же набор атрибутов,
а изменения в одном экземпляре будут отражаться во всех остальных.

Этот принцип ООП может быть полезен в некоторых случаях, когда необходимо создать несколько объектов с одинаковыми атрибутами, но он также может привести к неожиданным результатам, если не используется осторожно.