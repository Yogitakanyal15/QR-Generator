# QR code generator
import qrcode
from PIL import Image

def generator(data,file,logo_path):
    qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image()
    img=img.convert("RGBA")
    if logo_path:
        try:
            logo=Image.open(logo_path)
            logo_size=(img.size[0]//5,img.size[1]//5)
            logo=logo.resize(logo_size)
            logo_pos=((img.size[0]-logo.size[0])//2,(img.size[1]-logo.size[1])//2)
            img.paste(logo,logo_pos)
        except FileNotFoundError:
            print("Your logo file doesn't found!")
            return

    img.save(file)
    print("QR generated successfully!")

data=input("Enter the data you want to embedd within the QR: ")
file=input("Enter the file name for your QR (Eg: QR.png): ")
logo_path=input("Enter the  path of your logo: ")

generator(data,file,logo_path)
