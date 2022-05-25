# -*- coding:utf8 -*-
import time
import os
import platform
import motor_master.sdk as sdk

# 使用sdk函数前 请先设置加载对应的控制器版本的参数文件
# 测试时建议直接写绝对路径 避免设置了错误的参数文件 程序崩溃
sdk.init("../sdk/bin_x64/MotorMaster.Sdk.dll", "../sdk/config/MotorMaster.config")

# 使用创建函数连接轴 如果失败会抛出异常
# device为通讯的设备， linux可能为 "/dev/tty" 的形式
axis = sdk.create_modbus_rtu(bytes("\\\\.\\COM21", encoding='ascii'), 115200, 1)

# 获取当前控制器版本和类型
version = axis.get_version()
print(version.major, version.minor, version.build, version.type)

# 让轴回原点
axis.go_home()
while not axis.get_output_signal("gone_home"):
    print(axis.position())

# 让轴进行推压运动
axis.push(30, 10, 15)
timeout = axis.wait_complete(1000)

# 让轴进行绝对运动
axis.move_absolute(0, 50, 500, 500, 0.1)
timeout = axis.wait_complete(1000)

sdk.destroy(axis)
