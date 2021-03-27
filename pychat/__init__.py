"""
Python package for running a simple websockets chat client or server.py
"""
import argparse
import time
from . import client, server

parser = argparse.ArgumentParser(description='Terminal Chat application')

parser.add_argument('-s', dest='serverQ', action='store_const',
                    const=True, default=False,
                    help='run server.py or client (default client)')

parser.add_argument('-u', metavar='url', type=str, dest="url", default='localhost',
                    help='url to connect to, not including the ws(s).')


args = parser.parse_args()
url_to_connect = args.url
if args.serverQ:
    print('starting server.py...')
    server.start()
else:
    client.ServerConnect(url_to_connect)
    while True:
        time.sleep(0.1)
