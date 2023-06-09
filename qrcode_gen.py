#!/usr/bin/env python3
import sys
import qrcode
from PIL import Image

if len(sys.argv) < 3:
    raise Exception(f'Usage: {sys.argv[0]} <logo.png> <url> [color]')

logo = Image.open(sys.argv[1])

# base width
basewidth = 100

# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

# url or text for the QR code
url = sys.argv[2]

# add to QRcode
QRcode.add_data(url)

# generate QR code
QRcode.make()

# color name from command line
QRcolor = '#f18018' if len(sys.argv) < 4 else sys.argv[3]

# adding color to QR code
QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# save the QR code generated
QRimg.save(f'''qrcode_{url.replace(r':', '_').replace('/','_').replace('.','_')}.png''')

print(f'QR code generated for {url}!')
