# cursor

## cursor介绍
> cursor官网： https://www.cursor.com/

+ cursor是一个集成了GPT4、Claude 3.5等先进LLM的类vscode的编译器
+ cursor的布局和vscode基本一致，并且cursor的使用操作也和vscode一致，包括extension下载、python编译器配置、远程服务器连接和settings等

## cursor下载及安装


## cursor的功能
### cursor Tab
> 使用`Tab`键代码自动填充

1. Tab功能打开和关闭
![](./pics/cursor1.png)

2. Tab的功能
+ 生成代码, 从光标所在的地方给出建议添加的代码
+ 多行编辑，一次性修改多行，比如修改多行代码的缩进
+ 智能重写，根据最新的更新和报错，提出一些建议
+ 光标预测，自动预测下一个光标所在的位置

3. Tab（cursor预测功能）显示
> ✔ Tab同意，Esc拒绝
> ✔ Ctrl+-> 逐步同意

+ 灰色代码： 光标预测的代码
+ 弹窗代码：发现问题，给出建议
![](./pics/cursor2.png)

### chat
> 用语言模型（ChatGPT 4.0这种）帮你生成代码，还不用自己复制粘贴，你觉得代码生成的还可以，就让Cursor直接帮你放文件里
1. chat的功能
使用`Ctrl+L`打开chat窗口

2. @功能
![](./pics/cursor4.png)

### composer
> 代码编辑窗口生成新的代码或者，编辑现在有的代码

1. composer的功能
使用`Ctrl+I`打开composer窗口

## 推荐插件
### 