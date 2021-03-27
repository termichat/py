from setuptools import setup

setup(
    app=["pychat"],
    setup_requires=["py2app", "websockets", "asyncio", "argparse"],
)