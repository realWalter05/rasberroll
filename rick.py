import time
import board
import busio
import digitalio
import RPi.GPIO as GPIO

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import subprocess


class Display:
    def __init__(self):
        # Config
        self.width = 128
        self.height = 64
        self.border = 5
        self.font = ImageFont.truetype("cour.ttf", 13)

        # Setup display
        self.oled = None
        self.image = None
        self.draw = None
        self.setup_display()

        # Setup displat slots
        self.slots = [0,0,0,0,0,0]
        self.slots_cordinates = [(0, 0), (0, 16), (0, 32), (70, 0), (70, 16), (70, 32)]

    def setup_display(self):
        self.oled = self.get_oled()
        self.image = self.get_default_image()
        self.draw = self.get_draw()


    def get_oled(self):
        # Use for I2C.
        i2c = board.I2C()
        oled = adafruit_ssd1306.SSD1306_I2C(self.width, self.height, i2c, addr=0x3C, reset=digitalio.DigitalInOut(board.D4))

        # Clear display.
        oled.fill(0)
        oled.show()
        return oled


    def get_default_image(self):
        image = Image.new("1", (self.oled.width, self.oled.height))
        return image


    def get_draw(self):
        draw = ImageDraw.Draw(self.image)
        draw.rectangle((0, 0, self.oled.width, self.oled.height), outline=255, fill=255)
        draw.rectangle((0, 0, self.oled.width, self.oled.height), outline=0, fill=0)
        return draw

    def print_word(self, word):
        if self.slots == [1,1,1,1,1,1]:
            self.setup_display()
            self.slots = [0,0,0,0,0,0]

        for idx,slot in enumerate(self.slots):
            if not slot:
                if word == "":
                    word = ":)"
                self.draw.text(self.slots_cordinates[idx], word, font=self.font, fill=255)
                self.oled.image(self.image)
                self.oled.show()
                self.slots[idx] = 1
                break

    def print_clock(self, time):
        self.draw.text((20,20), time, font=self.font, fill=255)
        self.oled.image(self.image)
        self.oled.show()


#if __name__ == "__main__":
#    display = Display()
#    display.print_word("lol")
#    display.print_word("lol")
