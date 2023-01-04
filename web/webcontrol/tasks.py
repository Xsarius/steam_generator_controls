from celery import shared_task
from .sensors import devices

class SGController:
    def __init__(self):
        self.STOP = 0
        self.temp = [0, 0, 0]
        self.pressure = 0
        self.control_commands = {
            'heater_1_power': 0,
            'heater_2_power': 0,
            'heater_3_power': 0,
            'heater_st_power': 0,
            'valve': 0,
        }


    @shared_task()
    def control_loop(self):
        print("Controls started")

        # Water temperature sensor
        temp_sensor_w1 = devices.Pt100_SPI()

        # Steam temperature sensors
        temp_sensor_s1 = devices.Pt100_SPI()
        temp_sensor_s2 = devices.Pt100_SPI()

        # Pressure sensor
        pressure_sensor_1 = devices.Keller23SX_RS485()

        # Water 3 phase heater
        heater_water_1 = devices.Heater_SSR()
        heater_water_2 = devices.Heater_SSR()
        heater_water_3 = devices.Heater_SSR()

        # Steam 1 phase superheater
        heater_steam_1 = devices.Heater_SSR()

        steam_valve_1 = devices.Valve_SRR()

        while True:

            if(self.STOP):
                heater_steam_1.off()
                heater_water_1.off()
                heater_water_2.off()
                heater_water_3.off()
                steam_valve_1.close()

            self.temp[0] = temp_sensor_w1.getTemp()
            self.temp[1] = temp_sensor_s1.getTemp()
            self.temp[2] = temp_sensor_s2.getTemp()
            self.pressure = pressure_sensor_1.getPressure()

            if(self.control_commands['heater_st_power']):
                heater_steam_1.on()
            elif(not self.control_commands['heater_st_power']):
                heater_steam_1.off()

            if(self.control_commands['heater_1_power']):
                heater_water_1.on()
            elif(not self.control_commands['heater_1_power']):
                heater_water_1.off()

            if(self.control_commands['heater_2_power']):
                heater_water_2.on()
            elif(not self.control_commands['heater_2_power']):
                heater_water_2.off()

            if(self.control_commands['heater_3_power']):
                heater_water_3.on()
            elif(not self.control_commands['heater_3_power']):
                heater_water_3.off()

            if(self.control_commands['valve']):
                steam_valve_1.open()
            elif(not self.control_commands['valve']):
                steam_valve_1.close()

    # Commands - dict with approperiate commands

    def set_commands(self, commands):
        self.control_commands['heater_1_power'] = commands['heater_1_power']
        self.control_commands['heater_2_power'] = commands['heater_2_power']
        self.control_commands['heater_3_power'] = commands['heater_3_power']
        self.control_commands['heater_st_power'] = commands['heater_st_power']
        self.control_commands['valve'] = commands['valve']
        self.control_commands['STOP'] = commands['STOP']

    def get_output(self):
        output = {
            'water_temp': self.temp[0],
            'steam_temp_1': self.temp[1],
            'steam_temp_2': self.temp[2],
            'pressure': self.pressure,
            'heater_1': self.control_commands['heater_1_power'],
            'heater_2': self.control_commands['heater_2_power'],
            'heater_3': self.control_commands['heater_3_power'],
            'heater_st': self.control_commands['heater_st_power'],
            'valve': self.control_commands['valve'],
        }

        return output

sgcontroller1 = SGController()