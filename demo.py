import pylibrm.RMAxis
import serial.tools.list_ports
import sys

def self_test():
    if sys.platform.find("win"):
        ports = map(lambda _: _.device, serial.tools.list_ports.comports())
        usb_ports = list(filter(lambda _: "usb" in _, ports))
        if len(usb_ports) > 0:
            print(usb_ports)
            axis = pylibrm.RMAxis.Axis.create_modbus_rtu(usb_ports[0], 1, 115200)
            axis._is_debug = True
            axis.wait(500)
            print(axis.get_version())
            axis.go_home()
            axis.wait(1000)
            for _ in range(10):
                axis.move_absolute(10, 100, 1000, 1000, 0.1)
                axis.wait_for_reached(3000)
                axis.move_absolute(0, 100, 1000, 1000, 0.1)
                axis.wait_for_reached(3000)
                print(axis.position())
            axis.close()
    else :
        pass

self_test()

