import requests
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont
import time


serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)


API_URL = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=BTC-EUR"

def fetch_btc_price():
    try:
        response = requests.get(API_URL, timeout=5)
        data = response.json()
        price = data['quoteResponse']['result'][0]['regularMarketPrice']
        return price
    except Exception as e:
        print("API fetch error:", e)
        return None

def display_price(price):
    with canvas(device) as draw:
    
        header_text = "BITCOIN HINTA (EUR)"
        w, h = draw.textsize(header_text)
        x = (device.width - w) // 2
        draw.text((x, 0), header_text)

        price_text = f"{price:.2f}"
        w, h = draw.textsize(price_text)
        x = (device.width - w) // 2
        y = (device.height - h) // 2 + 4
        draw.text((x, y), price_text)

if __name__ == "__main__":
    while True:
        price = fetch_btc_price()
        if price is not None:
            display_price(price)
        time.sleep(30)
