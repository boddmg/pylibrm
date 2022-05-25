from pymodbus.client.sync import ModbusSerialClient as ModbusClient


def self_test():
    client = ModbusClient(method="rtu", port="/COM5", stopbits=1, bytesize=8, parity='N', baudrate = 115200)
    client.connect()
    print(client.read_holding_registers(0,2))
    client.close()
    pass

if __name__ == "__main__":
    self_test()

