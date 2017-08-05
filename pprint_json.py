import json
import sys


def load_data(filepath):
    try:
        json_file = open(filepath, 'r')
    except FileNotFoundError:
        raise FileNotFoundError('Файл %s не существует.' % filepath)
    return json.loads(''.join(json_file.readlines()))


def pretty_print_json(data):
    def prettify(current_object, tabs=0, first_token_tabs=True, has_next=True):
        open_token = '{' if type(current_object) == dict else '['
        close_token = '}' if type(current_object) == dict else ']'
        if first_token_tabs:
            print('\t' * tabs + open_token)
        else:
            print(open_token)
        # Показывает сколько ключей из объекта уже были отработаны, нужно для постановки запятой
        iterated = 0
        for key in current_object:
            iterated += 1
            if type(current_object) == dict:
                print('\t' * (tabs + 1) + key + ': ', end='')
                if type(current_object[key]) == dict or type(current_object[key]) == list:
                    prettify(current_object[key], tabs + 1, False, len(current_object) - iterated != 0)
                else:
                    print(str(current_object[key]) + ',' * min(1, len(current_object) - iterated))
            else:
                if type(key) == dict or type(key) == dict:

                    prettify(key, tabs + 1, True, len(current_object) - iterated != 0)
        print('\t' * tabs + close_token, end='')
        if has_next:
            print(',')
        else:
            print()

    prettify(data, 0, False, False)

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