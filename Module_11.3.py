def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj)

    # Получаем атрибуты объекта
    attributes = dir(obj)

    # Получаем методы объекта
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    # Получаем модуль, к которому принадлежит объект
    obj_module = obj.__module__

    # Собираем информацию в словарь
    info = {
        "type": obj_type,
        "attributes": attributes,
        "methods": methods,
        "module": obj_module,
    }

    # Добавляем другие интересные свойства, если они есть
    if hasattr(obj, '__doc__'):
        info['docstring'] = obj.__doc__

    if hasattr(obj, '__dict__'):
        info['dict'] = obj.__dict__

    return info


# Пример использования:
if __name__ == "__main__":
    class Example:
        """Пример класса для демонстрации."""

        def __init__(self, value):
            self.value = value

        def display(self):
            return f"Value: {self.value}"


    example_obj = Example(42)

    # Проводим интроспекцию объекта example_obj
    result = introspection_info(example_obj)

    # Выводим результат
    for key, value in result.items():
        print(f"{key}: {value}")
