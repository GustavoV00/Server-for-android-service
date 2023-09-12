from aiohttp import web
from utils import log
import asyncio
import os

app = web.Application()
logger = log.RotatingLogger("log/log_file")

counter = 0
buffer = asyncio.Queue()
lock = asyncio.Lock()

async def handle_static(request):
    file_path = os.path.join('log', request.match_info['filename'])
    
    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return web.Response(text=content, content_type='text/plain')
    else:
        return web.Response(text="File not found", status=404)


async def save_windows(request):
    global counter

    try:
        data = await request.json()

        async with lock:
            await buffer.put(data)
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


async def reset_counter():
    global counter
    counter = 0


app.router.add_get('/static/{filename}', handle_static)
app.router.add_post("/windows", save_windows)

if __name__ == "__main__":
    web.run_app(app)
