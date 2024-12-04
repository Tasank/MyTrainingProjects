# __eq__ - ==
# __ne__ - !=
# __lt__ - <
# __le__ - <=
# __gt__ - >
# __ge__ - >=

class Post:
    def __init__(self, title, text, category):
        self.title = title
        self.text = text
        self.category = category

    def __eq__(self, other):
        if isinstance(other, Post):
            if self.title == other.title and self.text == other.text and self.category == other.category:
                print('Найден плагиат!')
        return ''


    def __ne__(self, other):
        if isinstance(other, Post):
            if self.title != other.title or self.text != other.text or self.category != other.category:
                print('Данный пост не плагиат!')
        return ''

    def __lt__(self, other):
        if isinstance(other, Post):
            if len(self.title) < len(other.title):
                print(f'Название {self.title} поста больше {other.title}!')

        return ''

post_1 = Post('title_1', 'text_1', 'category_1')
post_2 = Post('title_11', 'text_2', 'category_2')

print(post_1 == post_2) # None
print(post_1 != post_2)
print(post_1 < post_2)