import asyncio
import requests


async def hello():
    print("Hello ...")
    await asyncio.sleep(2)
    print("... World!")

async def get_hello():
    # http request to get hello
    try:
        url = "http://localhost:8000/hello"
        response = requests.get(url)
        if response.status_code == 200:
            print(response.json())
    except Exception as e:
        print(e)

    try:
        url = "http://localhost:8000/os-info"
        response = requests.get(url)
        print(response.json())
    except Exception as e:
        print(e)

    return response.json()



