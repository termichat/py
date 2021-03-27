# PyTermiChat
chat without GUI

**Disclaimer:** This is not *yet* encrypted.

**Not To Be Confused with [TermChat](https://github.com/alexanderepstein/termchat)**

## installing:
```bash
pip install pytermichat
```

## running:
```bash
python -m pychat [-h] [-s] [-u]
```
***note:** this will only to connect to instances hosted on* `127.0.0.1`

## Running as a server
```bash
python -m pychat -s
```
this will run the server on `0.0.0.0:80`

current port is not *yet* changeable

## Custom Servers
```bash
python -m pychat -u "url to the server"
```

## Credits:
- Python `websockets` module
