#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os.path

import click


def add_train(trains, nomer, punkt, time):
    """
    Добавить данные о поезде.
    """
    trains.append({
        'nomer': nomer,
        'punkt': punkt,
        'time': time,
    })
    return trains


def display_trains(punkts):
    """
    Вывод списка поездов.
    """
    if punkts:
        click.echo('+------+----------------------------+--------------------+-----------------+')
        click.echo('| {:^6} | {:^30} | {:^20} | {:^17} |'.format("№", "Номер поезда", "Пункт назначения", "Время отправления"))
        click.echo('+------+----------------------------+--------------------+-----------------+')
        for idx, train in enumerate(punkts, 1):
            click.echo('| {:>6} | {:<30} | {:<20} | {:>17} |'.format(idx, train.get('nomer', ''), train.get('punkt', ''), train.get('time', 0)))
        click.echo('+------+----------------------------+--------------------+-----------------+')
    else:
        click.echo("Список поездов пуст.")


@click.command()
@click.option('-f', '--filename', required=True, type=str, help='Имя файла данных')
@click.option('--add', is_flag=True, help='Добавить новый поезд')
@click.option('--train', type=str, help="Номер поезда")
@click.option('--punkt', type=str, help="Пункт назначения поезда")
@click.option('--time', type=int, help="Время отправления")
def main(filename, add, train, punkt, time):
    if add:
        trains = []

        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as fin:
                trains = json.load(fin)

        if train and time:
            trains = add_train(trains, train, punkt, time)

        with open(filename, "w", encoding="utf-8") as fout:
            json.dump(trains, fout, ensure_ascii=False, indent=4)
    else:
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as fin:
                trains = json.load(fin)
                display_trains(trains)
        else:
            click.echo("Файл не существует.")


if __name__ == '__main__':
    main()