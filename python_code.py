from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont, ImageDraw
from pathlib import Path
import yfinance as yf
import time


serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)


font_path = str(Path(__file__).resolve().parent.joinpath('luma.examples', 'examples', 'fonts', 'pixelmix.ttf'))
font2 = ImageFont.truetype(font_path, 8)
font3 = ImageFont.truetype(font_path, 8)
font4 = ImageFont.truetype(font_path, 8)

while True:

    ticker = yf.Ticker("BTC-EUR")
    data = ticker.history(period='1d')
    hinta = data['Close'].iloc[-1]
    pyoristettu_hinta = round(hinta, 2)
    print(pyoristettu_hinta)


    text = "BITCOIN HINTA (EUR)"
    lol = 0.00129156 * pyoristettu_hinta
    trol = round(lol, 2)
    omistus = ("Minun BTC: " + str(trol))




    with canvas(device) as draw:
        #Kordinaattien otto
        bbox = draw.textbbox((0,0), text, font=font2)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[0]

        bbox = draw.textbbox((0, 0), str(pyoristettu_hinta), font=font2)
        print(bbox)
        pyoristettu_hinta_width = bbox[2] - bbox[0]
        pyoristettu_hinta_height = bbox[3] - bbox[0]

        bbox = draw.textbbox((0, 0), str(omistus), font=font2)
        omistus_width = bbox[2] - bbox[0]
        omistus_height = bbox[3] - bbox[0]

        # Koordinaatit
        x = (device.width - text_width) // 2
        y = (device.height - text_height) // 2

        a = (device.width - pyoristettu_hinta_width) // 2
        b = (device.height - pyoristettu_hinta_height) // 2

        c = (device.width - omistus_width) // 2
        d = (device.height - omistus_height) // 2



        #Käsky piirtämiselle
        draw.text((x, 0), text, fill="white", font=font2)
        draw.text((a, 9), str(pyoristettu_hinta), fill="white", font=font3)
        draw.text((c, d), omistus, fill="white", font=font4)

    time.sleep(50)
