# -*- encoding=cp936 -*-

from input import *

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
    print len(pcap_file)
    print pcap_file.getPacketHeaderNum()