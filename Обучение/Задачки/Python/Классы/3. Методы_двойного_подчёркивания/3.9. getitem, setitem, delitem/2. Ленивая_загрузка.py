"""
Создайте класс LazyImage, который хранит в себе путь к изображению.
Реализуйте метод __getitem__, чтобы при доступе к элементу изображения оно загружалось только тогда,
когда это необходимо.
"""
from PIL import Image


class LazyImage:
    def __init__(self, path):
        self.path = path
        self._image = None
        self._weight = None
        self._height = None

    @property
    def width(self):
        if self._weight is None:
            self._load_image_info()
        return self._width

    @property
    def height(self):
        if self._height is None:
            self._load_image_info()
        return self._height

    def _load_image_info(self):
        # Открываем изображение для получения его размеров
        with Image.open(self.path) as img:
            self._width, self._height = img.size

    def load(self):
        if self._image is None:
            self._image = Image.open(self.path)

    def __getitem__(self, item):
        if self._image is None:
            self.load()
        return self._image.__getitem__(item)


# Пример использования
img = LazyImage("image.jpg")
print(img.width)  # выведет ширину изображения, но изображение не будет загружено
print(img.height)  # выведет высоту изображения, но изображение не будет загружено
img.load()  # загрузит изображение
print(img.width)  # выведет 512
