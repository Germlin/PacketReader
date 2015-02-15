# -*- encoding=cp936 -*-

__author__ = 'Reuynil'

from input import *
from ethernet import *
from ip import *


def testBit(int_data, offset):
    '''
    ����ĳһλ�Ƿ�Ϊ1
    :param int_data: int���͵�����
    :param offset: Ҫ���Ե�λ�����λΪ7
    :return:��1��ʱ�򷵻�True
    '''
    mask = 0b00000001 << offset
    return bool(int_data & mask)


def byteToInt(byte_data):
    return int(byte_data.encode('hex'), 16)


def reassembleIP(pcap):
    '''

    :param packet_list: packet�������ͣ���һ��list
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
        if temp_eth.getType() == 'ETH_TYPE_IP':  # �ж��ǲ���ip���ݱ�
            temp_ip = ip(temp_eth)
            if temp_ip.checkSum() == True:  # �ж�ip���ݱ��ǲ����д���
                if temp_ip.fragment() == True:
                    temp_ip_id = temp_ip.getID()
                    if work_list.has_key(temp_ip_id):
                        work_list[temp_ip_id].append(temp_ip)
                    else:
                        value = list()
                        value.append(temp_ip)
                        work_list[temp_ip_id] = value
                else:  #���ܷ�Ƭ
                    temp_ip_id = temp_ip.getID()
                    res["temp_ip_id"] = temp_ip  #TODO���ĳ�ipDatagram���͵ġ�

    for key, value in work_list:
        if len(work_list[key]) == 1:
            res[work_list[key].getID()] = work_list[key]  # TODO:SAME WITH BEFORE
        else:
            pass


def followTCPstream(ip):
    pass
