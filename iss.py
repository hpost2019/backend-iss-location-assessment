#!/usr/bin/env python

__author__ = 'hpost2019'
import requests
import json
import turtle


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


def retrieve_location():
    """Queries API to get current longitude and latitude
    of ISS.  Returns object with data"""
    res = requests.get('http://api.open-notify.org/iss-now.json')
    res_obj = json.loads(res.text)
    return {'long': res_obj['iss_position']['longitude'],
            'lat': res_obj['iss_position']['latitude'],
            'timestamp': res_obj['timestamp']}


def plot_iss():
    """Takes in current location of ISS and plots
    in on a word map"""
    image = 'iss.gif'
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.bgpic('map.gif')
    screen.setworldcoordinates(-180, -90, 180, 90)
    iss = turtle.Turtle()
    turtle.register_shape(image)
    iss.shape(image)
    loc_obj = retrieve_location()
    iss.penup()
    iss.goto(float(loc_obj['long']), float(loc_obj['lat']))
    screen.exitonclick()


def main():
    list_astronauts()
    plot_iss()
    pass


if __name__ == '__main__':
    main()
