# credit-calculator
一个简单的收集印花活动的计算器。
我默认的收集印花活动分为5个项目，通过完成每个项目可以获得一枚印花。每一名参加者在同一个项目只能获得一枚印花。
***
当然你可以根据实际情况更改就是了。
考虑到人员分工合作的问题，负责统计活动参加者的人员使用“初始化人员名单”来创建一个JSON文件用于记录所有参加者信息。
***
## 如何创建人员名单？
只需要设定好你文件所在的绝对工作路径，然后把人员信息输入进去就好了。
***
我推荐先用EXCEL之类的工具先将人员排序，然还再按照顺序一个一个填进去，按照'姓名':'序号'的格式。
（其实序号不写也没关系）
***
姓名是可以用中文的！！！！！你要用英文我不拦你。
## 工作人员如何使用这个计算器
打开“印花分数记录主程序”就好。
因为还不知道怎么在input里面输入中文字符，所以就是全英文了。
（能上Github上不会英文？你逗我）
***
设置好程序的工作路径之后，把paticipants.json放入同一工作路径就能开工了。
***
1.使用'add'命令给一个参加者加印花，加印花的同时会记录参加者当前的印花数。
***
2.使用'check'命令查询某参加者的印花数量。
我是一个谨慎的人，所以每次add都会留下log。log我是添加到末尾而不是直接覆写，一般来说最后一次的就是了。
你要是觉得麻烦，把56行的参数'a'改成'w'就好.（我就是这么干的）
***
3.使用'quit'命令退出。但因为我没设计存档，所以工作会丢失，而且log不会在再次允许的时候初始化。
所以最好在活动结束之前一直运行着，活动结束后记得清空log。
***
4.因为懒，所以没有写防跳出，你要输入这三个指令之外的，那我……算了我还是加一下防跳出吧……我知道挺多人手残会输错
## 其它吐槽
其实我是想写英文版的，不过想到我代码中那么多中文估计老外看不懂————那我就不写了。
