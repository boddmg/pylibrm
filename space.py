from pylibrm import RMAxis as Axis


def go_home(x: Axis, y, z, timeout):
    x.go_home()
    pass


def move_relative(x_handle, x_distance, y_handle, y_distance, z_handle, z_distance, timeout):
    pass


def move_absolute(x_handle, x_distance, y_handle, y_distance, z_handle, z_distance, timeout):
    pass


def config_motions(x_speed, x_acc, x_dec, y_speed, y_acc, y_dec, z_speed, z_acc, z_dec):
    pass


#TODO: force calibration.
def config_force(external_weight)
    pass


def read_softwareVersion():
    pass


def read_force():
    pass
