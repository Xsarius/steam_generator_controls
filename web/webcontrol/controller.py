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

    # Commands - dict with approperiate commands

    def set_commands(self, commands):
        self.control_commands['heater_1_power'] = commands['heater_1_power']
        self.control_commands['heater_2_power'] = commands['heater_2_power']
        self.control_commands['heater_3_power'] = commands['heater_3_power']
        self.control_commands['heater_st_power'] = commands['heater_steam_power']
        self.control_commands['valve'] = commands['valve']
        self.control_commands['STOP'] = commands['STOP']
        self.control_commands['save'] = commands['save']

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
