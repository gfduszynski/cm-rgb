#!/usr/bin/env python3

from cm_rgb.ctrl import *

c = CMRGBController()

c.set_channel(LedChannel.LOGO, LedMode.STATIC, 0xFF, 0xff, 0x00, 0xff)
c.set_channel(LedChannel.FAN, LedMode.BREATHE, 0xFF, 0x44, 0x70, 0xd0, 0x2c)
c.set_channel(LedChannel.R_STATIC, LedMode.R_DEFAULT, 0xFF, 0, 0xff, 0xff)
c.set_channel(LedChannel.R_SWIRL, LedMode.R_SWIRL, 0x60, 0xff, 0xa5, 0x00, 0x74)
c.set_channel(LedChannel.R_BREATHE, LedMode.R_DEFAULT, 0xff, 0x60, 0x00, 0x60, 0x26)

c.assign_leds_to_channels(LedChannel.LOGO, LedChannel.FAN, LedChannel.R_STATIC, LedChannel.R_STATIC,
                          LedChannel.R_STATIC,
                          LedChannel.R_STATIC, LedChannel.R_STATIC, LedChannel.R_SWIRL, LedChannel.R_SWIRL,
                          LedChannel.R_SWIRL, LedChannel.R_SWIRL, LedChannel.R_SWIRL, LedChannel.R_SWIRL,
                          LedChannel.R_BREATHE, LedChannel.R_BREATHE, LedChannel.R_BREATHE)

c.apply()
c.save()
