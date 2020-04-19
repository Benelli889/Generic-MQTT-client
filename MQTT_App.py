# -*- coding: utf-8 -*-
import os
import paho.mqtt.client as mqtt
from threading import Thread
import time
from MQTT_Client import MqttHandler

mqtt = MqttHandler()


class AppClass():
    # def __init__(self):
    # Thread.__init__(self)
    #self.daemon = True
    # self.start()

    # def run(self):
    # for source in range(1, 6):
    # self.mainfunction(source)

    def mainfunction(self, source):

        if source == 2:
            mqtt.led_on()
            print("mqtt.led_on()")
        elif source == 5:
            mqtt.led_off()
            print("mqtt.led_off()")
        else:
            mqtt.get_status()
            print("mqtt.get_status()")

        time.sleep(1)


App = AppClass()


def on_message_App(client, userdata, message):
    print("AppClass() on_message")
    print("client: {}, userdata: {}, message: {}".format(
        client, userdata, message))


if __name__ == '__main__':

    #eingabe = input("> ")
    s = 0
    # while eingabe != "q":
    ON_MESSAGE_GLOBAL_K1 = 0xFF

    while True:

        if mqtt.ON_MESSAGE_GLOBAL != ON_MESSAGE_GLOBAL_K1:
            #    print("ON_MESSAGE_GLOBAL: {}".format(
            #        mqtt.ON_MESSAGE_GLOBAL))

            if mqtt.ON_MESSAGE_GLOBAL == '0':
                print("LED: {}".format(mqtt.ON_MESSAGE_GLOBAL))
            elif mqtt.ON_MESSAGE_GLOBAL == '1':
                print("LED: {}".format(mqtt.ON_MESSAGE_GLOBAL))
            elif mqtt.ON_MESSAGE_GLOBAL != ON_MESSAGE_GLOBAL_K1:
                print("LED: {} {}".format("undefined:", mqtt.ON_MESSAGE_GLOBAL))

        ON_MESSAGE_GLOBAL_K1 = mqtt.ON_MESSAGE_GLOBAL
    mqtt._stop()
