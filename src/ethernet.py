# -*- encoding=utf-8 -*-

from utility import *
from pcapreader import *
import base64

__author__ = 'Reuynil'

# Ethernet payload types - http://standards.ieee.org/regauth/ethertype
ETH_TYPE_PUP = 0x0200  # PUP protocol
ETH_TYPE_IP = 0x0800  # IP protocol
ETH_TYPE_ARP = 0x0806  # address resolution protocol
ETH_TYPE_AOE = 0x88a2  # AoE protocol
ETH_TYPE_CDP = 0x2000  # Cisco Discovery Protocol
ETH_TYPE_DTP = 0x2004  # Cisco Dynamic Trunking Protocol
ETH_TYPE_REVARP = 0x8035  # reverse addr resolution protocol
ETH_TYPE_8021Q = 0x8100  # IEEE 802.1Q VLAN tagging
ETH_TYPE_IPX = 0x8137  # Internetwork Packet Exchange
ETH_TYPE_IP6 = 0x86DD  # IPv6 protocol
ETH_TYPE_PPP = 0x880B  # PPP
ETH_TYPE_MPLS = 0x8847  # MPLS
ETH_TYPE_MPLS_MCAST = 0x8848  # MPLS Multicast
ETH_TYPE_PPPoE_DISC = 0x8863  # PPP Over Ethernet Discovery Stage
ETH_TYPE_PPPoE = 0x8864  # PPP Over Ethernet Session Stage
ETH_TYPE_LLDP = 0x88CC  # Link Layer Discovery Protocol


class ethernet:
    def __init__(self, packet):
        self.__data = packet.getData()
        self.dst = self.__data[0:6]
        self.src = self.__data[6:12]
        self.type = self.__data[12:14]

    def getDst(self):
        s = list()
        for i in range(6):
            s.append(base64.b16encode(self.dst[i:i + 1]))
        return str(b":".join(s))[2:-1]

    def getSrc(self):
        s = list()
        for i in range(6):
            s.append(base64.b16encode(self.src[i:i + 1]))
        return str(b":".join(s))[2:-1]

    def getType(self):
        g = globals()
        for k, v in list(g.items()):
            if k.startswith('ETH_TYPE_') and v == int.from_bytes(self.type, byteorder='big', signed=False):
                return k
        return None

    def getData(self):
        return self.__data[14:]
