import websockets
import asyncio
import secrets

connected = set()


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


async def handle_connections(websocket, path):
    # Register.
    newPath = path.replace('/', '')
    await websocket.send(f'Hello. Welcome {newPath}')
    connected.add(websocket)
    try:
        async for message in websocket:
            print(message)
            for w in connected:
                if not w == websocket:
                    await w.send(f"{BColors.BOLD}{newPath}:{BColors.ENDC} {message}")
    finally:
        # Unregister.
        connected.remove(websocket)


def start():
    print()
    start_server = websockets.serve(handle_connections, "0.0.0.0", 80)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
