# -*- encoding=cp936 -*-

__author__ = 'Reuynil'

from input import *
from ethernet import *
from ip import *


def reassembleIP(pcap, dst, src):
    '''

    :param packet_list: packet数据类型，是一个list
    :param dst:
    :param src:
    :return:
    '''
    packet_list = pcap.getPacket()
    ip_list = list()
    for packet in packet_list:
        temp_eth = ethernet(packet)
        if temp_eth.getType() == 'ETH_TYPE_IP':
            temp_ip = ip(temp_eth)
            if temp_ip.getDst() == dst:
                if temp_ip.getSrc() == src:
                    if temp_ip.getID():
                        # TODO
                        pass


def followTCPstream(ip):
    pass
