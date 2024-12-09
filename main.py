from advance.async_compute import hello, get_hello
from advance.numpy_math import np_size
import asyncio
from datetime import datetime
import pytest


async def main():
    print(f"End time: {datetime.now()}")
    await hello()
    print(f"End time: {datetime.now()}")

    await get_hello()

    size = np_size(10, 2, 5)
    print(f"Size: {size}")



# Python 3.7+
asyncio.run(main())
