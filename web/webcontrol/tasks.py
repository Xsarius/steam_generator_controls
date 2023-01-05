from celery import shared_task
from .sensors import devices
from webcontrol.models import SteamGenerator

class SGController:
    def __init__(self, STOP=0, temp=[0, 0, 0], pressure=0, commands = {
            'heater_1_power': 0,
            'heater_2_power': 0,
            'heater_3_power': 0,
            'heater_st_power': 0,
            'valve': 0,
            'save': 0,
        }):
        self.STOP = STOP
        self.temp = temp
        self.pressure = pressure
        self.control_commands = commands

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
        heater_water_1 = devices.Heater_SSR(maxpower=2667)
        heater_water_2 = devices.Heater_SSR(maxpower=2667)
        heater_water_3 = devices.Heater_SSR(maxpower=2667)

        # Steam 1 phase superheater
        heater_steam_1 = devices.Heater_SSR(maxpower=954)

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

            if(self.control_commands['save']):
                data = {
                    'ht1_pwr': heater_water_1.power,
                    'ht2_pwr': heater_water_2.power,
                    'ht3_pwr': heater_water_3.power,
                    'htst_pwr': heater_steam_1.power,
                    'valve': steam_valve_1.state
                }
                self.save_data_to_db(data=data)

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
        self.control_commands['heater_st_power'] = commands['heater_steam_power']
        self.control_commands['valve'] = commands['valve']
        self.control_commands['STOP'] = commands['STOP']
        self.control_commands['save'] = commands['save']

    @shared_task
    def save_data_to_db(self, data):
        SteamGenerator.objects.create(
            water_temp= self.temp[0],
            steam_temp_1= self.temp[1],
            steam_temp_2= self.temp[2],
            pressure= self.pressure,
            heater_water1_power=data['ht1_pwr'],
            heater_water2_power=data['ht2_pwr'],
            heater_water3_power=data['ht3_pwr'],
            heater_steam_power = data['htst_pwr'],
            valve = data['valve']
        )

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