# -*- encoding=cp936 -*-

__author__ = 'Reuynil'

from utility import *
from input import *
from ethernet import *
from ip import *
from tcp import *

if __name__ == '__main__':
    file_name = "weather_channel_android_app.pcap"

    src_path = sys.path[0]
    program_path = os.path.abspath(os.path.join(src_path, os.pardir))
    input_path = os.path.join(program_path, 'input')
    output_path = os.path.join(program_path, 'output')

    input_file = os.path.join(input_path, file_name)

    pcap_file = PcapFile(input_file)
    test = pcap_file.getPcapHeader()
    print test
    print pcap_file.packetNum()

    #测试是否能够把每个packet从pcap文件上剥离下来，成功
    pkt=pcap_file.getPacket()
    eth=ethernet(pkt[0])
    print eth.getDst()
    print eth.getType()

    # 测试IP
    ip = ip(eth)
    print '-' * 60
    print ip.getDst()
    print ip.getSrc()
    print ip.fields["HeaderLength"]
    print ip.getProtocol()
    print ip.checkSum()
    print len(ip.getData() + '')

    # for ls in reassembleIP(pcap_file):
    #    print ls.dst

    test_file = open('test_text.txt', 'rb')
    test_data = test_file.readline()
    print getFiled(test_data, 0, 0, 8)
