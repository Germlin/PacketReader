# -*- encoding=utf-8 -*-

from PyPcap.packet import *
from PyPcap.pcap import Pcap, Packet

# Ethernet payload types - http://standards.ieee.org/regauth/ethertype
ETH_TYPE = {
    'ETH_TYPE_PUP': 0x0200,  # PUP protocol
    'ETH_TYPE_IP': 0x0800,  # IP protocol
    'ETH_TYPE_ARP': 0x0806,  # address resolution protocol
    'ETH_TYPE_AOE': 0x88a2,  # AoE protocol
    'ETH_TYPE_CDP': 0x2000,  # Cisco Discovery Protocol
    'ETH_TYPE_DTP': 0x2004,  # Cisco Dynamic Trunking Protocol
    'ETH_TYPE_REVARP': 0x8035,  # reverse addr resolution protocol
    'ETH_TYPE_8021Q': 0x8100,  # IEEE 802.1Q VLAN tagging
    'ETH_TYPE_IPX': 0x8137,  # Internetwork Packet Exchange
    'ETH_TYPE_IP6': 0x86DD,  # IPv6 protocol
    'ETH_TYPE_PPP': 0x880B,  # PPP
    'ETH_TYPE_MPLS': 0x8847,  # MPLS
    'ETH_TYPE_MPLS_MCAST': 0x8848,  # MPLS Multicast
    'ETH_TYPE_PPPoE_DISC': 0x8863,  # PPP Over Ethernet Discovery Stage
    'ETH_TYPE_PPPoE': 0x8864,  # PPP Over Ethernet Session Stage
    'ETH_TYPE_LLDP': 0x88CC,  # Link Layer Discovery Protocol'''
}


class EthernetPacket(BasicPacket):
    _Ethernet_header_structure_ = (
        ('destination', '6B', 6),
        ('source', '6B', 6),
        ('type', 'H', 2),
    )

    def __init__(self, packet):
        if packet.link_type != 0x01:
            raise PacketTypeError()
        else:
            super(EthernetPacket, self).__init__(self._Ethernet_header_structure_)
            self._parse_header_(packet.data[0:self._header_length_])
            self.data = packet.data[self._header_length_:]

    def fmt_dst(self):
        s = list()
        for i in self.header['destination']:
            s.append(hex(i)[2:])
        return str(":".join(s))

    def fmt_src(self):
        s = list()
        for i in self.header['source']:
            s.append(hex(i)[2:])
        return str(":".join(s))

    def fmt_type(self):
        for (k, v) in ETH_TYPE.items():
            if v == self.header['type']:
                return k
        return Exception("Unknown type.")


class Ethernet:
    def __init__(self, pcap_file):
        assert type(pcap_file) == Pcap
        self.packets = {}
        for p in pcap_file.packets:
            try:
                ep = EthernetPacket(p)
            except PacketTypeError:
                pass
            else:
                #k = (ep.fmt_src(), ep.fmt_dst(), ep.fmt_type())
                k=(ep.header['source'],ep.header['destination'],ep.header['type'])
                if k not in self.packets.keys():
                    v = [ep]
                    self.packets[k] = v
                else:
                    self.packets[k].append(ep)

    def filter(self, **kwargs):
        res = {}
        for (epk, epv) in self.packets.items():
            flag = True
            for (k, v) in kwargs.items():
                if k == 'SRC_MAC':
                    flag = flag and epk[0] == v
                elif k == 'DST_MAC':
                    flag = flag and epk[1] == v
                elif k == 'TYPE':
                    flag = flag and epk[2] == v
                else:
                    flag = False
            if flag:
                res[epk] = epv
        return res
