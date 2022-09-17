import board, digitalio, adafruit_max31865

class Pt100():
    def __init__(self):
        spi = board.SPI()
        cs = digitalio.DigitalInOut(board.D5)
        self.sensor = adafruit_max31865.MAX31865(spi, cs, wires=4)

    def getTemp(self):
        return self.sensor.temperature