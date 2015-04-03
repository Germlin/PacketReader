# -*- encoding=utf-8 -*-

__author__ = 'linyue'


import ProtocolReverse
import sys
import os


def realtest():
    file_name = "15032801.pcap"
    test_path = sys.path[0]
    program_path = os.path.abspath(os.path.join(test_path, os.pardir))
    input_path = os.path.join(program_path, 'input')
    output_path = os.path.join(program_path, 'output')
    input_file = os.path.join(input_path, file_name)

    pcap_file = ProtocolReverse.pcapreader.PcapFile(input_file)
    res = ProtocolReverse.tcp.TCP.reassemble_tcp(pcap_file)
    print('here')
    print(len(res))
    msl=list()
    for t in res:
        if len(t.data)==0:
            continue
        msl.append(ProtocolReverse.tokenize.tokenize_tcp(t))

    print('here')
    mss=ProtocolReverse.initialcluster.initial_cluster(msl)
    print(len(mss))


if __name__ == '__main__':
    file_name = "15032801.pcap"
    test_path = sys.path[0]
    program_path = os.path.abspath(os.path.join(test_path, os.pardir))
    input_path = os.path.join(program_path, 'input')
    output_path = os.path.join(program_path, 'output')
    input_file = os.path.join(input_path, file_name)

    pcap_file = ProtocolReverse.pcapreader.PcapFile(input_file)
    res = ProtocolReverse.tcp.TCP.reassemble_tcp(pcap_file)
    msl = [ProtocolReverse.tokenize.tokenize_tcp(t) for t in res]
    print(len(msl))
    se=ProtocolReverse.initialcluster.cluster_by_direction(msl)
    print(len(se))
