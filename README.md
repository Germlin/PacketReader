# Discover
An automatic protocol reverse engineering

## ��Դ
Discover is an automatic protocol reverse engineering. The idea of this tool is from *Discover : an automatic protocol reverse engineering*��

## �������
+ ethernet��ip��tcp��Щ��Э��������������Ĺ��캯��������һ�����ݰ���**ȫ��**���ݣ����磺

> ip(data)�е�data��Ethernet������ݰ���ȫ�����ݣ�����Ethernet�ı���ͷ������```__init__()```�ĵ�һ��������```data.getData()```

+ ��������ĸ��д����������һ����������ĸСд������ĵ�������ĸ��д������ȫ��Сд�����»������ӣ�
+ ��ipָ����wireshark�����һ��ip���ݰ�����ipDatagramָ����������ip���ݱ�

## ����ṹ
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

## �ο�
+ dpkt
