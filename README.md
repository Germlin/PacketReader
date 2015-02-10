# Discover
An automatic protocol reverse engineering

## 来源
Discover是一个自动化的协议逆向分析工具，它的主要思想来自于一篇论文《Discover : an automatic protocol reverse engineering》

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
              |--test_*
```
## 参考
+ dpkt
