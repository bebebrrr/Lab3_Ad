#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

import click


@click.group()
def commands():
    pass


@commands.command("add")
@click.argument("filename")
@click.option("--number", help="The train's number")
@click.option("--punkt", help="The train's punkt")
@click.option("--time", help="Departure time")
def add(filename, number, punkt, time):
    """
    Добавить данные о поезде.
    """
    trains = load_trains(filename)
    trains.append(
        {
            "number": number,
            "punkt": punkt,
            "time": time,
        }
    )
    # trains.append(train)
    save_trains(filename, trains)


@commands.command("display")
@click.argument("filename")
@click.option("--punkts", help="Display trains data")
def display_trains(filename, punkts):
    """
    Отобразить список поездов.
    """
    trains = load_trains(filename)
    if punkts:
        # Заголовок таблицы.
        line = "+-{}-+-{}-+-{}-+-{}-+".format(
            "-" * 4, "-" * 30, "-" * 20, "-" * 17
        )
        print(line)
        print(
            "| {:^4} | {:^30} | {:^20} | {:^17} |".format(
                "№", "Номер поезда", "Пункт назначения", "Время отправления"
            )
        )
        print(line)
        # Вывести данные о всех поездах.
        for idx, trains in enumerate(punkts, 1):
            print(
                "| {:>4} | {:<30} | {:<20} | {:>17} |".format(
                    idx,
                    trains.get("number", ""),
                    trains.get("punkt", ""),
                    trains.get("time", 0),
                )
            )
        print(line)

    else:
        print("Список поездов пуст.")


def load_trains(filename):
    """
    Загрузить все поезда из файла JSON.
    """
    with open(filename, "r", encoding="utf-8") as fin:
        return json.load(fin)


def save_trains(filename, number, time, punkts):
    """
    Сохранить все поезда в JSON.
    """
    with open(filename, "w", encoding="utf-8") as fount:
        json.dump(punkts, time, number, fount, ensure_ascii=False, indent=4)


@commands.command("select")
@click.argument("filename")
@click.argument("filename2")
@click.argument("timeB")
def select(filename, filename2, timeB):
    """
    Выбрать поезда с заданным временем.
    """
    trains = load_trains(filename)
    result = []
    for time in trains:
        if time.get("time") >= timeB:
            result.append(time)

    save_trains(filename2, result)
    display_trains(filename2)


def main():
    commands()


if __name__ == "__main__":
    main()
