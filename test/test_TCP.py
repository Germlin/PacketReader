__author__ = 'Reuynil'

import ProtocolReverse
import os
import sys

if __name__ == '__main__':
    file_name = "20150325_douban.pcap"
    test_path = sys.path[0]
    program_path = os.path.abspath(os.path.join(test_path, os.pardir))
    input_path = os.path.join(program_path, 'input')
    output_path = os.path.join(program_path, 'output')
    input_file = os.path.join(input_path, file_name)

    pcap_file = ProtocolReverse.pcapreader.PcapFile(input_file)
    res = ProtocolReverse.tcp.TCP.reassemble_tcp(pcap_file)
    data_path = os.path.join(output_path, file_name)
    os.makedirs(data_path, exist_ok=True)
    for t in res:
        t.save(data_path)
