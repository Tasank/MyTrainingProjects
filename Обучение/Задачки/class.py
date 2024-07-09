"""
Представьте, что у вас есть приложение, которое оптимизировано как для ПК, так и для мобильных устройств.
Шаблоны для этих версий хранятся в каталогах full/ и mobile/. Гарантируется, что состав шаблонов идентичен,
отличается лишь содержание. Создайте простой middleware, который будет отправлять пользователю соответствующую
версию.
"""

class MobileOrFullMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # код, выполняемый до формирования ответа (или другого middleware)

        response = self.get_response(request)
        # код, выполняемый после формирования запроса (или нижнего слоя)
        if request.mobile:
            prefix = "mobile/"
        else:
            prefix = "full/"
        response.template_name = prefix + response.template_name

        return response