# Discover
An automatic protocol reverse engineering

## ��Դ
Discover��һ���Զ�����Э������������ߣ�������Ҫ˼��������һƪ���ġ�Discover : an automatic 
protocol reverse engineering����

## �������
+ ethernet��ip��tcp��Щ��Ĺ��캯��������һ�����ݰ���**ȫ��**����ip(data)�е�data��Ethernet��
�����ݰ���ȫ�����ݣ�����Ethernet�ı���ͷ������```__init__()```�ĵ�һ��������```data.getData()```
+ ��������ĸ��д����������һ����������ĸСд������ȫ��Сд�����»������ӣ�

## ����ṹ
```
Discover---input ���Ҫ�����PCAP�ļ�
        |
        |--output �������Ľ��
        |
        |--src---input.py Դ����
              |--ethernet.py
              |--ip.py
              |--tcp.py
              |--tokenize.py
              |--main.py
              |--test\_\*
```

## �ο�
+ dpkt