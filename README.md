# Discover
An automatic protocol reverse engineering

## 来源
Discover is an automatic protocol reverse engineering. The idea of this tool is from *Discover : an automatic protocol reverse engineering*。

## 代码规则
+ ethernet、ip、tcp这些以协议名称命名的类的构造函数传入上一层数据包的**全部**数据，例如：

> ip(data)中的data是Ethernet层的数据包的全部内容，包括Ethernet的报文头，所以```__init__()```的第一步往往是```data.getData()```

+ 类名首字母大写，函数名第一个单词首字母小写，后面的单词首字母大写，参数全部小写（用下划线连接）
+ 类ip指的是wireshark捕获的一个ip数据包，而ipDatagram指的是重组后的ip数据报

## 代码结构
```
Discover---input store the pcap file to deal with
        |
        |--output store the result
        |
        |--src---input.py source files
              |--utility.py all the other source files will import this file.
              |--ethernet.py
              |--ip.py
              |--tcp.py
              |--tokenize.py
              |--main.py
              |--test\_\*
```

## 参考
+ dpkt
