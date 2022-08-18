from position import *
'''
攻击函数，传入一个列表，数字代表选第几个从者卡
传入str则表示宝具（见position中的宝具字典）
'''
def attack(list):
    wait(ATTACK,timeout=50)
    touch(ATTACK)
    sleep(1)#等一秒，不然点击太快，这里以后改成检查图片元素再点击
    for i in list:
        if isinstance(i,int):
            touch(CARD_DICT[i])
        elif isinstance(i,str):
            touch(NOBLE_PHANTASM_DICT[i])
            print('发动宝具 '+i+'！')
'''
使用技能，参数为一个list。按从左到右顺序，1-9
如果元素为list，则表明该技能为己方指向性buff技能，根据元素选取目标
参数格式：
        [1,[2,3],4]
从左向右：释放第一个从者的一技能
          释放第二个从者的技能给3从者
          释放第二个从者的一技能
'''
def using_skills(list1):
    for i in list1:
        sleep(0.5)
        wait(ATTACK, timeout=50)
        if isinstance(i,int):#自buff或者全体性buff
            touch(SKILL_DICT[i])
        elif isinstance(i,list):#指向性buff
            touch(SKILL_DICT[i[0]])
            sleep(0.5)
            touch(ORDER_DICT[i[1]])

'''衣服技能，参数为几技能和指向第几个从者，第二个参数默认为0,即没有指向,第三个参数为换人服'''
def monster_skills(choice,servant=0,is_charge = None):
    wait(ATTACK, timeout=50)
    touch(MASTER_BUTTON)#按下御主衣服
    sleep(0.5)
    touch(MASTER_SKILLS[choice])#选取御主技能
    if servant!=0:
       sleep(0.5)
       touch(ORDER_DICT[servant])#指向从者
    if is_charge is not None:#换人
        touch(REPLACE[is_charge[0]])
        sleep(0.5)
        touch(REPLACE[is_charge[1]])
        sleep(0.5)
        touch(REPLACE[7])

'''
结束函数，用于战斗结束
qs:这里需要解决如果出现从者升级的话，需要点击一下页面，目前思路是隔五秒点击一次
'''
def ending():
    touch(wait(TOUCH_UI,timeout=60),times=5)
    if exists(TOUCH_UI):#可能出现从者牵绊页面
        touch(TOUCH_UI)
    touch(NEXT)