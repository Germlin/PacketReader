# Discover
一个自动化的协议逆向分析引擎

## 目录
+ [Discover](https://github.com/Reuynil/Discover#discover)
 + [代码](https://github.com/Reuynil/Discover#%E6%9D%A5%E6%BA%90)
 + [代码规则]()

## 代码
Discover使用Python3.4开发，不需要导入其他第三方模块。
### 命名规则
+ ethernet、ip、tcp这些以协议名称命名的类的构造函数传入上一层数据包的**全部**数据，例如：

 ip(data)中的data是Ethernet层的数据包的全部内容，包括Ethernet的报文头。

+ 类名首字母大写，函数名第一个单词首字母小写，后面的单词首字母大写，参数全部小写（用下划线连接）
+ 类ip指的是wireshark捕获的一个ip**数据包**，而ipDatagram指的是重组后的ip**数据报**。

### 代码结构

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
### 函数功能

#### pcapreader.py

#### tokenize.py
1. ```token```用来描述**一个**数据的记号，包括记号的类型（type，二进制：‘B’，文本：‘T’），属性（variable，```Ture```为可变），同时带有数据。两个```token```的类型和属性相同时，认为两个记号相等。
2. ```tokenPattern```用来描述**一段**数据的记号模式，它的成员是一个```list```，```list```的元素也是```list```类型，包括两个（以后可以增加）```str```类型的元素，一个代表记号的类型，一个代表记号的属性。如果两个```tokenPattern```的```list```每个元素都一样，认为两个记号模式相等。
 + ```tokenPattern```主要用来作为`message_set`的key。
3. ```data_tokenization(data)```对一段```bytes```数据尝试按照utf-8的编码方式进行解码，如果不能解码，标记为二进制数据，否则标记为文本。
 + 注意，这个函数中，一段有4个字的数据会被标记成**3**个类型为‘B’的```token```，而不是1个。
4. ```tokenization(data,text_threshold)```对一段```bytes```数据进行标记，```text_threshold```代表文本类型的数据的最小长度，默认为3。
 + 注意，在这个函数中，一段有4个字的数据会被标记成**1**个类型为‘B’的```token```个。
5. ```tokenize_tcp(tcp_datagram_list)```的参数是一个```list```，元素是```tcpDatagram```，返回值是一个```list```， 元素是```message```。注意，```message```包括三个成员:
 + ```token```构成的```list```;
 + tcpDatagram的原始数据;
 + 消息的方向。

## 算法
Discover 的算法思想来源于论文——*Discover : an automatic protocol reverse engineering*。
### 例子
|输入数据   |类型     |模块     |函数     |输出数据   |类型     |
|----------|------------|----------|----------|----------|----------|
|pcapFile  |pcap格式文件   |tcp.py      |reassemble_tcp     |tcp_datagram_list  |list(tcpDatagram)   |
|t_d_l     |list(tcpDatagram)   |tokenize.py    |tokenize_tcp   |tcp_message_list   |list(message)  |

## 参考
+ dpkt

## TODO：
+ tcp.py中用于校验校验和的函数没有完成。
