import ctypes
import os 

_native_sdk = None

COMMAND_NONE = 0
COMMAND_GO_HOME = 1
COMMAND_DELAY = 2
COMMAND_MOVE_ABSOLUTE = 3
COMMAND_PUSH = 4
COMMAND_MOVE_RELATIVE = 5
command_CLOSED_LOOP_PUSH = 6

IO_IN_NULL = 0
IO_IN_GO_HOME = 1
IO_IN_ERROR_RESET = 2
IO_IN_START = 3
IO_IN_SERVO = 4
IO_IN_STOP = 5
IO_IN_PAUSE = 6
IO_IN_FORCE_INPUT = 7
IO_IN_POSITION_0 = 8
IO_IN_POSITION_1 = 9
IO_IN_POSITION_2 = 10
IO_IN_POSITION_3 = 11
IO_IN_POSITION_4 = 12
IO_IN_POSITION_5 = 13
IO_IN_POSITION_6 = 14
IO_IN_POSITION_7 = 15
IO_IN_POSITION_8 = 16
IO_IN_POSITION_9 = 17
IO_IN_POSITION_10 = 18
IO_IN_POSITION_11 = 19
IO_IN_POSITION_12 = 20
IO_IN_POSITION_13 = 21
IO_IN_POSITION_14 = 22
IO_IN_POSITION_15 = 23

IO_OUT_NULL = 0
IO_OUT_GONE_HOME = 1
IO_OUT_ALARM = 2
IO_OUT_IN_POSITION = 3
IO_OUT_REACH_POSITION_TARGET = 4
IO_OUT_MOVING = 5
IO_OUT_REACH_0 = 6
IO_OUT_REACH_1 = 7
IO_OUT_REACH_2 = 8
IO_OUT_REACH_3 = 9
IO_OUT_REACH_4 = 10
IO_OUT_REACH_5 = 11
IO_OUT_REACH_6 = 12
IO_OUT_REACH_7 = 13
IO_OUT_REACH_8 = 14
IO_OUT_REACH_9 = 15
IO_OUT_REACH_10 = 16
IO_OUT_REACH_11 = 17
IO_OUT_REACH_12 = 18
IO_OUT_REACH_13 = 19
IO_OUT_REACH_14 = 20
IO_OUT_REACH_15 = 21
IO_OUT_IN_GLOBAL_ZONE_0 = 22
IO_OUT_UPPER_GLOBAL_ZONE_0 = 23
IO_OUT_LOWER_GLOBAL_ZONE_0 = 24
IO_OUT_IN_GLOBAL_ZONE_1 = 25
IO_OUT_UPPER_GLOBAL_ZONE_1 = 26
IO_OUT_LOWER_GLOBAL_ZONE_1 = 27

class Version(ctypes.Structure):
    _fields_ = [('major', ctypes.c_int),
                ('minor', ctypes.c_int),
                ('build', ctypes.c_int),
                ('type', ctypes.c_int)]

class Command(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('position', ctypes.c_float),
                ('velocity', ctypes.c_float),
                ('acceleration', ctypes.c_float),
                ('deacceleration', ctypes.c_float),
                ('tolerance', ctypes.c_float),
                ('push_force', ctypes.c_float),
                ('push_distance', ctypes.c_float),
                ('delay', ctypes.c_float),
                ('next_command_index', ctypes.c_int)]

def init(native_path, config_path):
    global _native_sdk
    _native_sdk = ctypes.CDLL(native_path)
    _native_sdk.rm_set_config_path(config_path)

    _native_sdk.rm_get_version.restype = Version

    _native_sdk.rm_set_input_signal.argtypes = (ctypes.c_uint32, ctypes.c_char_p, ctypes.c_bool,)
    _native_sdk.rm_get_input_signal.restype = ctypes.c_bool
    _native_sdk.rm_get_output_signal.argtypes = (ctypes.c_uint32, ctypes.c_char_p,)
    _native_sdk.rm_get_output_signal.restype = ctypes.c_bool

    _native_sdk.rm_config_motion.argtypes = (ctypes.c_uint32, ctypes.c_float, ctypes.c_float, ctypes.c_float,)
    _native_sdk.rm_move_to.argtypes = (ctypes.c_uint32, ctypes.c_float,)

    _native_sdk.rm_config_motion.rm_go_home = (ctypes.c_uint32,)
    _native_sdk.rm_move_absolute.argtypes = (ctypes.c_uint32, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,)
    _native_sdk.rm_push.argtypes = (ctypes.c_uint32, ctypes.c_float, ctypes.c_float, ctypes.c_float)
    _native_sdk.rm_precise_push.argtypes = (ctypes.c_uint32, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_uint32)

    _native_sdk.rm_wait_complete.restype = ctypes.c_bool
    _native_sdk.rm_is_moving.restype = ctypes.c_bool
    _native_sdk.rm_is_reached.restype = ctypes.c_bool
    _native_sdk.rm_is_push_empty.restype = ctypes.c_bool

    _native_sdk.rm_set_command.argtypes = (ctypes.c_uint32, ctypes.c_int, Command)
    _native_sdk.rm_get_command.restype = Command
    _native_sdk.rm_execute_command.argtypes = (ctypes.c_uint32, ctypes.c_uint32)
    _native_sdk.rm_trig_command.argtypes = (ctypes.c_uint32, Command)
    _native_sdk.rm_load_commands.argtypes = (ctypes.c_uint32, Command)
    _native_sdk.rm_save_commands.argtypes = (ctypes.c_uint32, Command)
    
    _native_sdk.rm_position.restype  = ctypes.c_float
    _native_sdk.rm_velocity.restype  = ctypes.c_float
    _native_sdk.rm_torque.restype  = ctypes.c_float
    _native_sdk.rm_force_sensor.restype  = ctypes.c_float
    _native_sdk.rm_error_code.restype  = ctypes.c_uint32

    _native_sdk.rm_destroy.argtypes = (ctypes.c_uint32,)
 

