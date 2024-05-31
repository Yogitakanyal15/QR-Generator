# QR code generator
import qrcode

def generator(data,file):
    qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=4,
    error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image()
    img.save(file)
    print("QR generated successfully!")

data=input("Enter the data you want to embedd within the QR: ")
file=input("Enter the file name for your QR (Eg: QR.png): ")
generator(data,file)