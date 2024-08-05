
#import copy
import random
import string

# Определение начальных ресурсов на астероиде
resources = {
    "никель": 4000,
    "медь": 5000,
    "железо": 3000,
    "титан": 2000,
    "вода": 3000,
    "кислород": 2000
}

# Задачи с требованиями по ресурсам
task_dict = {
    1: {"description": "Провести диагностику всех систем зонда", "requirements": {}, "critical": True},
    2: {"description": "Установить связь с Землей", "requirements": {}, "critical": True},
    3: {"description": "Передать начальные данные на Землю", "requirements": {}, "critical": True},
    4: {"description": "Запустить системы энергоснабжения", "requirements": {}, "critical": True},
    5: {"description": "Поиск ближайших астероидов", "requirements": {}, "critical": True},
    6: {"description": "Анализ состава ближайших астероидов", "requirements": {}, "critical": True},
    7: {"description": "Выбор астероида с нужными ресурсами", "requirements": {}, "critical": True},
    8: {"description": "Навигация к выбранному астероиду", "requirements": {}, "critical": True},
    9: {"description": "Сбор образцов с поверхности астероида", "requirements": {}, "critical": True},
    10: {"description": "Анализ собранных образцов", "requirements": {}, "critical": True},
    11: {"description": "Извлечение полезных ресурсов из образцов", "requirements": {}, "critical": True},
    12: {"description": "Хранение извлеченных ресурсов", "requirements": {}, "critical": True},
    13: {"description": "Проведение профилактической проверки систем", "requirements": {}, "critical": True},
    14: {"description": "Использование ресурсов для ремонта зонда", "requirements": {"никель": 1000}, "critical": True},
    15: {"description": "Использование ресурсов для создания копии зонда", "requirements": {"титан": 500}, "critical": True},
    16: {"description": "Сбор воды с поверхности астероида", "requirements": {"вода": 500}, "critical": False},
    17: {"description": "Сбор кислорода с поверхности астероида", "requirements": {"кислород": 300}, "critical": False},
    18: {"description": "Запуск созданной копии зонда", "requirements": {}, "critical": True},
    19: {"description": "Синхронизация данных с копией зонда", "requirements": {}, "critical": True},
    20: {"description": "Передача собранных данных на Землю", "requirements": {}, "critical": False},
    21: {"description": "Оптимизация траектории полета", "requirements": {}, "critical": False},
    22: {"description": "Проверка состояния систем навигации", "requirements": {}, "critical": False},
    23: {"description": "Мониторинг космического пространства на наличие опасностей", "requirements": {}, "critical": False},
    24: {"description": "Обход препятствий на пути", "requirements": {}, "critical": False},
    25: {"description": "Продолжение поиска новых ресурсов", "requirements": {}, "critical": False},
    26: {"description": "Установка научных приборов на астероид", "requirements": {}, "critical": False},
    27: {"description": "Изучение воздействия космической среды на материалы зонда", "requirements": {}, "critical": False},
    28: {"description": "Отправка периодических отчетов на Землю", "requirements": {}, "critical": False},
    29: {"description": "Изучение гравитационных аномалий", "requirements": {}, "critical": False},
    30: {"description": "Оценка эффективности использования ресурсов", "requirements": {}, "critical": True},
}

# Функция для генерации уникального ID
def generate_unique_id(length=6):
    characters = string.ascii_uppercase + string.digits + "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    return ''.join(random.choice(characters) for _ in range(length))

