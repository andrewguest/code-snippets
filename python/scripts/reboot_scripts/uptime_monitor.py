#!/usr/bin/python3
import socket

from Adafruit_IO import Client
import uptime

from secrets import secrets


hostname = socket.gethostname()
adafruit_io_feed = 'servers.raspberrypi-{}-uptime'.format(hostname.lower())


#########################
#   Get server uptime   #
#########################
server_uptime = uptime.uptime()
server_uptime = server_uptime / 60
server_uptime = "{:.2f}".format(server_uptime)


#############################
#   Setup for Adafruit IO   #
#############################

# Set to your Adafruit IO key.
ADAFRUIT_IO_USERNAME = secrets['adafruitio_username']

# Set to your Adafruit IO username.
ADAFRUIT_IO_KEY = secrets['adafruitio_key']

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)


aio.send_data(adafruit_io_feed, server_uptime)
