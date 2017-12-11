

import mipow.bleee as ble


class Mipow:

    def __init__(self, address, device="hci0"):
        self.address = address
        self.device = device
        self._ble = ble.BLE()
        self._device = self._ble.device_by_address(address)

    def connect(self):
        self._device.Connect()

    def disconnect(self):
        self._device.Disconnect()

    def set(self, r, g, b, l=0):
        self.connect()
        char = self._device.char_by_uuid("0000fffc-0000-1000-8000-00805f9b34fb")
        char.write(bytes([l, r, g, b]))
