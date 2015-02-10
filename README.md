# Discover
An automatic protocol reverse engineering

## 来源
Discover是一个自动化的协议逆向分析工具，它的主要思想来自于一篇论文《Discover : an automatic 
protocol reverse engineering》。

## 代码规则
+ ethernet、ip、tcp这些类的构造函数传入上一层数据包的**全部**，即ip(data)中的data是Ethernet层
的数据包的全部内容，包括Ethernet的报文头，所以```__init__()```的第一步往往是```data.getData()```
+ 类名首字母大写，函数名第一个单词首字母小写，参数全部小写（用下划线连接）

## 代码结构
```
Discover---input 存放要处理的PCAP文件
        |
        |--output 存放输出的结果
        |
        |--src---input.py 源代码
              |--ethernet.py
              |--ip.py
              |--tcp.py
              |--tokenize.py
              |--main.py
              |--test\_\*
```

## 参考
+ dpkt