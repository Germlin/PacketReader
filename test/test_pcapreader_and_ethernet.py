# -*- encoding=utf-8 -*-

__author__ = 'linyue'

import PyPcap
import sys
import os


if __name__ == "__main__":
    file_name = "weather_channel_android_app.pcap"
    test_path = sys.path[0]
    program_path = os.path.abspath(os.path.join(test_path, os.pardir))
    input_path = os.path.join(program_path, 'input')
    output_path = os.path.join(program_path, 'output')
    input_file = os.path.join(input_path, file_name)

    pcap_file = PyPcap.pcapreader.PcapFile(input_file)
    pcap_file_header = pcap_file.get_pcap_header()
    print(pcap_file_header)

    packet_list = pcap_file.get_packet()
    print(len(packet_list))

    eth = PyPcap.ethernet.Ethernet(packet_list[0])
    print(eth.get_dst(), eth.get_src(), eth.get_type())
