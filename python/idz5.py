#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import sys
from datetime import date


def create_person(name, sign, date):
    """ creates person variable with its fields"""
    person = {
        'name': name,
        'sign': sign,
        'date': date,
    }
    return person


def display_list_of_workers(persons):
    """ prints charicteristics of all persons"""
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8
    )
    print(line)

    print(
        '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
            "No",
            "Ф.И.О.",
            "Знак",
            "Дата рождения"
        )
    )
    print(line)

    for idx, worker in enumerate(persons, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                idx,
                worker.get('name', ''),
                worker.get('sign', ''),
                worker.get('date', 0)
            )
        )
    print(line)


def show_sign(persons):
    """prints all persons with inputed sign"""
    selected_sign = input("What sign? ")
    date_format = "%d.%m.%Y"

    for person in persons:
        right_person_found = False
        if person['sign'] == selected_sign:
            print(person['name'], person['sign'], datetime.datetime.strptime(person['date'], date_format))
            right_person_found = True
        if not right_person_found:
            print("Нет людей со знаком ", selected_sign)


def provide_docs():
    """prints command list"""
    print("Список команд:\n")
    print("add - добавить человека;")
    print("list - вывести список людей;")
    print("show sign - запросить людей с определенным знаком зодиака;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def main():
    persons = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Фамилия и Имя? ")
            sign = input("Знак зодиака? ")
            date = input("Дата рождения? ")
            persons.append(create_person(name, sign, date))

            if len(persons) > 1:
                persons.sort(key=lambda item: item.get('sign', ''))

        elif command == 'list':
            display_list_of_workers(persons)

        elif command == 'show sign':
            show_sign(persons)

        elif command == 'help':
            provide_docs()

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
