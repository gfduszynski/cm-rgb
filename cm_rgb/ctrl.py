import hid
import math
from enum import Enum


class LedChannel(Enum):
    R_STATIC = 0x00
    R_BREATHE = 0x01
    R_CYCLE = 0x02
    LOGO = 0x05
    FAN = 0x06
    R_RAINBOW = 0x07
    R_SWIRL = 0x0A
    OFF = 0xFE


class LedMode(Enum):
    OFF = 0x00
    STATIC = 0x01
    CYCLE = 0x02
    BREATHE = 0x03
    R_RAINBOW = 0x05
    R_SWIRL = 0x4a
    R_DEFAULT = 0xFF


class CMRGBController:
    VENDOR_ID = 0x2516
    PRODUCT_ID = 0x0051
    PRODUCT_STR = 'CYRM02p0303h00E0r0100'
    IFACE_NUM = 1

    @staticmethod
    def new_packet(fill, *args):
        pkt = bytearray([fill] * 65)
        pkt[0] = 0  # Report ID
        for i, v in enumerate(args):
            pkt[i + 1] = v
        return pkt

    # 52 get / 51 SET - looks like even numbers are getters and odd setters
    P_POWER_ON = new_packet.__func__(0, 0x41, 0x80)
    P_POWER_OFF = new_packet.__func__(0, 0x41, 0x03)
    P_RESTORE = new_packet.__func__(0, 0x41)
    P_LED_LOAD = new_packet.__func__(0, 0x50)
    P_LED_SAVE = new_packet.__func__(0, 0x50, 0x55)
    P_APPLY = new_packet.__func__(0, 0x51, 0x28, 0x00, 0x00, 0xe0)
    P_MAGIC_2 = new_packet.__func__(0, 0x51, 0x96)
    P_MIRAGE_OFF = new_packet.__func__(0, 0x51, 0x71, 0x00, 0x00, 0x01, 0x00, 0xFF, 0x4A, 0x02, 0x00, 0xFF, 0x4A, 0x03,
                                       0x00, 0xFF, 0x4A, 0x04, 0x00, 0xFF, 0x4A)
    P_GET_VER = new_packet.__func__(0, 0x12, 0x20)                                   

    def __init__(self):
        self.__init_hid_device()
        self.__init_controller()

    def __init_hid_device(self):
        device_list = [x for x in hid.enumerate(self.VENDOR_ID, self.PRODUCT_ID)
                       if x['interface_number'] == self.IFACE_NUM]
        if len(device_list) == 0:
            raise Exception("No devices found. See: https://github.com/gfduszynski/cm-rgb/issues/9")

        self.device = hid.device()
        self.device.open_path(device_list[0]["path"])

    def __init_controller(self):
        # Without this controller wont accept changes
        self.send_packet(self.P_POWER_ON)

        # No idea what this does but it's in original startup sequence
        self.send_packet(self.P_MAGIC_2)

        # Some sort of apply / flush op
        self.apply()        

    def send_packet(self, packet):
        self.device.write(packet)
        return self.device.read(64)

    def apply(self):
        return self.send_packet(self.P_APPLY)

    def save(self):
        return self.send_packet(self.P_LED_SAVE)

    def restore(self):
        self.send_packet(self.P_LED_LOAD)
        self.send_packet(self.P_POWER_OFF)
        self.send_packet(self.P_RESTORE)
        self.apply()

    def disableMirage(self):
        self.send_packet(self.enableMirage(0,0,0))

    def enableMirage(self, rHz, gHz, bHz):
        def hzToBytes(hz):
            if hz == 0:
                return [0x00, 0xFF, 0x4A]
            v = 187498.0 / hz
            vMul = math.floor(v/256.0)
            vRem = v / (vMul + 1)
            return [min(vMul,255), math.floor(vRem % 1 * 256), math.floor(vRem)]

        rBytes = hzToBytes(rHz)
        gBytes = hzToBytes(gHz)
        bBytes = hzToBytes(bHz)

        pkt = self.new_packet(0, 0x51, 0x71, 0x00, 0x00, 
        0x01, 0x00, 0xFF, 0x4A, # This part is probably for white LED's that did not found their way into final cooler
        0x02, rBytes[0], rBytes[1], rBytes[2], 
        0x03, gBytes[0], gBytes[1], gBytes[2],  
        0x04, bBytes[0], bBytes[1], bBytes[2])
        return self.send_packet(pkt)

    def getVersion(self):
        reply = self.send_packet(self.P_GET_VER)
        fv = bytearray(16)

        i = 0
        while i < 16 :
            if reply[i + 0x08] != 0 :
                fv[int(i / 2)] = fv[int(i / 2)] + reply[i + 0x08]
            else:
                break
            i+=2

        return fv.decode("utf-8")


    # color_source 0x20 takes supplied color for breathe mode
    def set_channel(self, channel, mode, brightness, r, g, b, speed=0xff, color_source=0x20):
        pkt = self.new_packet(0xff, 0x51, 0x2C, 0x01, 0x0, channel.value, speed, color_source, mode.value, 0xFF,
                              brightness, r, g, b, 0x00, 0x00, 0x00)
        return self.send_packet(pkt)

    def assign_leds_to_channels(self, logo, fan, *ring):
        pkt = self.new_packet(0x00, 0x51, 0xA0, 0x01, 0, 0, 0x03, 0, 0, logo.value, fan.value)
        j = 0
        # Ring LED's
        for i in range(11, 26):
            if j < len(ring):
                pkt[i] = ring[j].value
                j += 1
            else:
                pkt[i] = LedChannel.OFF.value

        return self.send_packet(pkt)
