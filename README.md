### 进度汇报：
## 成员分工：
刘鸿瑞：boss子弹的发射 （2%）
钱磊：找所有的素材、写所有的代码 （98%）
董天阳：（0%） （?）


## 游戏特色：
1.可交互的火堆以及燃烧机制
2.两个战斗系统：回合制和Boss战
3.商店系统
4.City中的趣味小游戏

## 游戏文件：
1.Settings.py：
游戏设置文件，包括游戏窗口大小、背景音乐、字体等。

2.BgmPlayer.py
该文件负责处理背景音乐的播放。

3.Gamemanager.py
切换场景

4.Main.py
该文件是游戏主程序，包含了游戏主循环，负责运行游戏。在开头会生成角色和场景

5.Player.py
该文件定义了Player类，该类负责处理玩家移动、更新玩家参数、播放人物动画等。

6.Scenes.py
该文件定义了forest和city这两个包含镜头移动的场景类和开始结束这类简单场景类。

7.Shop.py
该文件定义了商店类，负责处理商店的显示、购买道具、结算价格等。
   ## (未全部完成)

8.Add_Windows.py
该文件定义了游戏里的文字和文字框，同时也负责定义应用文字和浮窗较多的回合制战斗场景。
   ## (未全部完成)

9.Collections.py
该文件定义了基本的父类以供继承，也定义了可以使用的代码工具。

10.Portals.py
该文件定义了传送门类。

11.Boss_and_fellows.py
该文件定义了Boss类和小兵。
   ## (未全部完成)

12.Boss_Scene.py
该文件定义了Boss战斗场景。
   ## (未全部完成)

13.Boss_Scene_EntityLike.py
该文件定义了Boss战斗场景里的场景实体类。

13.Wild_Scene_EntityLike.py
该文件定义了Forest场景里的场景实体类。

13.City_Scene_EntityLike.py
该文件定义了City场景里的场景实体类。


