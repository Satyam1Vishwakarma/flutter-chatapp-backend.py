import io
import aiohttp
import asyncio
import aiofiles
from PIL import Image

cid='52HbaJc3ppjfTYX16Lt5LGahSPh'
secrets='EwLdLyxupnvhYX/eMBgwENgqIBbASEGc0OsM4BkW5SDR31IC83FOfDBg/SAuIwWBSPu2sE/s676QR4kd/Xm7mQ=='
baseurl='https://khalbank.sirv.com'
files=f'{baseurl}/v2/files'
uploadurl=f'{files}/upload?filename=/avatar'
deleteurl=f'{files}/delete?filename=/avatar'


async def get_token():
    hdr = {'content-type': "application/json"}
    payload={"clientId": cid,"clientSecret":secrets}

    async with aiohttp.ClientSession(headers=hdr) as session:
        async with session.post(f'{baseurl}/token',json=payload) as resp:
            return (await resp.json())['token']

async def image_upload(token,name):
    hdr = {'content-type': "application/json",'authorization': "Bearer "+token}

    async with aiofiles.open(f'./avatar/{name}', mode='rb') as f:
        payload = await f.read()

    async with aiohttp.ClientSession(headers=hdr) as session:
        await session.post(f'{uploadurl}/{name}', data=payload)


async def image_delete(token,name):
    hdr = {'content-type': "application/json",'authorization': "Bearer "+token}

    async with aiohttp.ClientSession(headers=hdr) as session:
        await session.post(f'{deleteurl}/{name}')

async def byt_img(byt,filename):
    image = Image.open(io.BytesIO(byt))
    image = image.convert('RGB')
    image.save(f'./avatar/{filename}','jpeg',optimize = True,quality = 40)

async def readimage(filename):
    async with aiofiles.open(f'./avatar/{filename}', mode='rb') as f:
        byt = await f.read()
    return byt
