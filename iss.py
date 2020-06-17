#!/usr/bin/env python

__author__ = 'hpost2019'
import requests
import json
import turtle
import time

iss = turtle.Turtle()
in_loc = turtle.Turtle()


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


def iss_location():
    """Queries API to get current longitude and latitude
    of ISS.  Returns object with data"""
    res = requests.get('http://api.open-notify.org/iss-now.json')
    if res.status_code == 200:
        res_obj = json.loads(res.text)
        lat = float(res_obj['iss_position']["latitude"])
        long = float(res_obj['iss_position']["longitude"])
        move_iss(lat, long)
    else:
        print("Houston we need some help here!! ", res.status_code)
    reload_iss = turtle.getcanvas()
    reload_iss.after(5000, iss_location)


def screen_setup(screen):
    """Does the required setup of the screen.  Set initial size,
    sets the background image, sets world cordinates so
    lat and long work, and finally reg shapes."""
    global iss, in_loc
    screen.setup(720, 360)
    screen.title("Where in the world is ISS?")
    screen.bgpic('map.gif')
    screen.setworldcoordinates(-180, -90, 180, 90)
    in_loc.shape('circle')
    in_loc.turtlesize(.3, .3, .3)
    in_loc.color('yellow')
    turtle.register_shape("iss.gif")
    iss.shape("iss.gif")


def move_iss(lat, long):
    """Takes in current location of ISS and plots
    in on a word map"""
    global iss
    iss.penup()
    iss.goto(long, lat)


def next_over_indianapolis(long, lat):
    payload = {'lat': lat, 'lon': long}
    res = requests.get('http://api.open-notify.org/iss-pass.json',
                       params=payload)
    if res.status_code == 200:
        res_obj = json.loads(res.text)
        return res_obj['response'][0]['risetime']
    else:
        print("Houston we have another problem!! ", res.status_code)


def plot_indianapolis():
    """Plots the location on the map of Indianapolis, Indiana.
    Then writes when ISS will next be over that location. """
    global in_loc

    in_loc.penup()
    in_loc.goto(-86.159536, 39.778117)
    next_time = next_over_indianapolis(-86.159536, 39.778117)
    next_time = time.ctime(next_time)
    in_loc.write(next_time)


def main():
    global iss, in_loc
    screen = turtle.Screen()
    list_astronauts()
    screen_setup(screen)
    plot_indianapolis()
    iss_location()
    pass


if __name__ == '__main__':
    main()
    turtle.mainloop()
