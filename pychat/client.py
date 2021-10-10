import asyncio
import sys
import websockets
import time
from . import notifypy
import json

class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    GREY = '\033[90m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


async def stream_as_generator(loop, stream):
    reader = asyncio.StreamReader(loop=loop)
    reader_protocol = asyncio.StreamReaderProtocol(reader)
    await loop.connect_read_pipe(lambda: reader_protocol, stream)

    while True:
        line = await reader.readline()
        if not line:  # EOF.
            break
        yield line


class ServerConnect:
    def __init__(self, url):
        self.nickname = input(f"{BColors.BOLD}What would you like people to call you? > ")
        self.websocket = None
        self.url = url
        asyncio.run(self.start())

    async def start(self):
        await asyncio.gather(self.main(), self.hello())

    async def main(self):
        loop = asyncio.get_running_loop()
        async for line in stream_as_generator(loop, sys.stdin):
            message = str(line.decode('utf-8'))
            message_formatted = message.strip('\n')
            await self.websocket.send(message_formatted)

    async def hello(self):
        uri = f"ws://{self.url}/{self.nickname}"
        async with websockets.connect(uri) as self.websocket:
            async for messg in self.websocket:
                formatted_messg = messg.replace("\'", "\"")

                message = json.loads(formatted_messg)
                print(f"{BColors.BOLD}{message['usr']}:{BColors.ENDC}", message['msg'])

                notification = notifypy.Notify()
                notification.title = f"New message from {message['usr']}"
                notification.message = message['msg']
                notification.send()




