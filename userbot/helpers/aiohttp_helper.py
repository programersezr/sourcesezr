# https://github.com/pokurt/Nana-Remix/blob/5ec27fcc124e7438b2816731c07ea4a129dc9a4d/nana/utils/aiohttp_helper.py#L4
# ported from nana remix

import aiohttp


class AioHttp:
    @tt_tt_4
    async def get_json(link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                return await resp.json()

    @tt_tt_4
    async def get_text(link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                return await resp.text()

    @tt_tt_4
    async def get_raw(link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                return await resp.read()

    @tt_tt_4
    async def get_status(link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                return resp.status
