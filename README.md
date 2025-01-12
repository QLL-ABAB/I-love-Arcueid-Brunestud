# 基本信息
英文队名：I-love-Arcueid-Brunestud
中文队名：我要抓走你的码码

github仓库地址：https://github.com/QLL-ABAB/I-love-Arcueid-Brunestud

队员：
钱磊：找所有的素材、写所有的代码、report/README等的撰写

刘鸿瑞：None

董天阳：扫雷部分的整合

联系方式：
钱磊：qianlei2024@shanghaitech.edu.cn / 2024533134
刘鸿瑞：liuhr2024@shanghaitech.edu.cn / 2024533118
董天阳：dongty2024@shanghaitech.edu.cn / 2024533055


# 游戏特色：
1.火堆和湖泊的交互.
2.两个战斗系统：回合制的打怪和Boss战
3.丰富的商店系统，包括道具、技能等
4.City中的趣味小游戏（贪吃蛇和扫雷）
5.丰富的音乐，豪堪的爱尔奎特（这很重要）
6.精美（？）的动画
7.存档系统

# 游戏内容说明

## 开始 ##
存档系统：
游戏开始时会出现存档界面，可以选择存档开始游戏
可以按垃圾桶初始化存档

## 森林场景 ##
1.基本操作：
移动：WASD
进入传送门：按一次E

2.传送门：
场地中有两个传送门，左边的一个是boss房的入口，进入之后无法退出，只能决一死战；右边是城市的入口。

3.小怪：
森林里有两种小怪，大怪攻击力和生命值都更高。
触碰会弹出窗口，选择fight进入战斗，选择escape会扣除金币和血量,在金币不足时扣除的血量会增多。(大怪伤害更高，抢的钱也更多)
对战是回合制。选择fight会攻击，然后敌人反击；选择defend会跳过自己的攻击回合，并获得增益，下一次攻击的伤害提高。
胜利获得金币，输了则死亡。
（战斗AI扔在制作中）

4.火堆：
场地里有火堆，与其碰撞，燃烧条会增加，爆条会扣除生命值，远离火堆则燃烧条缓慢下降。

5.湖泊：
场地里有随机生成的水泊。在商店中购买桶之后可以与其交互，按方框键取水，再按一次倒出水。
取水之后方框键的左边会有瞄准的按钮，点击进入泼水模式，会出现跟随鼠标移动的瞄准圆圈。再按一遍瞄准按钮会退出瞄准模式
在瞄准模式中按空格可以泼水，此时水桶再次变回空桶状态。泼水范围内的火堆会被熄灭，不会再造成伤害。


## 城市场景 ##
1.基本操作：
移动：WASD
进入传送门：按一次E

2.小游戏：
城市里有两个游戏机，上面的一个是扫雷，下面的一个是贪吃蛇。
扫雷在雷全部排出之后会获得金币，贪吃蛇会按照蛇的长度获得金币。
左边有商店和酒店，在酒店花费金币可以重置森林里的怪物，并且在血量较少时恢复生命值；在商店里可以购买多种商品。

3.商店：
在商店里可以购买多种商品。第一行有加血（上限为20），加攻击力和吸血技能。第二行是子弹穿墙技能、加速技能和咖喱棒技能。
技能在购买后会在打BOSS的时候有奇效，获得的技能会显示在左上角。

4.AI聊天：
点击爱尔奎特就会弹出聊天框，可以与AI聊天。
第一行为你输入的内容，按backspace键可以删除，按enter键发送消息,按tab清除所有文字（刷新）
回车后会显示AI的回复，如果回复内容超过八行可以使用上下键翻页。
如果还要聊天，按tab清除所有文字,再在第一行输入你想说的话

## Boss战 ##
1.基本操作：
移动：WASD
发射子弹 ：空格键
咖喱棒蓄力：鼠标左键
咖喱棒发射：鼠标右键

2.敌人介绍:
敌人有boss和小怪.Boss会发射两种子弹，黄色的子弹不能穿透掩体，紫色的子弹会穿透掩体，并且无法被咖喱棒的剑气消除。小怪会发射可以穿墙的电磁子弹。
在传送门中会飞出小怪，小怪在掩体前方会随机移动，在快要经过掩体时通过掩体之间的空位向前，穿过掩体之后，如果主角在前方，就会对主角发起自杀式袭击。
小怪和boss均有受击动画，boss会有血条显示血量，小怪的颜色显示血量。

3.技能：
(1).购买穿墙技能之后，子弹可以穿过掩体攻击敌人。
(2).购买咖喱棒后，在蓝条充满（即冷却完成）后可以发射剑气，剑气会消灭沿途的所有小怪，同时，清除几乎所有子弹。
在能量充满时长按左键可以进行充能，左上方会显示充能进度，充能越多，剑气越大。
(3).如果购买了吸血技能，在扣除boss固定血量之后，有概率自身回血（不会超过上限20点）（剑气不可以吸血！只有普通子弹可以）。
(4).加速：减少发射普通子弹和咖喱棒充能的时间

4.传送门：
如果妄图进入产出小怪的传送门，则会被其吸住，直到死亡。

## 游戏流程也可以见视频 ##

# 游戏文件：
1.Settings.py：
游戏设置文件，包括游戏窗口大小、背景音乐、字体等。
存档系统

2.BgmPlayer.py
该文件负责处理背景音乐的播放。

3.Gamemanager.py
切换场景与接受处理键盘的输入。

4.Main.py
该文件是游戏主程序，包含了游戏主循环，负责运行游戏。

5.Player.py
该文件定义了Player类，该类负责处理玩家移动、更新玩家参数、播放人物动画等。

6.Scenes.py
该文件定义了forest和city这两个包含镜头移动的场景类。

7.Shop.py
该文件定义了商店类，负责处理商店的显示、购买道具、结算价格以及AI聊天的窗口等。

8.Add_Windows.py
该文件定义了游戏里的文字和文字框，同时也负责定义应用文字和浮窗较多的回合制战斗场景。

9.Collections.py
该文件定义了基本的父类以供继承，也定义了可以使用的代码工具。

10.Portals.py
该文件定义了传送门类。

11.Boss_and_fellows.py
该文件定义了Boss类和小兵，并包含其需要的子弹类等。

12.Boss_Scene.py
该文件定义了Boss战斗场景，包含里面实体的各种互动。

13.Boss_Scene_EntityLike.py
该文件定义了Boss战斗场景里的场景实体类。

14.Wild_Scene_EntityLike.py
该文件定义了Forest场景里的场景实体类。

15.City_Scene_EntityLike.py
该文件定义了City场景里的场景实体类。

16.Openai.py
该文件定义了OpenAI聊天机器人，负责处理AI的聊天。

17.Game_scene.py :
贪吃蛇

18.Game_scene2.py :
扫雷

19.Restart.py :
游戏开始和结束界面

20.save1.json / save2.json / save3.json :
存档文件

21.assets :
游戏素材文件夹。