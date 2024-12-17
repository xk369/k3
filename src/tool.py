import sys
import argparse
from parser import parse_xml_to_config

def main():
    # Создаем парсер командной строки
    parser = argparse.ArgumentParser(description='Преобразование XML в конфигурационный файл')
    parser.add_argument('input_file', help='Путь к входному XML файлу')
    parser.add_argument('output_file', help='Путь для записи результата')

    args = parser.parse_args()

    # Чтение XML из файла
    try:
        with open(args.input_file, 'r', encoding='utf-8') as file:
            xml_string = file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{args.input_file}' не найден.")
        sys.exit(1)
    except IOError as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)

    # Преобразование XML в конфигурацию
    try:
        config = parse_xml_to_config(xml_string)
    except ValueError as e:
        print(f"Ошибка обработки XML: {e}")
        sys.exit(1)

    # Запись результата в файл
    try:
        with open(args.output_file, 'w', encoding='utf-8') as output_file:
            # Преобразуем словарь в строку с помощью json.dumps() и записываем в файл
            output_file.write(str(config))
        print(f"Результат сохранён в файл: {args.output_file}")
    except IOError as e:
        print(f"Ошибка при записи в файл: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
