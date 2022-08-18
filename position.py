'''
该文件记录按钮的位置信息
'''
from airtest.core.api import *
#分辨率
w = 1280
h = 720
#，指令卡位置，根据分辨率获取的相对位置(在1280*720下测得的数据)
THE_FIRST_CARD=[0.10*w, 0.7*h]#第一张指令卡
THE_SECOND_CARD=[0.3*w, 0.7*h]#第二张指令卡
THE_THIRD_CARD=[0.50*w, 0.7*h]#第三张指令卡
THE_FOURTH_CARD=[0.70*w, 0.7*h]#第四张指令卡
THE_FIFTH_CARD=[0.90*w, 0.7*h]#第五张指令卡

#技能组定位
#第一个从者
THE_FIRST_SKILL_ONE = [0.055*w, 0.8*h]#一技能
THE_FIRST_SKILL_TWO = [0.13*w, 0.8*h]
THE_FIRST_SKILL_THREE = [0.2*w, 0.8*h]

#第二个从者
THE_SECOND_SKILL_ONE = [0.3*w, 0.8*h]#一技能
THE_SECOND_SKILL_TWO = [0.375*w, 0.8*h]
THE_SECOND_SKILL_THREE = [0.45*w, 0.8*h]

#第三个从者
THE_THIRD_SKILL_ONE = [0.55*w, 0.8*h]#一技能
THE_THIRD_SKILL_TWO = [0.625*w, 0.8*h]
THE_THIRD_SKILL_THREE = [0.7*w, 0.8*h]

#技能选定目标
SKILL_ORDER_ONE = [0.2*w, 0.7*h]#一技能
SKILL_ORDER_TWO = [0.5*w, 0.7*h]
SKILL_ORDER_THREE = [0.8*w, 0.7*h]

#御主技能选取
MASTER_SKILL_ONE = [0.70*w, 0.45*h]
MASTER_SKILL_TWO = [0.77*w, 0.45*h]
MASTER_SKILL_THREE = [0.84*w, 0.45*h]

#换人选取
PLACE_ONE = [0.10*w,0.45*h]
PLACE_TWO = [0.25*w,0.45*h]
PLACE_THREE = [0.40*w,0.45*h]
PLACE_FOUR = [0.57*w,0.45*h]
PLACE_FIVE = [0.75*w,0.45*h]
PLACE_SIX = [0.9*w,0.45*h]

EXCHANGE = [0.5*w,0.85*h]

#用于选取指令卡
CARD_DICT = {
    1:THE_FIRST_CARD,
    2:THE_SECOND_CARD,
    3:THE_THIRD_CARD,
    4:THE_FOURTH_CARD,
    5:THE_FIFTH_CARD
}
#用来选取技能
SKILL_DICT = {
        1:THE_FIRST_SKILL_ONE,
        2:THE_FIRST_SKILL_TWO,
        3:THE_FIRST_SKILL_THREE,
        4:THE_SECOND_SKILL_ONE,
        5:THE_SECOND_SKILL_TWO,
        6:THE_SECOND_SKILL_THREE,
        7:THE_THIRD_SKILL_ONE,
        8:THE_THIRD_SKILL_TWO,
        9:THE_THIRD_SKILL_THREE,
}
#用于选取技能所选定的目标
ORDER_DICT = {
    1:SKILL_ORDER_ONE,
    2:SKILL_ORDER_TWO,
    3:SKILL_ORDER_THREE
}


UI = 'ui'
#攻击按钮
ATTACK = Template(UI+r"/tpl1594979160293.png", record_pos=(0.386, 0.188), resolution=(1280, 720))

#点击界面
TOUCH_UI = Template(UI+r"/tpl1595078390926.png", record_pos=(0.003, 0.225), resolution=(1280, 720))
#下一步
NEXT = Template(UI+r"/tpl1595078402994.png", record_pos=(0.363, 0.238), resolution=(1280, 720))

#确定按钮
START_TASK = Template(UI+r'/$FY(L8TNHO@U$~}AN5CN1OH.png')

