from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP",
    ])
w,h = device().get_current_resolution()
#分辨率
w = 1280
h = 720
'''
点击屏幕
w_percentage:宽度百分比
h_percentage:高度百分比
click_time:点击次数
click_space:点击间隔
'''
def v_click(w_percentage,h_percentage,click_time=10,click_space=0.5):
        for i in range(0,click_time):
          touch((w_percentage*w,h_percentage*h))
          sleep(0.5)
        #touch((w_percentage*w,h_percentage*h),times=click_time)

v_click(0.5,0.5,10)