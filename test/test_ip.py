# -*- encoding=utf-8 -*-

__author__ = 'linyue'

import PyPcap
import os
import sys

if __name__ == '__main__':
    file_name = "test_ping_ip_reassemble.pcap"
    test_path = sys.path[0]
    program_path = os.path.abspath(os.path.join(test_path, os.pardir))
    input_path = os.path.join(program_path, 'input')
    output_path = os.path.join(program_path, 'output')
    input_file = os.path.join(input_path, file_name)

    pcap_file = PyPcap.pcapreader.PcapFile(input_file)
    ip_list = PyPcap.ip.IP.reassemble_ip(pcap_file)
    print(len(ip_list))
    print(ip_list[0].dst)