# Функция для изменения ID при повреждениях
def mutate_id(current_id):
    if random.choice([True, False]):
        # Добавить символ
        new_char = random.choice(string.ascii_uppercase + string.digits + "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
        current_id += new_char
    else:
        # Удалить последний символ
        current_id = current_id[:-1]
    return current_id

# Функция для генерации астероидов или планет с случайными ресурсами
def generate_celestial_body():
    return {
        "никель": random.randint(200, 2000),
        "медь": random.randint(200, 2000),
        "железо": random.randint(200, 2000),
        "титан": random.randint(200, 2000),
        "вода": random.randint(100, 1500),
        "кислород": random.randint(100, 1500)
    }

# Функция для проверки ресурсов
def check_resources(requirements, available_resources):
    return all(available_resources.get(resource, 0) >= amount for resource, amount in requirements.items())

# Функция для уменьшения ресурсов
def reduce_resources(requirements, available_resources):
    for resource, amount in requirements.items():
        available_resources[resource] -= amount

# Функция для выполнения задачи
def execute_task(task_id, drone_state, available_resources):
    task = task_dict[task_id]
    if check_resources(task["requirements"], available_resources):
        reduce_resources(task["requirements"], available_resources)

        # Проверка на задачу починки
        if task_id == 14:
            if drone_state["прочность"] < 100:
                drone_state["прочность"] += 0.1
                print(f"    [Выполнена] {task['description']}. Прочность увеличена на 1.")
            else:
                drone_state["улучшения"] += 1
                print(f"    [Выполнена] {task['description']}. Прочность уже 100, улучшения увеличены на 1.")
        # Проверка на задачу клонирования
        elif task_id == 15:
            print(f"    [Выполнена] {task['description']}. Создается клон.")
            return True  # Возвращаем True, чтобы указать на необходимость клонирования
        else:
            print(f"    [Выполнена] {task['description']}")
    else:
        # Увеличиваем количество ошибок, если задача не может быть выполнена
        drone_state["ошибки"] += 1  # Увеличиваем количество ошибок
        if task["critical"]:
            drone_state["повреждения"] += 1
            drone_state["id"] = mutate_id(drone_state["id"])
            print(f"    [Критическая ошибка] {task['description']}. Нанесены повреждения. Новый ID: {drone_state['id']}")
        else:
            if random.choice([True, False]):
                print(f"    [Удалена] Некритическая задача '{task['description']}' удалена из-за недостатка ресурсов.")
                del task_dict[task_id]
            else:
                task_dict[task_id]["description"] += " (изменена из-за недостатка ресурсов)"
                print(f"    [Изменена] Некритическая задача '{task['description']}' изменена из-за недостатка ресурсов.")
    return False  # Возвращаем False, если клонирование не требуется

# Функция для выполнения всех задач
def execute_all_tasks(drone_state, available_resources):
    for task_id in sorted(task_dict.keys()):
        if execute_task(task_id, drone_state, available_resources):
            return True  # Возвращаем True, если необходимо клонирование
    return False  # Возвращаем False, если клонирование не требуется

# Итеративная функция для клонирования зонда
def clone_drone(drone_state, max_clones):
    current_clone = 1
    while current_clone <= max_clones:
        # Генерация нового небесного тела
        new_body_resources = generate_celestial_body()
        print(f"\nНебесное тело {current_clone}: Ресурсы {new_body_resources}")

        # Наносим повреждения за полет к новому астероиду или планете
        drone_state["прочность"] -= 0.05
        if drone_state["прочность"] <= 0:
            print(f"Зонд уничтожен из-за критических повреждений.")
            return drone_state

        # Выполняем все задачи для текущего зонда
        print(f"\nКорабль {current_clone} (ID: {drone_state['id']}):")
        needs_cloning = execute_all_tasks(drone_state, new_body_resources)

        # Клонируем зонд
        new_drone_state = {
            "ошибки": drone_state["ошибки"],
            "повреждения": drone_state["повреждения"],
            "прочность": drone_state["прочность"],
            "id": drone_state["id"],
            "улучшения": drone_state["улучшения"]
        }
        print(f"\n[Клонирование] Зонд {current_clone} клонирован. Ошибки: {new_drone_state['ошибки']}, "
              f"Повреждения: {new_drone_state['повреждения']}, Прочность: {new_drone_state['прочность']:.2f}, "
              f"ID: {new_drone_state['id']}, Улучшения: {new_drone_state['улучшения']}")

        # Обновление состояния для следующего клона
        drone_state = new_drone_state
        current_clone += 1 if needs_cloning else 0
    return drone_state

# Начальное состояние зонда
initial_drone_state = {
    "ошибки": 0,
    "повреждения": 0,
    "прочность": 100,
    "улучшения": 0,
    "id": generate_unique_id()
}

# Клонирование зонда 10000 раз
final_drone_state = clone_drone(initial_drone_state, 100000)

# Вывод конечного состояния последнего зонда
print(f"\nКонечное состояние последнего зонда:")
print(f"Ошибки: {final_drone_state['ошибки']}")
print(f"Повреждения: {final_drone_state['повреждения']}")
print(f"Прочность: {final_drone_state['прочность']:.2f}")
print(f"Улучшения: {final_drone_state['улучшения']}")
print(f"ID: {final_drone_state['id']}")
