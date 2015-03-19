# -*- encoding=utf-8 -*-

__author__ = 'Reuynil'

from utility import *
from pcapreader import *
from ethernet import *
from ip import *
from tcp import *

# TODO：
# the follow statment is same, use the first kind.
# print(int.from_bytes(data[0:1],byteorder='big',signed=False))
# print(int(base64.b16encode(data[0:1]),16))




if __name__ == '__main__':
    file_name = "weather_channel_android_app.pcap"
    # do not edit.
    src_path = sys.path[0]
    program_path = os.path.abspath(os.path.join(src_path, os.pardir))
    input_path = os.path.join(program_path, 'input')
    output_path = os.path.join(program_path, 'output')
    # if you want to change the pcap file, you just need to change the file_name.
    input_file = os.path.join(input_path, file_name)

    pcap_file = PcapFile(input_file)
    test = pcap_file.getPcapHeader()
    print(test)
    print(pcap_file.packetNum())

    # 测试是否能够把每个packet从pcap文件上剥离下来，成功
    pkt = pcap_file.getPacket()
    eth = ethernet(pkt[8])
    print(eth.getDst())
    print(eth.getType())

    # 测试IP
    ipd = ip(eth)
    print('-' * 60)
    print(ipd.get_dst())
    print(ipd.get_src())
    print(ipd.fields["HeaderLength"])
    print(ipd.get_total_length())
    print(ipd.get_protocol())
    print(ipd.test_checksum())
    print(len(ipd.get_data()))

    # test cast for the function reassembleIP in ip.py
    print('-' * 10 + ' test for reassembleIP ' + '-' * 10)
    test_file_name = "test_ping_ip_reassemble.pcap"
    test_input_file = os.path.join(input_path, test_file_name)
    test_pcap_file = PcapFile(test_input_file)
    print(("This pcap file has %d packets." % test_pcap_file.packetNum()))
    test_packet = test_pcap_file.getPacket()[0]
    test_eth = ethernet(test_packet)
    print(("The type of the first packet is %s " % test_eth.getType()))
    test_ip = ip(test_eth)
    print(("the checksum of the ip datagram is %s" % test_ip.fields["Checksum"]))
    print((test_ip.fragment(), test_ip.moreFragment()))
    res = reassembleIP(test_pcap_file)
    print(len(res))
    res1 = res[1]
    print(len(res1.data))

    print('\n' + '-' * 10 + 'i dont know ' + '-' * 10)
    test_file = open('test_text.txt', 'rb')
    test_data = test_file.readline()

    print((get_filed(test_data, 0, 0, 8)))


    # test case for TCP
    print('\n' + '-' * 10 + 'TCP' + '-' * 10)
    assert isinstance(ipd, ip)
    ipD = ipDatagram(ipd.get_dst(), ipd.get_src(), ipd.get_protocol(), ipd.get_data())
    tcp = TCP(ipD)
    print('''
    src port: {0}
    dst port: {1}
    seq : {2}
    ack : {3}
    len : {4}
    '''.format(tcp.get_src_port(), tcp.get_dst_port(), tcp.get_seq(), tcp.get_ack(), tcp.get_length()))
    print("ACK: ", tcp.test_ack())
    print("FIN: ", tcp.test_fin())
    print("dataLength: ", tcp.get_data_length())
    print("SYN: ", tcp.test_syn())
    print("FIN: ", tcp.test_fin())
    tcp_list = TCP.reassemble_tcp(pcap_file)
    for t in tcp_list:
        t.save(output_path)
