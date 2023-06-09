from datetime import datetime

from model.Condition import Condition
from model.Language import Language


def print_header(header: str):
    print('\n')
    print('*' * (len(header) + 6))
    print(f'** {header} **')
    print('*' * (len(header) + 6))


def parse_conditions(to_parse: str):
    raw_conditions = to_parse.split(',')
    conditions = []
    for raw_condition in raw_conditions:
        conditions.append(Condition(raw_condition))
    return conditions


def parse_languages(to_parse: str):
    raw_languages = to_parse.split(',')
    languages = []
    for raw_language in raw_languages:
        languages.append(Language[raw_language])
    return languages


def parse_date(to_parse: str):
    return datetime.strptime(to_parse, '%d-%m-%Y')


def parse_date_time(to_parse: str):
    return datetime.strptime(to_parse, '%d-%m-%Y %H:%M')


def parse_client(to_parse: str, clients):
    for client in clients:
        if client.name == to_parse:
            return client
    return None
