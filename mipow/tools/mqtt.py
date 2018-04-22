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

    topic_command = args.prefix + "/command"
    topic_rgb = args.prefix + "/rgb"
    topic_white = args.prefix + "/white"
    topic_available = args.prefix + "/available"

    def on_connect(client, userdata, flags, rc):
        print("Connected")
        for t in [topic_command, topic_rgb, topic_white]:
            client.subscribe(t)
        client.publish(topic_available, "online")

    enabled = False
    color = [0, 0, 0, 0]

    def on_message(client, userdata, msg):
        nonlocal color, enabled
        if msg.topic == topic_command:
            if msg.payload == b"ON":
                enabled = True
            else:
                enabled = False
        elif msg.topic == topic_rgb:
            for i, c in enumerate(map(int, msg.payload.split(b","))):
                color[i] = c
        elif msg.topic == topic_white:
            color[3] = int(msg.payload)
        else:
            return  # Meh

        if enabled:
            mw.set(color[0], color[1], color[2], l=color[3])
        else:
            mw.set(0, 0, 0, l=0)

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.will_set(topic_available, "offline")
    client.connect(args.mqtt_address, args.mqtt_port, 60)

    client.loop_forever()


if __name__ == "__main__":
    main()
