import digitalio, adafruit_max31865, serial.rs485, board
from pymodbus.client import ModbusSerialClient
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class Pt100_SPI():
    def __init__(self, pinNum, wires=4):
        self.pin = "board.{}".format(pinNum)
        self.spi = board.SPI()
        self.cs = digitalio.DigitalInOut(self.pin)
        self.sensor = adafruit_max31865.MAX31865(self.spi, self.cs, wires)

    def getTemp(self):
        return self.sensor.temperature

class Keller23SX_RS485():
    def __init__(self, USB_port, baudrate=9600):
        self.usb_port = USB_port
        self.baudrate = baudrate
        self.serial_port = serial.rs485.RS485(port=self.usb_port, baudrate=self.baudrate)
        self.client = ModbusSerialClient(method='rtu')
        self.client.socket = self.serial_port

    def getPressure(self):
        self.client.connect()
        result = self.client.read_input_registers(1)
        self.client.close()
        return result

class Heater_SSR():
    def __init__(self, pinNum):
        self.pin = pinNum
        GPIO.setup(pinNum, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

class Valve_SRR():
    def __init__(self, pinNum):
        self.pin = pinNum
        GPIO.setup(pinNum, GPIO.OUT)

    def open(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def close(self):
        GPIO.output(self.pin, GPIO.LOW)