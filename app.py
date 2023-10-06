from aiohttp import web
from utils import log
import asyncio
import os
import json


logger = log.TimestampedRotatingLogger()

counter = 0
buffer = asyncio.Queue()
lock = asyncio.Lock()

async def save_windows(request):
    global counter

    try:
        data = await request.json()
        data_str = json.dumps(data).replace("'", '"')
        data_str = data_str.replace('false', '"False"').replace('true', '"True"')


        async with lock:
            await buffer.put(data_str)
            counter += 1

            if counter == 10:
                await asyncio.gather(log_buffer(), reset_counter())

        response_text = "Ok"
        return web.Response(text=response_text, status=200, content_type="text/plain")

    except Exception as e:
        return web.Response(
            text=f"Error: {str(e)}",
            status=500,
            content_type="text/plain",
        )


async def log_buffer():
    while not buffer.empty():
        elem = await buffer.get()
        print(elem)
        logger.info(elem)
    logger.rotate_logs()


async def reset_counter():
    global counter
    counter = 0


async def my_web_app():
    app = web.Application()
    app.router.add_post("/windows", save_windows)
    return app