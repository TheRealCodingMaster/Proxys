import aiohttp
import asyncio
from aiohttp import web

async def handle(request):
    target_url = request.match_info.get('url', '')
    if not target_url:
        return web.Response(text="URL not provided")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://{target_url}') as resp:
                data = await resp.read()
                return web.Response(body=data, status=resp.status, headers=resp.headers)
    except Exception as e:
        return web.Response(text=f"Error: {e}", status=500)

app = web.Application()
app.router.add_route('GET', '/{url:.*}', handle)

if __name__ == '__main__':
    web.run_app(app, port=8080)
