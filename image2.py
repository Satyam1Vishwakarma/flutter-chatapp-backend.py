import json
import io
from urllib import response
from imagekitio import ImageKit
from PIL import Image
import aiofiles


imagekit =ImageKit(
    private_key='private_8TT0t79RFW4t4wZfd21tDDfFQ7Q=',
    public_key='public_b/yyTY7UM7tXWiOgoY5mhnFt6n4=',
    url_endpoint='https://ik.imagekit.io/yriztiyh8jv'
)


def image_upload(filename):
    resp=imagekit.upload_file(file=open(f"./avatar/{filename}","rb"),
    file_name=filename,
    options={"folder":"/avatar/"},
    )
    return resp["response"]["fileId"],resp["response"]["url"]

async def image_delete(fid):
    imagekit.delete_file(fid)
    return 'done'

async def byt_img(byt,filename):
    image = Image.open(io.BytesIO(byt))
    image = image.convert('RGB')
    image.save(f'./avatar/{filename}','jpeg',optimize = True,quality = 40)
    image_upload(filename)
