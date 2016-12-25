Packet
========

FOO_HEADER
------------

``FOO_HEADER`` 是一个元组，里面的元素代表了报头字段。表示字段的元素也是元组，包含两个元素，分别代表了：

+ 字段名称
+ 字段类型，其数字与字母的含义与Python自带的 ``struct`` 模块中 ``unpack`` 函数参数一致。

如果你需要添加新的协议，可以定义新的 ``FOO_HEADER`` 。需要注意的是，解析报头的函数 ``parse_header`` 使用了内置函数 ``unpack`` ，它处理的最小单位是字节，如果协议报头中某些字段是以比特位为单位，需要在 ``Packet`` 中添加 ``foo_header_format`` 函数处理相应的字段。


类 Packet
------------

``Packet`` 类的成员有：

+ packet_header
+ ethernet_header
+ ip_header
+ tcp_header 或 udp_header

这些成员包括了数据包从物理层到传输层协议栈的报头。

``Packet`` 类的方法有：

+ foo_header_format
+ foo_address_format
+ quintuple

