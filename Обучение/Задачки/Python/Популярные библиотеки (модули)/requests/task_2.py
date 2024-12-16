"""
Сделать простой GET-запрос к сайту,
Использовать библиотеку requests и json
"""
import requests
import json

response = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
#print(response.content.decode('utf-8'))
data = json.loads(response.content)
print(type(data))

for dat in data:
    print(dat[:50], '\n')