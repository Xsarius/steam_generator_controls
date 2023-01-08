import digitalio, adafruit_max31865, serial.rs485, board
from pymodbus.client import ModbusSerialClient
import RPi.GPIO as GPIO

class Pt100_SPI():
    def __init__(self, pinNum, wires=4):
        self.pin = pinNum
        # self.spi = board.SPI()
        # self.cs = digitalio.DigitalInOut(self.pin)
        # self.sensor = adafruit_max31865.MAX31865(self.spi, self.cs, wires)

    def getTemp(self):
        return 0 #self.sensor.temperature

class Keller23SX_RS485():
    def __init__(self, USB_port, baudrate=9600):
        self.usb_port = USB_port
        self.baudrate = baudrate
        # self.serial_port = serial.rs485.RS485(port=self.usb_port, baudrate=self.baudrate)
        # self.client = ModbusSerialClient(method='rtu')
        # self.client.socket = self.serial_port

    def getPressure(self):
        # self.client.connect()
        # result = self.client.read_input_registers(1)
        # self.client.close()
        return 0

class Heater_SSR():
    def __init__(self, pinNum, maxpower, power=0):
        self.pin = pinNum
        self.power = power
        self.maxpower = maxpower
        # GPIO.setup(pinNum, GPIO.OUT)

    def on(self):
        #GPIO.output(self.pin, GPIO.HIGH)
        self.power=self.maxpower

    def off(self):
        #GPIO.output(self.pin, GPIO.LOW)
        self.power=0

class Valve_SRR():
    def __init__(self, pinNum, state='close'):
        self.pin = pinNum
        self.state = state
        # GPIO.setup(pinNum, GPIO.OUT)

    def open(self):
        #GPIO.output(self.pin, GPIO.HIGH)
        self.state = 'open'

    def close(self):
        #GPIO.output(self.pin, GPIO.LOW)
        self.state = 'closed'