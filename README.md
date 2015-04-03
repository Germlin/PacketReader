# ProtocolReverse

一个自动化的协议逆向分析引擎。使用Python3.4开发，需要使用到Numpy。

## 命名规则
+ Ethernet、IP、Tcp这些以协议名称命名的类的构造函数传入上一层数据包的**全部**数据，例如：IP(data)中的data是Ethernet层的数据包的全部内容，包括Ethernet的报文头。

+ 类`ip`指的是wireshark捕获的一个ip**数据包**，而`IpDatagram`指的是重组后的ip**数据报**。

## 算法
+ Discover 的算法思想来源于论文——*Discover : an automatic protocol reverse engineering*。
+ 参考了dpkt和PI。

## TODO：
+ tcp.py中用于校验校验和的函数没有完成。
+ 尽量将代码中`from moudle import *`改成`import moudle`，以减少命名冲突。
