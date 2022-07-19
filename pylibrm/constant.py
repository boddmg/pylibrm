'''
Best practice 01

Put all constants in one file, and protect them from changing value.

'''
# File name: constants.py

class Const(object):
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__: # 判断是否已经被赋值，如果是则报错
            raise self.ConstError("Can't change const.%s" % name)
        if not name.isupper(): # 判断所赋值是否是全部大写，用来做第一次赋值的格式判断，也可以根据需要改成其他判断条件
            raise self.ConstCaseError('const name "%s" is not all supercase' % name)

        self.__dict__[name] = value

const = Const()

const.COMMAND_NONE = 0
const.COMMAND_GO_HOME = 1
const.COMMAND_DELAY = 2
const.COMMAND_MOVE_ABSOLUTE = 3
const.COMMAND_PUSH = 4
const.COMMAND_MOVE_RELATIVE = 5
const.COMMAND_CLOSED_LOOP_PUSH = 6

const.EXECUTE_COMMAND_INDEX = 15
const.IO_IN_NULL = 1400
const.IO_IN_GO_HOME = 1401
const.IO_IN_ERROR_RESET = 1402
const.IO_IN_START = 1403
const.IO_IN_SERVO = 1404
const.IO_IN_STOP = 1405
const.IO_IN_PAUSE = 1406
const.IO_IN_FORCE_RESET = 1424

const.IO_OUT_NULL = 0
const.IO_OUT_GONE_HOME = 1
const.IO_OUT_ALARM = 2
const.IO_OUT_IN_POSITION = 3
const.IO_OUT_REACH_POSITION_TARGET = 4
const.IO_OUT_MOVING = 5
const.IO_OUT_REACH_0 = 6
const.IO_OUT_REACH_1 = 7
const.IO_OUT_REACH_2 = 8
const.IO_OUT_REACH_3 = 9
const.IO_OUT_REACH_4 = 10
const.IO_OUT_REACH_5 = 11
const.IO_OUT_REACH_6 = 12
const.IO_OUT_REACH_7 = 13
const.IO_OUT_REACH_8 = 14
const.IO_OUT_REACH_9 = 15
const.IO_OUT_REACH_10 = 16
const.IO_OUT_REACH_11 = 17
const.IO_OUT_REACH_12 = 18
const.IO_OUT_REACH_13 = 19
const.IO_OUT_REACH_14 = 20
const.IO_OUT_REACH_15 = 21
const.IO_OUT_IN_GLOBAL_ZONE_0 = 22
const.IO_OUT_UPPER_GLOBAL_ZONE_0 = 23
const.IO_OUT_LOWER_GLOBAL_ZONE_0 = 24
const.IO_OUT_IN_GLOBAL_ZONE_1 = 25
const.IO_OUT_UPPER_GLOBAL_ZONE_1 = 26
const.IO_OUT_LOWER_GLOBAL_ZONE_1 = 27