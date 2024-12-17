import math
import re

# Проверка, является ли строка числом
def is_number(value):
    try:
        float(value)  # Пробуем преобразовать в число
        return True
    except ValueError:
        return False

# Проверка, является ли строка математическим выражением
def is_math_expression(value):
    math_chars = set("0123456789+-*/(). sqrtlen")  # Символы для мат. выражений
    return all(char in math_chars for char in value.replace(" ", ""))

# Проверка, является ли строка IP-адресом
def is_ip_address(value):
    parts = value.split(".")
    return len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)

# Функция для вычисления математических выражений
def eval_expression(expression, constants=None):
    if constants is None:
        constants = {}
    try:
        if is_number(expression):  # Если это число
            return float(expression) if '.' in expression else int(expression)
        elif is_ip_address(expression):  # Если это IP-адрес
            return expression  # Возвращаем как строку
        elif is_math_expression(expression):  # Если это математическое выражение
            # Заменяем функции на Python аналоги
            expression = expression.replace("sqrt", "math.sqrt").replace("len", "len")
            return eval(expression, {"math": math, "len": len}, constants)
        else:  # Просто строка, возвращаем как есть
            return expression
    except Exception as e:
        raise ValueError(f"Ошибка при вычислении выражения: {expression}. Детали: {str(e)}")

# Парсинг XML в конфигурацию
def parse_xml_to_config(xml_data):
    config = {}

    # Парсинг констант
    constant_pattern = re.compile(r'<constant name="([^"]+)">([^<]+)</constant>')
    constants = constant_pattern.findall(xml_data)
    for name, value in constants:
        config[name] = eval_expression(value, config)

    # Парсинг массивов
    array_pattern = re.compile(r'<array name="([^"]+)">(.*?)</array>', re.DOTALL)
    arrays = array_pattern.findall(xml_data)
    for name, values_block in arrays:
        value_pattern = re.compile(r'<value>(.*?)</value>')
        values = value_pattern.findall(values_block)
        config[name] = [eval_expression(value, config) for value in values]

    # Парсинг словарей
    dict_pattern = re.compile(r'<dict name="([^"]+)">(.*?)</dict>', re.DOTALL)
    dicts = dict_pattern.findall(xml_data)
    for name, entries_block in dicts:
        entry_pattern = re.compile(r'<entry key="([^"]+)">([^<]+)</entry>')
        entries = entry_pattern.findall(entries_block)
        config[name] = {key: eval_expression(value, config) for key, value in entries}

    return config
