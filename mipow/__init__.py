

import time
import mipow.bleee as ble
import string


class Mipow:

    UUID_LIGHT_LEVEL = "0000fffc-0000-1000-8000-00805f9b34fb"
    UUID_PRODUCT_NAME = "0000ffff-0000-1000-8000-00805f9b34fb"
    UUID_FIRMWARE_REVISION = "00002a26-0000-1000-8000-00805f9b34fb"
    UUID_PIN = "0000fff7-0000-1000-8000-00805f9b34fb"

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

    def connect(self, timeout=None):
        """Connect to the device."""
        self._device.Connect()
        # Meeeh
        while timeout is None or timeout >= 0:
            if self._device.ServicesResolved:
                break
            time.sleep(1)
            if timeout is not None:
                timeout -= 1

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

    def read_firmware_revision(self):
        """Read device firmware revision.

        Returns:
            bytes: Firmware revision bytestring returned by the device
        """
        self.connect()
        return self._device.char_by_uuid(self.UUID_FIRMWARE_REVISION).read()

    def read_device_name(self):
        """Read device name string.

        Returns:
            bytes: Product name bytestring returned by the device
        """
        self.connect()
        return self._device.char_by_uuid(self.UUID_PRODUCT_NAME).read()

    def write_device_name(self, name):
        """Writes device name string.

        Args:
            name (bytes): Name of the device to use
        """
        self.connect()
        self._device.char_by_uuid(self.UUID_PRODUCT_NAME).write(name)

    def read_pin(self):
        """Reads the device PIN.

        Returns:
            bytes: PIN returned by the device
        """
        self.connect()
        return self._device.char_by_uuid(self.UUID_PIN).read()

    def write_pin(self, pin):
        """Write the device PIN.

        Args:
            pin (bytes): 4 digit PIN
        """
        self.connect()
        self._device.char_by_uuid(self.UUID_PIN).write(pin)
