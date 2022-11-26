import board, digitalio, adafruit_max31865

class Pt100_SPI():
    def __init__(self, pinNum):
        pin = "board.{}".format(pinNum)
        spi = board.SPI()
        cs = digitalio.DigitalInOut(pin)
        self.sensor = adafruit_max31865.MAX31865(spi, cs, wires=4)

    def getTemp(self):
        return self.sensor.temperature

class KellerPressure_SPI():
    def __init__(self, pinNum):
        pin = "board.{}".format(pinNum)

    def getPressure(self):
        return 0