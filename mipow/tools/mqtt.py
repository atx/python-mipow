#! /usr/bin/env python3

import argparse
import mipow
import paho.mqtt.client as mqtt


def parse_color(s):
    return [int(ca + cb, 16) for ca, cb in zip(s[::2], s[1::2])]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a", "--address",
        required=True,
        help="Bluetooth address of the device",
    )
    parser.add_argument(
        "-t", "--prefix",
        required=True,
        help="Popic prefix",
    )
    parser.add_argument(
        "-m", "--mqtt-address",
        default="127.0.0.1",
        help="MQTT server address",
    )
    parser.add_argument(
        "-p", "--mqtt-port",
        default=1883,
        help="MQTT server port"
    )
    args = parser.parse_args()

    # TODO: Multi device support

    mw = mipow.Mipow(args.address)

    topic_rgbl = args.prefix + "/rgbl"

    def on_connect(client, userdata, flags, rc):
        client.subscribe(topic_rgbl)

    def on_message(client, userdata, msg):
        color = parse_color(msg.payload.decode())
        print("Setting to", color)
        bright = color[3] if len(color) == 4 else 0
        mw.set(color[0], color[1], color[2], l=bright)

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(args.mqtt_address, args.mqtt_port, 60)

    client.loop_forever()


if __name__ == "__main__":
    main()
