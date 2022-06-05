from pymodbus.client.sync import ModbusSerialClient as ModbusClient


def self_test():
    client = ModbusClient(method="rtu", port="/dev/tty.usbserial-110", stopbits=1,
                          bytesize=8, parity='N', baudrate=115200)
    connection = client.connect()
    print(connection)
    res = client.read_input_registers(8, 8, unit=2)
    print(res.registers)
    client.close()
    pass

if __name__ == "__main__":
    self_test()

