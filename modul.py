#!/usr/bin/env python3
# -*- config: utf-8 -*-

from dataclasses import dataclass, field
from typing import List


class IllegalYearError(Exception):

    def __init__(self, year, message="Illegal year (ДД.ММ.ГГГГ)"):
        self.year = year
        self.message = message
        super(IllegalYearError, self).__init__(message)

    def __str__(self):
        return f"{self.year} -> {self.message}"


class UnknownCommandError(Exception):

    def __init__(self, command, message="Unknown command"):
        self.command = command
        self.message = message
        super(UnknownCommandError, self).__init__(message)

    def __str__(self):
        return f"{self.command} -> {self.message}"


@dataclass(frozen=True)
class People:
    surname: str
    name: str
    number: int
    year: int


@dataclass
class Staff:
    peoples: List[People] = field(default_factory=lambda: [])

    def add(self, surname, name, number, year) -> None:

        if "." not in number:
            raise IllegalYearError(year)

        self.peoples.append(
            People(
                surname=surname,
                name=name,
                number=number,
                year=year
            )
        )

        self.peoples.sort(key=lambda peoples: people.number)

    def __str__(self):
        table = []
        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 20,
            '-' * 20,
            '-' * 20,
            '-' * 15
        )
        table.append(line)
        table.append(
            '| {:^4} | {:^20} | {:^20} | {:^20} | {:^15} |'.format(
                "№",
                "Фамилия ",
                "Имя",
                "Номер телефона",
                "Дата рождения"
            )
        )
        table.append(line)

        for idx, People in enumerate(self.peoples, 1):
            table.append(
                '| {:>4} | {:<20} | {:<20} | {:<20} | {:>15} |'.format(
                    idx,
                    people.surname,
                    people.name,
                    people.number,
                    people.year
                )
            )

        table.append(line)

        return '\n'.join(table)

    def select(self, surname):
        parts = command.split(' ', maxsplit=2)
        sur = (parts[1])
        result = []

        for people in self.peoples:
            if people.surname == surname:
                result.append(people)

        return result

    def load(self, filename):
        with open(filename, 'r', encoding='utf8') as fin:
            xml = fin.read()
        parser = ET.XMLParser(encoding="utf8")
        tree = ET.fromstring(xml, parser=parser)
        self.peoples = []

        for people_element in tree:
            surname, name, number, year = None, None, None, None

            for element in people_element:
                if element.tag == 'surname':
                    surname = element.text
                elif element.tag == 'name':
                    name = element.text
                elif element.tag == 'number':
                    number = element.text
                elif element.tag == 'year':
                    year = element.text

                if surname is not None and name is not None \
                        and number is not None and year is not None:
                    self.peoples.append(
                        People(
                            surname=surname,
                            name=name,
                            number=int(number),
                            year=int(year)
                        )
                    )

    def save(self, filename):
        root = ET.Element('peoples')
        for people in self.peoples:
            people_element = ET.Element('people')

            surname_element = ET.SubElement(people_element, 'surname')
            surname_element.text = people.surname

            name_element = ET.SubElement(people_element, 'name')
            name_element.text = people.name

            number_element = ET.SubElement(people_element, 'number')
            number_element.text = str(people.number)

            year_element = ET.SubElement(people_element, 'year')
            year_element.text = str(people.year)

            root.append(people_element)

        tree = ET.ElementTree(root)
        with open(filename, 'wb') as fout:
            tree.write(fout, encoding='utf8', xml_declaration=True)
