# 自动战斗脚本


目前脚本仅支持宝具三连（计算色卡伤害难度太大）、自动选取从者、礼装，自动吃苹果（现在我只设置了金的）和自动进入下一回合，所以尽量组成能够3t的队伍再来尝试。其余的功能等我有需求了就更新了（自动抽卡功能加自动贩卖功能正在写）。

目前所有的选人、礼装、宝具都是通过图片识别来选取的，当前我只录入了我需要的东西，所以要加对象的话，请自行在字典里添加（我知道宝具完全不需要使用图片，直接用位置就行了，但是我觉得这样很酷）。

如何写脚本，请参考[接口文档](接口文档.md)。

项目使用的python版本为3.7，airtest版本为1.1.3，需要自行安装adb，设备需要设置为720*1280。

关于如何添加字典的文档还没写完，有空了再添加。

