# -*- encoding=cp936 -*-

__author__ = 'Reuynil'

from utility import *
from ethernet import *

# Protocol (ip_p) - http://www.iana.org/assignments/protocol-numbers
IP_PROTO_IP = 0  # dummy for IP
IP_PROTO_HOPOPTS = IP_PROTO_IP  # IPv6 hop-by-hop options
IP_PROTO_ICMP = 1  # ICMP
IP_PROTO_IGMP = 2  # IGMP
IP_PROTO_GGP = 3  # gateway-gateway protocol
IP_PROTO_IPIP = 4  # IP in IP
IP_PROTO_ST = 5  # ST datagram mode
IP_PROTO_TCP = 6  # TCP
IP_PROTO_CBT = 7  # CBT
IP_PROTO_EGP = 8  # exterior gateway protocol
IP_PROTO_IGP = 9  # interior gateway protocol
IP_PROTO_BBNRCC = 10  # BBN RCC monitoring
IP_PROTO_NVP = 11  # Network Voice Protocol
IP_PROTO_PUP = 12  # PARC universal packet
IP_PROTO_ARGUS = 13  # ARGUS
IP_PROTO_EMCON = 14  # EMCON
IP_PROTO_XNET = 15  # Cross Net Debugger
IP_PROTO_CHAOS = 16  # Chaos
IP_PROTO_UDP = 17  # UDP
IP_PROTO_MUX = 18  # multiplexing
IP_PROTO_DCNMEAS = 19  # DCN measurement
IP_PROTO_HMP = 20  # Host Monitoring Protocol
IP_PROTO_PRM = 21  # Packet Radio Measurement
IP_PROTO_IDP = 22  # Xerox NS IDP
IP_PROTO_TRUNK1 = 23  # Trunk-1
IP_PROTO_TRUNK2 = 24  # Trunk-2
IP_PROTO_LEAF1 = 25  # Leaf-1
IP_PROTO_LEAF2 = 26  # Leaf-2
IP_PROTO_RDP = 27  # "Reliable Datagram" proto
IP_PROTO_IRTP = 28  # Inet Reliable Transaction
IP_PROTO_TP = 29  # ISO TP class 4
IP_PROTO_NETBLT = 30  # Bulk Data Transfer
IP_PROTO_MFPNSP = 31  # MFE Network Services
IP_PROTO_MERITINP = 32  # Merit Internodal Protocol
IP_PROTO_SEP = 33  # Sequential Exchange proto
IP_PROTO_3PC = 34  # Third Party Connect proto
IP_PROTO_IDPR = 35  # Interdomain Policy Route
IP_PROTO_XTP = 36  # Xpress Transfer Protocol
IP_PROTO_DDP = 37  # Datagram Delivery Proto
IP_PROTO_CMTP = 38  # IDPR Ctrl Message Trans
IP_PROTO_TPPP = 39  # TP++ Transport Protocol
IP_PROTO_IL = 40  # IL Transport Protocol
IP_PROTO_IP6 = 41  # IPv6
IP_PROTO_SDRP = 42  # Source Demand Routing
IP_PROTO_ROUTING = 43  # IPv6 routing header
IP_PROTO_FRAGMENT = 44  # IPv6 fragmentation header
IP_PROTO_RSVP = 46  # Reservation protocol
IP_PROTO_GRE = 47  # General Routing Encap
IP_PROTO_MHRP = 48  # Mobile Host Routing
IP_PROTO_ENA = 49  # ENA
IP_PROTO_ESP = 50  # Encap Security Payload
IP_PROTO_AH = 51  # Authentication Header
IP_PROTO_INLSP = 52  # Integated Net Layer Sec
IP_PROTO_SWIPE = 53  # SWIPE
IP_PROTO_NARP = 54  # NBMA Address Resolution
IP_PROTO_MOBILE = 55  # Mobile IP, RFC 2004
IP_PROTO_TLSP = 56  # Transport Layer Security
IP_PROTO_SKIP = 57  # SKIP
IP_PROTO_ICMP6 = 58  # ICMP for IPv6
IP_PROTO_NONE = 59  # IPv6 no next header
IP_PROTO_DSTOPTS = 60  # IPv6 destination options
IP_PROTO_ANYHOST = 61  # any host internal proto
IP_PROTO_CFTP = 62  # CFTP
IP_PROTO_ANYNET = 63  # any local network
IP_PROTO_EXPAK = 64  # SATNET and Backroom EXPAK
IP_PROTO_KRYPTOLAN = 65  # Kryptolan
IP_PROTO_RVD = 66  # MIT Remote Virtual Disk
IP_PROTO_IPPC = 67  # Inet Pluribus Packet Core
IP_PROTO_DISTFS = 68  # any distributed fs
IP_PROTO_SATMON = 69  # SATNET Monitoring
IP_PROTO_VISA = 70  # VISA Protocol
IP_PROTO_IPCV = 71  # Inet Packet Core Utility
IP_PROTO_CPNX = 72  # Comp Proto Net Executive
IP_PROTO_CPHB = 73  # Comp Protocol Heart Beat
IP_PROTO_WSN = 74  # Wang Span Network
IP_PROTO_PVP = 75  # Packet Video Protocol
IP_PROTO_BRSATMON = 76  # Backroom SATNET Monitor
IP_PROTO_SUNND = 77  # SUN ND Protocol
IP_PROTO_WBMON = 78  # WIDEBAND Monitoring
IP_PROTO_WBEXPAK = 79  # WIDEBAND EXPAK
IP_PROTO_EON = 80  # ISO CNLP
IP_PROTO_VMTP = 81  # Versatile Msg Transport
IP_PROTO_SVMTP = 82  # Secure VMTP
IP_PROTO_VINES = 83  # VINES
IP_PROTO_TTP = 84  # TTP
IP_PROTO_NSFIGP = 85  # NSFNET-IGP
IP_PROTO_DGP = 86  # Dissimilar Gateway Proto
IP_PROTO_TCF = 87  # TCF
IP_PROTO_EIGRP = 88  # EIGRP
IP_PROTO_OSPF = 89  # Open Shortest Path First
IP_PROTO_SPRITERPC = 90  # Sprite RPC Protocol
IP_PROTO_LARP = 91  # Locus Address Resolution
IP_PROTO_MTP = 92  # Multicast Transport Proto
IP_PROTO_AX25 = 93  # AX.25 Frames
IP_PROTO_IPIPENCAP = 94  # yet-another IP encap
IP_PROTO_MICP = 95  # Mobile Internet Ctrl
IP_PROTO_SCCSP = 96  # Semaphore Comm Sec Proto
IP_PROTO_ETHERIP = 97  # Ethernet in IPv4
IP_PROTO_ENCAP = 98  # encapsulation header
IP_PROTO_ANYENC = 99  # private encryption scheme
IP_PROTO_GMTP = 100  # GMTP
IP_PROTO_IFMP = 101  # Ipsilon Flow Mgmt Proto
IP_PROTO_PNNI = 102  # PNNI over IP
IP_PROTO_PIM = 103  # Protocol Indep Multicast
IP_PROTO_ARIS = 104  # ARIS
IP_PROTO_SCPS = 105  # SCPS
IP_PROTO_QNX = 106  # QNX
IP_PROTO_AN = 107  # Active Networks
IP_PROTO_IPCOMP = 108  # IP Payload Compression
IP_PROTO_SNP = 109  # Sitara Networks Protocol
IP_PROTO_COMPAQPEER = 110  # Compaq Peer Protocol
IP_PROTO_IPXIP = 111  # IPX in IP
IP_PROTO_VRRP = 112  # Virtual Router Redundancy
IP_PROTO_PGM = 113  # PGM Reliable Transport
IP_PROTO_ANY0HOP = 114  # 0-hop protocol
IP_PROTO_L2TP = 115  # Layer 2 Tunneling Proto
IP_PROTO_DDX = 116  # D-II Data Exchange (DDX)
IP_PROTO_IATP = 117  # Interactive Agent Xfer
IP_PROTO_STP = 118  # Schedule Transfer Proto
IP_PROTO_SRP = 119  # SpectraLink Radio Proto
IP_PROTO_UTI = 120  # UTI
IP_PROTO_SMP = 121  # Simple Message Protocol
IP_PROTO_SM = 122  # SM
IP_PROTO_PTP = 123  # Performance Transparency
IP_PROTO_ISIS = 124  # ISIS over IPv4
IP_PROTO_FIRE = 125  # FIRE
IP_PROTO_CRTP = 126  # Combat Radio Transport
IP_PROTO_CRUDP = 127  # Combat Radio UDP
IP_PROTO_SSCOPMCE = 128  # SSCOPMCE
IP_PROTO_IPLT = 129  # IPLT
IP_PROTO_SPS = 130  # Secure Packet Shield
IP_PROTO_PIPE = 131  # Private IP Encap in IP
IP_PROTO_SCTP = 132  # Stream Ctrl Transmission
IP_PROTO_FC = 133  # Fibre Channel
IP_PROTO_RSVPIGN = 134  # RSVP-E2E-IGNORE
IP_PROTO_RAW = 255  # Raw IP packets
IP_PROTO_RESERVED = IP_PROTO_RAW  # Reserved
IP_PROTO_MAX = 255


