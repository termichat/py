"""
Python package for running a simple websockets chat client or server
"""
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('-s', dest='serverQ', action='store_const',
                    const=True, default=False,
                    help='run server or client')

args = parser.parse_args()
if args.serverQ:
    print('starting server...')