#连续出击
CONTINUOUS_ATTACK = Template(UI+r'/)I`@C1(@F)@2J3B]KDH)SE2.png')

#吃苹果界面
EAT_APPLE = Template(UI+r'/2)FXV]XXYHWJW_E~I[V_H57.png')

#金苹果
GOLD_APPLE = Template(UI+r'/39X`%EUD6S4DT1M]BO{@()R.png')

#决定
DECIDE = Template(UI+r'/X{(HR)IZ7(}A$TIKFGSKBLX.png')

#御主技能按钮
MASTER_BUTTON = Template(UI+r"/tpl1594975621655.png", record_pos=(0.43, -0.036), resolution=(1280, 720))
MASTER_SKILLS = {
    1:MASTER_SKILL_ONE,
    2:MASTER_SKILL_TWO,
    3:MASTER_SKILL_THREE,
}

#换人服位置
REPLACE = {
    1:PLACE_ONE,
    2:PLACE_TWO,
    3:PLACE_THREE,
    4:PLACE_FOUR,
    5:PLACE_FIVE,
    6:PLACE_SIX,
    7:EXCHANGE,
}


NoblePhantasmlist = "NoblePhantasm"

NOBLE_PHANTASM_DICT = {
    #大英雄-流星一条
    'Stella':Template(NoblePhantasmlist+r"/Stella.png", record_pos=(-0.177, -0.123), resolution=(1280, 720)),
    #崔斯坦-恸哭幻奏
    'FaliNaught':Template(NoblePhantasmlist+r"/FaliNaught.png", record_pos=(0.013, -0.073), resolution=(1280, 720)),
    #旧剑-誓约胜利之剑
    'Excalibur':Template(NoblePhantasmlist+r"/Excalibur.png", record_pos=(-0.17, -0.081), resolution=(1280, 720)),
    #艾蕾-没记住叫啥
    'KurKigalIrkalla':Template(NoblePhantasmlist+r"/KurKigalIrkalla.png", record_pos=(0.009, -0.081), resolution=(1280, 720)),
    #B阿周那-裁定归灭之回剑
    'MahaPralaya':Template(NoblePhantasmlist+r"/MahaPralaya.png", record_pos=(-0.17, -0.113), resolution=(1280, 720)),
    #长江-骑士不死于徒手
    'KnightOfOwner':Template(NoblePhantasmlist+r"/KnightOfOwner.png", record_pos=(0.01, -0.12), resolution=(1280, 720)),
    #伯爵-虎啊，起来嗨
    'EnferChateeauDIf':Template(NoblePhantasmlist+r"/EnferChateeauDIf.png", record_pos=(-0.171, -0.076), resolution=(1280, 720)),
}



class_path='class/'
#助战界面职介选取
CLASS_DICT={
    'saber':Template(class_path+r"tpl1609925611172.png", record_pos=(-0.373, -0.177), resolution=(1280, 720)),
    'archer':Template(class_path+r"tpl1609925615805.png", record_pos=(-0.321, -0.177), resolution=(1280, 720)),
    'lancer':Template(class_path+r"tpl1609925620833.png", record_pos=(-0.267, -0.178), resolution=(1280, 720)),
    'rider':Template(class_path+r"tpl1609925625707.png", record_pos=(-0.216, -0.177), resolution=(1280, 720)),
    'caster':Template(class_path+r"tpl1609925631530.png", record_pos=(-0.168, -0.18), resolution=(1280, 720)),
    'assassin':Template(class_path+r"tpl1609925638727.png", record_pos=(-0.11, -0.175), resolution=(1280, 720)),
    'bresker':Template(class_path+r"tpl1609925643743.png", record_pos=(-0.059, -0.177), resolution=(1280, 720)),
    'ex':Template(class_path+r"tpl1609925648467.png", record_pos=(-0.007, -0.18), resolution=(1280, 720)),
    'mix':Template(class_path+r"tpl1609925652073.png", record_pos=(0.045, -0.179), resolution=(1280, 720)),

}