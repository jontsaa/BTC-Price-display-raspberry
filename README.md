# Bitcoin Price Ticker (SSD1306 OLED)

This Python project displays the real-time Bitcoin price (BTC to EUR) and the value of a specific crypto portfolio on an SSD1306 OLED display. It is designed to run on a Raspberry Pi (or similar Linux SBC) using the I2C interface.

## Features
- **Real-time Data:** Fetches live market data using the `yfinance` library.
- **Portfolio Tracker:** Automatically calculates the Euro value of your specific BTC holdings.
- **Dynamic Centering:** Text is programmatically centered on the display regardless of string length.
- **Hardware Support:** Built on the `luma.oled` library for SSD1306 displays.

## Hardware Requirements
- Raspberry Pi (any model with GPIO)
- SSD1306 OLED Display (128x64 or 128x32, I2C interface)
- Jumper wires

### Wiring (Default I2C)
- **VCC** -> 3.3V
- **GND** -> Ground
- **SDA** -> GPIO 2 (SDA)
- **SCL** -> GPIO 3 (SCL)

## Installation

1. **Enable I2C** on your Raspberry Pi:
   Run `sudo raspi-config` -> Interface Options -> I2C -> Enable.

2. **Install System Dependencies** (Required for Pillow/Luma):
   ```bash
   sudo apt-get update
   sudo apt-get install python3-dev libfreetype6-dev libjpeg-dev build-essential
