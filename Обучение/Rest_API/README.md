Чтобы протестировать REST API, можно использовать CURL. Выполнить эту команду:

#### Но!  
В коде есть проверка на уникальный ключ, она не будет работать, если вы будете использовать его ещё раз.

Поэтому если вы хотите протестировать нужно изменить переменные в запросе 

```bash
     curl -X POST -H "Content-Type: application/json" -d "{\"beauty_title\": \"Перевал\", \"title\": \"Тестовый Перевал\", \"other_titles\": \"\", \"connect\": \"\", \"add_time\": \"2021-09-22 13:18:13\", \"user\": {\"email\": \"unique_email@example.com\", \"fam\": \"Новиков\", \"name\": \"Алексей\", \"otc\": \"Алексеевич\", \"phone\": \"+7 987 654 32 10\"}, \"coords\": {\"latitude\": 50.0, \"longitude\": 40.0, \"height\": 1500}, \"level\": {\"winter\": \"\", \"summer\": \"1Б\", \"autumn\": \"1Б\", \"spring\": \"\"}, \"images\": [{\"data\": \"<base64_encoded_image_data>\", \"title\": \"Тестовое изображение\"}]}" http://127.0.0.1:5000/submitData     
```

Также для добавления изображения в запрос (в формате Base64). Необходимо добавить свой путь к изображению в файле 
convert_img.py. Вывод конвертации txt нужно скопировать и заменить строку `<base64_encoded_image_data>`.

Если возникают ошибки можно протестировать без изображения.