from flask import Flask, request, jsonify

from Обучение.Rest_API.DatabaseHandler import DatabaseHandler

# Создание приложения Flask
app = Flask(__name__)

# Создание экземпляра DatabaseHandler
db_handler = DatabaseHandler()


# Определение маршрута для обработки POST-запросов
@app.route('/submitData', methods=['POST'])
def submit_data():
    try:
        # Получение данных из запроса
        data = request.json

        # Проверка типа данных
        if not isinstance(data, dict):
            # Возвращение ошибки, если данные не являются словарем
            return jsonify(status=400, message="Неверный формат данных"), 400

        # Определение обязательных полей
        required_fields = ['beauty_title', 'title', 'add_time', 'user', 'coords', 'level', 'images']

        # Проверка обязательных полей
        for field in required_fields:
            if field not in data:
                # Возвращение ошибки, если обязательное поле отсутствует
                return jsonify(status=400, message=f"Отсутствует обязательное поле {field}"), 400

        # Получение информации о пользователе
        user_info = data.get('user', {})

        # Проверка типа данных
        if not isinstance(user_info, dict):
            # Возвращение ошибки, если данные не являются словарем
            return jsonify(status=400, message="Неверный формат информации о пользователе"), 400

        # Определение обязательных полей для пользователя
        required_user_fields = ['email', 'fam', 'name', 'otc', 'phone']

        # Проверка обязательных полей для пользователя
        for field in required_user_fields:
            if field not in user_info:
                # Возвращение ошибки, если обязательное поле отсутствует
                return jsonify(status=400, message=f"Отсутствует обязательное поле {field} в информации о пользователе"), 400

        # Получение координат
        coords = data.get('coords', {})

        # Проверка типа данных
        if not isinstance(coords, dict):
            # Возвращение ошибки, если данные не являются словарем
            return jsonify(status=400, message="Неверный формат координат"), 400

        # Определение обязательных полей для координат
        required_coords_fields = ['latitude', 'longitude', 'height']

        # Проверка обязательных полей для координат
        for field in required_coords_fields:
            if field not in coords:
                # Возвращение ошибки, если обязательное поле отсутствует
                return jsonify(status=400, message=f"Отсутствует обязательное поле {field} в координатах"), 400

        # Получение уровня
        level = data.get('level', {})

        # Проверка типа данных
        if not isinstance(level, dict):
            # Возвращение ошибки, если данные не являются словарем
            return jsonify(status=400, message="Неверный формат уровня"), 400

        # Определение обязательных полей для уровня
        required_level_fields = ['winter', 'summer', 'autumn', 'spring']

        # Проверка обязательных полей для уровня
        for field in required_level_fields:
            if field not in level:
                # Возвращение ошибки, если обязательное поле отсутствует
                return jsonify(status=400, message=f"Отсутствует обязательное поле {field} в уровне"), 400

        # Получение изображений
        images = data.get('images', [])

        # Проверка типа данных
        if not isinstance(images, list) or not all(isinstance(image, dict) for image in images):
            # Возвращение ошибки, если данные не являются списком словарей
            return jsonify(status=400, message="Изображения должны быть списком словарей"), 400

        try:
            # Проверка существования пользователя
            if db_handler.check_user_exists(user_info.get('email')):
                # Возвращение ошибки, если пользователь уже существует
                return jsonify(status=400, message="Пользователь уже существует"), 400

            # Добавление пользователя
            user_id = db_handler.add_user(
                user_info.get('email'),
                user_info.get('fam'),
                user_info.get('name'),
                user_info.get('otc'),
                user_info.get('phone')
            )

            # Добавление координат
            coord_id = db_handler.add_coord(
                coords.get('latitude'),
                coords.get('longitude'),
                coords.get('height')
            )

            # Добавление перевала
            pereval_id = db_handler.add_pereval(
                beauty_title=data.get('beauty_title'),
                title=data.get('title'),
                other_titles=data.get('other_titles', ""),
                connect=data.get('connect', ""),
                add_time=data.get('add_time'),
                user_id=user_id,
                coord_id=coord_id,
                level_winter=level.get('winter'),
                level_summer=level.get('summer'),
                level_autumn=level.get('autumn'),
                level_spring=level.get('spring')
            )

            # Добавление изображений
            for image in images:
                image_id = db_handler.add_image(
                    image.get('data'),
                    image.get('title'),
                    pereval_id
                )
                # Если не удалось добавить изображение, то возвращаем ошибку
                if image_id is None:
                    return jsonify(status=500, message="Ошибка при добавлении изображения"), 500

            if pereval_id is not None:
                return jsonify(status=200, id=pereval_id, message="Отправлено успешно"), 200
            else:
                return jsonify(status=500, message="Ошибка при добавлении перевала"), 500
        except Exception as e:
            return jsonify(status=500, message=f"Внутренняя ошибка {e}"), 500
    except Exception as e:
        return jsonify(status=500, message=f"Внутренняя ошибка {e}"), 500

if __name__ == '__main__':
    app.run(debug=True)