class ip:
    def __init__(self, eth):
        """
        初始化函数。
        :param eth: type: ethernet(defined in ethernet.py)
        :return: nothing
        """
        assert isinstance(eth, ethernet)
        self.__data = eth.getData()
        self.fields = {"version": None,
                       "HeaderLength": getFiled(self.__data, 0, 4, 4) * 4,
                       "DSCP": None,
                       "ECN": None,
                       "TotalLength": getFiled(self.__data, 2, 0, 16),
                       "Identification": getFiled(self.__data, 4, 0, 16),
                       "Flags": None,
                       "FragmentOffset": getFiled(self.__data, 6, 3, 13) * 8,
                       "TTL": None,
                       "Protocol": getFiled(self.__data, 9, 0, 8),
                       "Checksum": getFiled(self.__data, 10, 0, 8),
                       "SourceIP": self.__data[12:16],
                       "DestinationIP": self.__data[16:20],
                       "Options": None}

    def getDst(self):
        s = list()
        for i in range(4):
            s.append(str(int(base64.b16encode(self.fields["DestinationIP"][i:i + 1]), 16)))
        return ".".join(s)

    def getSrc(self):
        s = list()
        for i in range(4):
            s.append(str(int(base64.b16encode(self.fields["SourceIP"][i:i + 1]), 16)))
        return ".".join(s)

    def getProtocol(self):
        g = globals()
        for k, v in list(g.items()):
            if k.startswith('IP_PROTO_') and v == self.fields["Protocol"]:
                return k
        return None

    def getData(self):
        return self.__data[self.fields["HeaderLength"]:]

    def getID(self):
        return self.fields["Identification"]

    def getTotalLength(self):
        return self.fields["TotalLength"]

    def getHeaderLength(self):
        return self.fields["HeaderLength"]

    def getOffset(self):
        return self.fields["FragmentOffset"]

    def checkSum(self):
        check_sum = 0
        i = 0
        while i < self.fields["HeaderLength"]:
            check_sum += getFiled(self.__data, i, 0, 16)
            i += 2
        check_sum = (check_sum >> 16) + (check_sum & 0xffff)
        return check_sum == 0xffff

    def fragment(self):
        """
        判断ip数据报是否可以分片
        :return:True代表可以分片，False代表不可以分片
        """
        Flag = int(base64.b16encode(self.__data[6:7]), 16)
        return not testBit(Flag, 6)

    def moreFragment(self):
        """
        判断ip数据报是不是最后一个分片
        :return:True是最后一个分片，False不是最后一个分片
        """
        Flag = int(base64.b16encode(self.__data[6:7]), 16)
        return testBit(Flag, 5)


