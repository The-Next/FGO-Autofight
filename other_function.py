from position import *
from servant import *
from dress import *
'''
助战选择
有一个小问题，一个界面同时出现很多同样的从者带着不同礼装的时候，一定概率会选不出来带正确礼装那个，所以我在这里设置的比较慢
另外一个问题，当往下拉的时候，有可能会拉到底部，后面应该更新拉到一定次数之后，刷新助战
'''
def help_option(classify,servant,dress):
    touch(CLASS_DICT[classify])
    while(True):
        x = exists(SERVANT_DICT[servant])
        if(x):
            # x_list = find_all(SERVANT_DICT[servant])#寻找所有的目标，因为一页上可能会出现好多个相同的从者带不同的礼装
            screen = G.DEVICE.snapshot()#获取页面
            #这里做一个判定，选中礼装的框不能超出屏幕，如果超出屏幕就继续往下划
            if x[0]-80 > 1280 or x[0]-30+120 >1280 or x[1]+65 > 720 or x[1]+30+100 > 720:

                swipe(v1=(500,500),vector=(0.2,-0.2))
                sleep(0.2)
                continue
            #剪裁礼装界面
            local_screen = aircv.crop_image(screen,(x[0]-80,x[1]+65,x[0]-30+120,x[1]+30+100))
            try_log_screen(local_screen)
            #要指定的礼装
            tempalte = DRESS_DICT[dress]
            pos = tempalte.match_in(local_screen)

            if pos:#找到指定礼装
                touch(x)
                break
            else:#没找到往下滑
                swipe(v1=(500,500),vector=(0.2,-0.2))
                sleep(0.2)
        else:
           swipe(v1=(500,500),vector=(0.2,-0.2))
           sleep(0.2)
    if exists(START_TASK):#继续按钮
        touch(START_TASK)


'''连续出击，没体力默认吃金苹果'''
def continuous_attack(eat_apple = False,apple = GOLD_APPLE):
    wait(CONTINUOUS_ATTACK,timeout=50)
    touch(CONTINUOUS_ATTACK)
    if eat_apple:#如果让吃苹果
        if exists(EAT_APPLE):#判断是否需要苹果
            touch(apple)
            touch(DECIDE)
        return True
    elif exists(EAT_APPLE):#如果出现了让吃苹果，但是现在不需要吃苹果，就退出
        return False
    else:#如果不让吃苹果但是现在不需要吃苹果，继续
        return True