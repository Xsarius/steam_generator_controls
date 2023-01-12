from webcontrol.sensors import devices
from web.settings import PINS
from celery import shared_task
import time

@shared_task()
def control_loop():
    print("Controls started")

    # # Water temperature sensor
    # temp_sensor_w1 = devices.Pt100_SPI(pinNum=PINS['TEMP_WATER_1'])

    # # Steam temperature sensors
    # temp_sensor_s1 = devices.Pt100_SPI(pinNum=PINS['TEMP_STEAM_1'])
    # temp_sensor_s2 = devices.Pt100_SPI(pinNum=PINS['TEMP_STEAM_1'])

    # # Pressure sensor
    # pressure_sensor_1 = devices.Keller23SX_RS485(USB_port=PINS['USB_PORT_1'])

    # # Water 3 phase heater
    # heater_water_1 = devices.Heater_SSR(pinNum=PINS['HEATER_1'],maxpower=2667)
    # heater_water_2 = devices.Heater_SSR(pinNum=PINS['HEATER_2'],maxpower=2667)
    # heater_water_3 = devices.Heater_SSR(pinNum=PINS['HEATER_3'],maxpower=2667)

    # # Steam 1 phase superheater
    # heater_steam_1 = devices.Heater_SSR(pinNum=PINS['HEATER_STEAM_1'],maxpower=954)

    # steam_valve_1 = devices.Valve_SRR(pinNum=PINS['VALVE_1'])

    print("Controls running")

    # if(controller.STOP):
    #     heater_steam_1.off()
    #     heater_water_1.off()
    #     heater_water_2.off()
    #     heater_water_3.off()
    #     steam_valve_1.close()

    # controller.temp[0] = temp_sensor_w1.getTemp()
    # controller.temp[1] = temp_sensor_s1.getTemp()
    # controller.temp[2] = temp_sensor_s2.getTemp()
    # controller.pressure = pressure_sensor_1.getPressure()

    # if(controller.control_commands['save']):
    #     data = {
    #         'ht1_pwr': heater_water_1.power,
    #         'ht2_pwr': heater_water_2.power,
    #         'ht3_pwr': heater_water_3.power,
    #         'htst_pwr': heater_steam_1.power,
    #         'valve': steam_valve_1.state
    #     }
    #     controller.save_data_to_db(data=data)

    # if(controller.control_commands['heater_st_power']):
    #     heater_steam_1.on()
    # elif(not controller.control_commands['heater_st_power']):
    #     heater_steam_1.off()

    # if(controller.control_commands['heater_1_power']):
    #     heater_water_1.on()
    # elif(not controller.control_commands['heater_1_power']):
    #     heater_water_1.off()

    # if(controller.control_commands['heater_2_power']):
    #     heater_water_2.on()
    # elif(not controller.control_commands['heater_2_power']):
    #     heater_water_2.off()

    # if(controller.control_commands['heater_3_power']):
    #     heater_water_3.on()
    # elif(not controller.control_commands['heater_3_power']):
    #     heater_water_3.off()

    # if(controller.control_commands['valve']):
    #     steam_valve_1.open()
    # elif(not controller.control_commands['valve']):
    #     steam_valve_1.close()

    time.sleep(10)

    return 0

@shared_task()
def save_data_to_db(controller, data):
    # SteamGenerator.objects.create(
    #     water_temp= self.temp[0],
    #     steam_temp_1= self.temp[1],
    #     steam_temp_2= self.temp[2],
    #     pressure= self.pressure,
    #     heater_water1_power=data['ht1_pwr'],
    #     heater_water2_power=data['ht2_pwr'],
    #     heater_water3_power=data['ht3_pwr'],
    #     heater_steam_power = data['htst_pwr'],
    #     valve = data['valve']
    # )
    return 0