class Axis:
    _handle = 0
    
    def __init__(self, handle):
        self._handle = handle

    def get_version(self):
        global _native_sdk
        return _native_sdk.rm_get_version(self._handle)

    def set_input_signal(self, signal, level):
        global _native_sdk
        _native_sdk.rm_set_input_signal(self._handle, signal, level)

    def get_input_signal(self, signal):
        global _native_sdk
        return _native_sdk.rm_get_input_signal(self._handle, signal)

    def get_output_signal(self, signal):
        global _native_sdk
        return _native_sdk.rm_get_output_signal(self._handle, signal)

    def config_motion(self, velocity, acceleration, deacceleration):
        global _native_sdk
        _native_sdk.rm_config_motion(self._handle, velocity, acceleration, deacceleration)

    def move_to(self, position):
        global _native_sdk
        _native_sdk.rm_move_to(self._handle, position)

    def go_home(self):
        global _native_sdk
        _native_sdk.rm_go_home(self._handle)

    def move_absolute(self, position, velocity, acceleration, deacceleration, band):
        global _native_sdk
        _native_sdk.rm_move_absolute(self._handle, position, velocity, acceleration, deacceleration, band)

    def push(self, force, distance, velocity):
        global _native_sdk
        _native_sdk.rm_push(self._handle, force, distance, velocity)

    def precise_push(self, force, distance, velocity, force_band, force_check_time):
        global _native_sdk
        _native_sdk.rm_precise_push(self._handle, force, distance, velocity, force_band, force_check_time)

    def wait_complete(self, timeout_ms):
        global _native_sdk
        _native_sdk.rm_wait_complete(self._handle, timeout_ms)

    def is_moving(self):
        global _native_sdk
        return _native_sdk.rm_is_moving(self._handle)

    def is_reached(self):
        global _native_sdk
        return _native_sdk.rm_is_reached(self._handle)

    def is_push_empty(self):
        global _native_sdk
        return _native_sdk.rm_is_push_empty(self._handle)

    def set_command(self, index, command):
        global _native_sdk
        _native_sdk.rm_set_command(self._handle,index, command)

    def get_command(self, index):
        global _native_sdk
        return _native_sdk.rm_get_command(self._handle, index)

    def execute_command(self, command):
        global _native_sdk
        _native_sdk.rm_execute_command(self._handle, command)

    def trig_command(self, index):
        global _native_sdk
        _native_sdk.rm_trig_command(self._handle, index)

    def load_commands(self):
        global _native_sdk
        _native_sdk.rm_load_commands(self._handle)

    def save_commands(self):
        global _native_sdk
        _native_sdk.rm_save_commands(self._handle)

    def position(self):
        global _native_sdk
        return _native_sdk.rm_position(self._handle)

    def velocity(self):
        global _native_sdk
        return _native_sdk.rm_velocity(self._handle)

    def torque(self):
        global _native_sdk
        return _native_sdk.rm_torque(self._handle)

    def force_sensor(self):
        global _native_sdk
        return _native_sdk.rm_force_sensor(self._handle)

    def error_code(self):
        global _native_sdk
        return _native_sdk.rm_error_code(self._handle)

    def reset_error(self):
        global _native_sdk
        _native_sdk.rm_reset_error(self._handle)

    def set_servo_on_off(self,on_off):
        global _native_sdk
        _native_sdk.rm_set_servo_on_off(self._handle, on_off)

    def stop(self):
        global _native_sdk
        _native_sdk.rm_stop(self._handle)


def create_modbus_rtu(device, baudrate, axis_no):
    global _native_sdk
    handle = _native_sdk.rm_create_modbus_rtu(device, baudrate, axis_no)
    if handle != -1:
        return Axis(handle)
    else:
        return None

def destroy(axis):
    global _native_sdk
    _native_sdk.rm_destroy(axis._handle)
