from pdf417 import encode, render_image
from colorama import Fore, Style
from api import app
import uvicorn

def handle_inputs():
    divider='@'
    inputs=[
    'Ingrese numero de tramite : ',
    'Ingrese apellidos (separados por un espacio) : ',
    'Ingrese nombres (separados por un espacio) : ',
    'Ingrese numero de dni : ',
    'Ingrese tipo de ejemplar : ',
    'Ingrese fecha de nacimiento : ',
    'Ingrese fecha de emision : ',
    ]
    buffer=[]
    step=0

    while True: 
        temp=input(inputs[step]).upper()
        if len(temp) == 0 :
            print('')
            print(Fore.RED,"VALOR INCORRECTO")
            print(Style.RESET_ALL)
            continue
        data=temp if step==6 else temp+divider
        buffer.append(data)
        step=step + 1

        if step==7:
            break

    text=''.join(buffer)
    return text


def generate_barcode(text):
# Convert to code words
    code = encode(text)
# Generate barcode as image
    return  render_image(code) 


if __name__=='__main__':
    uvicorn.run("main:app", port=5000, log_level="info")
    # text=handle_inputs()
    # image=generate_barcode(text)
    # image.save('barcode.jpg')
    # print('============================')
    # print("=     Imagen generada!     =")
    # print('============================')



