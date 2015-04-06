# ProtocolReverse

一个针对手机应用协议的自动化协议逆向分析引擎。使用Python3.4开发，需要使用到Numpy。

## 算法
分析算法是基于报文序列的思路，与Discover和PI相似，加入了针对压缩数据的处理。参考了如下内容：
+ *Discover : an automatic protocol reverse engineering*
+ dpkt
+ PI

## 命名规则
+ 命名规则使用Python规定的命名风格。
+ Ethernet、IP、Tcp这些以协议名称命名的类的构造函数传入上一层数据包的**全部**数据，例如：IP(data)中的data是Ethernet层的数据包的全部内容，包括Ethernet的报文头。
+ 类`ip`指的是wireshark捕获的一个ip**数据包**，而`IpDatagram`指的是重组后的ip**数据报**。

## TODO：
+ tcp.py中用于校验校验和的函数没有完成。
+ 尽量将代码中`from moudle import *`改成`import moudle`，以减少命名冲突。
