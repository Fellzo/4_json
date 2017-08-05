import json
import sys


def load_data(filepath):
    try:
        json_file = open(filepath, 'r')
    except FileNotFoundError:
        raise FileNotFoundError('Файл %s не существует.' % filepath)
    return json.loads(''.join(json_file.readlines()))


def __get_tokens_for_object(object_type):
    return '{' if object_type == dict else '[', '}' if object_type == dict else ']'


def __is_iterable(object_type):
    return object_type == list or object_type == dict


def __prettify(current_object, tabs=0, first_token_tabs=True, has_next=True):
    open_token, close_token = __get_tokens_for_object(type(object))
    if first_token_tabs:
        print('\t' * tabs + open_token)
    else:
        print(open_token)
    # Показывает сколько ключей из объекта уже были отработаны, нужно для постановки запятой
    iterated = 0
    for key in current_object:
        iterated += 1
        keys_left = len(current_object) - iterated
        if type(current_object) == dict:
            print('\t' * (tabs + 1) + key + ': ', end='')
            if __is_iterable(type(current_object[key])):
                __prettify(current_object[key], tabs + 1, False, keys_left != 0)
            else:
                print(str(current_object[key]) + ',' * min(1, keys_left))
        else:
            if __is_iterable(type(key)):
                __prettify(key, tabs + 1, True, keys_left != 0)
    print('\t' * tabs + close_token, end='')
    if has_next:
        print(',')
    else:
        print()


def pretty_print_json(json_input_data):
    __prettify(json_input_data, 0, False, False)


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