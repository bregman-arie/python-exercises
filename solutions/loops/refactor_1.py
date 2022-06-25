#!/usr/bin/env python
# coding=utf-8
from collections import namedtuple
import timeit


def before_refactor():

    Mushroom = namedtuple('Mushroom', ['name', 'poisonous'])

    mushrooms = [Mushroom('Portabello', False), Mushroom('Oyster', False),
                 Mushroom('Death Cap', True)]
    i = 0

    for mushroom in mushrooms:
        i += 1
        name = mushroom.name
        print('%d:"%s"' % (i, name))


def after_refactor():  # <- Solution is here! :)

    Mushroom = namedtuple('Mushroom', ['name', 'poisonous'])

    mushrooms = [Mushroom('Portabello', False), Mushroom('Oyster', False),
                 Mushroom('Death Cap', True)]

    for i, mushroom in enumerate(mushrooms):
        i += 1
        name = mushroom.name
        print('%d:"%s"' % (i, name))


print(timeit.timeit(
    "before_refactor()",
    setup="from __main__ import before_refactor", number=100))
print(timeit.timeit(
    "after_refactor()",
    setup="from __main__ import after_refactor", number=100))
