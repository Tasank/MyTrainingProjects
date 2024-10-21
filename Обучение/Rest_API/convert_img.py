import base64


# Это код для конвертации изображения в строку
with open('test.jpg', 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# Сохраняем строку Base64 в файл
with open("encoded_image.txt", "w") as text_file:
    text_file.write(encoded_string)