class ipDatagram:
    def __init__(self, dst, src, protocol, data):
        self.dst = dst
        self.src = src
        self.protocol = protocol
        self.data = data


def reassembleIP(pcap):
    """

    :param pcap:
    :return:
    """
    assert isinstance(pcap, PcapFile)
    res = list()
    work_list = dict()
    packet_list = pcap.getPacket()
    for packet in packet_list:
        temp_eth = ethernet(packet)
        if temp_eth.getType() == 'ETH_TYPE_IP':  # 判断是不是ip数据报
            temp_ip = ip(temp_eth)
            if temp_ip.checkSum() or temp_ip.fields["Checksum"] == 0:  # 判断ip数据报是不是有错误
                if temp_ip.fragment():
                    temp_ip_id = temp_ip.getID()
                    if temp_ip_id in work_list:
                        work_list[temp_ip_id].append(temp_ip)
                    else:
                        value = list()
                        value.append(temp_ip)
                        work_list[temp_ip_id] = value
                else:  # 不能分片
                    res.append(ipDatagram(temp_ip.getDst(), temp_ip.getSrc(), temp_ip.getProtocol(), temp_ip.getData()))

    # The idea of the algorithm is from RFC815
    for key in work_list:
        temp_ip_list = work_list[key]
        temp_dst = temp_ip_list[0].getDst()
        temp_src = temp_ip_list[0].getSrc()
        temp_protocol = temp_ip_list[0].getProtocol()
        temp_data = dict()
        hole_descriptor_list = list()
        hole_descriptor_list.append(dict(first=0, last=1048576))
        for fragment in temp_ip_list:
            assert isinstance(fragment, ip)
            fragment_first = fragment.getOffset()
            fragment_last = fragment.getOffset() + (fragment.getTotalLength() - fragment.getHeaderLength())
            for hole in hole_descriptor_list:
                hole_first = hole["first"]
                hole_last = hole["last"]
                if fragment_first <= hole_last and fragment_last >= hole_first:
                    hole_descriptor_list.remove(hole)
                    temp_data[fragment_first] = fragment.getData()
                    if fragment_first > hole_first:
                        new_hole = dict(first=hole_first, last=fragment_first - 1)
                        hole_descriptor_list.append(new_hole)
                    if fragment_last < hole_last and fragment.moreFragment():
                        new_hole = dict(first=fragment_last + 1, last=hole_last)
                        hole_descriptor_list.append(new_hole)
        if len(hole_descriptor_list) == 0:
            data = b''
            for k in sorted(temp_data.keys()):
                data = data + temp_data[k]
            res.append(ipDatagram(temp_dst, temp_src, temp_protocol, data))
        else:
            raise Exception("lost IP packet.")
    return res
