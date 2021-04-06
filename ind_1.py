#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 13. Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения. Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть упорядочены по трем первым цифрам номера телефона; вывод на
# экран информации о человеке, чья фамилия введена с клавиатуры; если такого нет, выдать
# на дисплей соответствующее сообщение.

# Выполнить индивидуальное задание 2 лабораторной работы 13, добавив возможность работы с
# исключениями и логгирование.

# Изучить возможности модуля logging. Добавить для предыдущего задания вывод в файлы лога
# даты и времени выполнения пользовательской команды с точностью до миллисекунды.


from datetime import date
import logging
import sys
import xml.etree.ElementTree as ET
import modul


if __name__ == '__main__':

    logging.basicConfig(
        filename='peoples.log',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s:%(message)s'
    )

    staff = modul.Staff()
    while True:
        try:
            command = input(">>> ").lower()
            if command == 'exit':
                break


            elif command == 'add':
                surname = input("Фамилия ")
                name = input("Имя ")
                number = int(input("Номер телефона "))
                year = input("Дата рождения в формате: дд.мм.гггг ")

                staff.add(surname, name, number, year)
                logging.info(
                    f"Добавлена фамилия: {surname}, "
                    f"Добавлено имя {name}, "
                    f"Добавлен номер телефона {number}, "
                    f"Добавлена дата рождения {year}. "
                )


            elif command == 'list':
                print(staff)
                logging.info("Отображен список людей.")

            elif command.startswith('select '):
                parts = command.split(' ', maxsplit=2)
                selected = staff.select(parts[1])

                if selected:
                    for c, people in enumerate(selected, 1):
                        print(
                            ('Фамилия:', people.surname),
                            ('Имя:', people.name),
                            ('Номер телефона:', people.number),
                            ('Дата рождения:', people.year)
                        )
                    logging.info(
                        f"Найден человек с фамилией {People.surname}"
                    )

                else:
                    print("Таких фамилий нет!")
                    logging.warning(
                        f"Человек с фамилией {People.surname} не найден."
                    )

            elif command.startswith('load '):
                parts = command.split(' ', maxsplit=1)
                staff.load(parts[1])
                logging.info(f"Загружены данные из файла {parts[1]}.")

            elif command.startswith('save '):
                parts = command.split(' ', maxsplit=1)
                staff.save(parts[1])
                logging.info(f"Сохранены данные в файл {parts[1]}.")

            elif command == 'help':

                print("Список команд:\n")
                print("add - добавить человека;")
                print("list - вывести список людей;")
                print("select <фамилия> - запросить информацию по фамилии;")
                print("help - отобразить справку;")
                print("load <имя файла> - загрузить данные из файла;")
                print("save <имя файла> - сохранить данные в файл;")
                print("exit - завершить работу с программой.")
            else:
                raise UnknownCommandError(command)

        except Exception as exc:
            logging.error(f"Ошибка: {exc}")
            print(exc, file=sys.stderr)
