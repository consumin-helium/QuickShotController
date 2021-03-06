import sys, traceback

if '--help' in sys.argv:
    print("""Tests the nxt-python setup and brick firmware interaction
Usage: nxt_test           # Finds one brick and shows information about it
       nxt_test --verbose # Shows more debug information when trying to find the brick
       nxt_test --help    # Shows this help
""")
    exit(0)

import nxt
import nxt.locator
import nxt.brick
import nxt.usbsock

#nxt.locator.make_config()
from nxt.motor import *
debug = False
if '--verbose' in sys.argv or '--debug' in sys.argv:
    debug = True
    print('debug = True')

b = None
try:
    print('Find brick...', flush=True)
    b = nxt.locator.find_one_brick(debug=True)
    name, host, signal_strength, user_flash = b.get_device_info()
    print('NXT brick name: %s' % name)
    print('Host address: %s' % host)
    print('Bluetooth signal strength: %s' % signal_strength)
    print('Free user flash: %s' % user_flash)
    prot_version, fw_version = b.get_firmware_version()
    print('Protocol version %s.%s' % prot_version)
    print('Firmware version %s.%s' % fw_version)
    millivolts = b.get_battery_level()
    print('Battery level %s mV' % millivolts)
    print('Play test sound...', end='', flush=True)
    b.play_tone_and_wait(300, 50)
    b.play_tone_and_wait(400, 50)
    b.play_tone_and_wait(500, 50)
    b.play_tone_and_wait(600, 50)
    print('done')
except:
    print("Error while running test:")
    traceback.print_tb(sys.exc_info()[2])
    print(str(sys.exc_info()[1]))
    if b in locals():
        b.sock.close()


print("AIDS")



m_left = Motor(b, PORT_B)
m_left.turn(100, 20)