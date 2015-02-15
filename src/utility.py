# -*- encoding=cp936 -*-

__author__ = 'Reuynil'

from input import *
from ethernet import *
from ip import *


def testBit(int_data, offset):
    '''
    测试某一位是否为1
    :param int_data: int类型的数据
    :param offset: 要测试的位，最高位为7
    :return:是1的时候返回True
    '''
    mask = 0b00000001 << offset
    return bool(int_data & mask)


def byteToInt(byte_data):
    return int(byte_data.encode('hex'), 16)


def reassembleIP(pcap):
    '''

    :param packet_list: packet数据类型，是一个list
    :param dst:
    :param src:
    :return:
    '''
    res = list()
    work_list = dict()
    packet_list = pcap.getPacket()
    ip_list = list()
    for packet in packet_list:
        temp_eth = ethernet(packet)
        if temp_eth.getType() == 'ETH_TYPE_IP':  # 判断是不是ip数据报
            temp_ip = ip(temp_eth)
            if temp_ip.checkSum() == True:  # 判断ip数据报是不是有错误
                if temp_ip.fragment() == True:
                    temp_ip_id = temp_ip.getID()
                    if work_list.has_key(temp_ip_id):
                        work_list[temp_ip_id].append(temp_ip)
                    else:
                        value = list()
                        value.append(temp_ip)
                        work_list[temp_ip_id] = value
                else:  #不能分片
                    temp_ip_id = temp_ip.getID()
                    res["temp_ip_id"] = temp_ip  #TODO：改成ipDatagram类型的。

    for key, value in work_list:
        if len(work_list[key]) == 1:
            res[work_list[key].getID()] = work_list[key]  # TODO:SAME WITH BEFORE
        else:
            pass


def followTCPstream(ip):
    pass
