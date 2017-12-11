

import mipow.bleee as ble


class Mipow:

    UUID_LIGHT_LEVEL = "0000fffc-0000-1000-8000-00805f9b34fb"

    def __init__(self, address, device="hci0"):
        """Create new Mipow object.

        Args:
            address (str): Bluetooth address of the light bulb
            device (str, optional): Name of the BlueZ device to use
        """
        self.address = address
        self.device = device
        self._ble = ble.BLE()
        self._device = self._ble.device_by_address(address)

    def connect(self):
        """Connect to the device."""
        self._device.Connect()

    def disconnect(self):
        """Disconnect from the device."""
        self._device.Disconnect()

    def set(self, r, g, b, l=0):
        """
        Set the device color.

        Args:
            r (int): Red color component (0-255)
            g (int): Green color component (0-255)
            b (int): Blue color component (0-255)
            l (int, optional): Warm white color component (0-255)
        """
        self.connect()
        char = self._device.char_by_uuid(self.UUID_LIGHT_LEVEL)
        char.write(bytes([l, r, g, b]))
