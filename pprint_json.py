import json
import sys

INDENT_SIZE = 4


def load_data(filepath):
    try:
        json_file = open(filepath, 'r')
    except FileNotFoundError:
        raise FileNotFoundError('Файл %s не существует.' % filepath)
    return json.loads(''.join(json_file.readlines()))


def pretty_print_json(json_input_data):
    print(json.dumps(json_input_data, sort_keys=True, indent=INDENT_SIZE, ensure_ascii=False))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('Не передан путь к json файлу.')
    path_to_json = sys.argv[1]
    if path_to_json.split('.')[-1] != 'json':
        raise Exception('На вход должен быть подан файл с расширением json.')
    try:
        json_data = load_data(path_to_json)
    except json.JSONDecodeError:
        raise Exception('Неправильный формат json файла.')
    pretty_print_json(json_data)