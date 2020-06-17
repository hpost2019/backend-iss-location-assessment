#!/usr/bin/env python

__author__ = 'hpost2019'
import requests
import json


def list_astronauts():
    """Queries API to get list of astronauts in space
    and what spacecraft they are currently on"""
    res = requests.get('http://api.open-notify.org/astros.json')
    res_obj = json.loads(res.text)
    print('There are currently {0} astronauts \
in space. They are:'.format(res_obj['number']))
    for person in res_obj['people']:
        print('\t{0} who is on spacecraft: {1}\
'.format(person['name'], person['craft']))


def main():
    list_astronauts()
    pass


if __name__ == '__main__':
    main()
