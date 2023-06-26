from typing import Union
from fastapi import FastAPI,Request,Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from io import BytesIO
from pdf417 import encode, render_image

class Form(BaseModel):
    date1: str
    date2: str
    name: str
    name2: str
    number1: str
    number2: str
    type: str

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

def generate_barcode2(text):
# Convert to code words
    code = encode(text)
# Generate barcode as image
    return  render_image(code) 


def get_bytes_value(image):
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='JPEG')
    return img_byte_arr.getvalue()

@app.get("/", response_class=HTMLResponse)
def read_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})

@app.post("/generate", responses = {
        200: {
            "content": {"image/png": {}}
        }
    },
    response_class=Response)
def generate_barcode(body:Form):
    text = f"{body.number1}@{body.name}@{body.name2}@{body.number2}@{body.type}@{body.date1}@{body.date2}"
    img=generate_barcode2(text)
    p=get_bytes_value(img)
    return Response(content=p, media_type="image/png")

