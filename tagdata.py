import config
from ruuvitag_sensor.ruuvi import RuuviTagSensor
import datetime


def get():

    macs = [config.TAG_ASUNTO_MAC, config.TAG_YLEINEN_MAC]

    timeout_in_sec = 4

    datas = RuuviTagSensor.get_data_for_sensors(macs, timeout_in_sec)

    asunto = datas[config.TAG_ASUNTO_MAC]
    yleinen = datas[config.TAG_YLEINEN_MAC]

    timestamp = str(datetime.datetime.now())
    asunto_data = "Asunto: " + str(asunto["temperature"]) + " C  " + str(asunto["humidity"]) + " %  " + str(asunto["pressure"]) + " hPa "
    yleinen_data = "Yleinen: " + str(yleinen["temperature"]) + " C  " + str(yleinen["humidity"]) + " %  " + str(yleinen["pressure"]) + " hPa "

    return_data = timestamp + "\n" + asunto_data + "\n" + yleinen_data
    
    


    return return_data
    


