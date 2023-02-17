PacketReader
============

A ``pcap`` file parser implemented by Python. ``libpcap`` is not needed for this package.

Installation
------------

::

  pip install PacketReader

Usage
-----

1. Import module.
::

  import PacketReader

2. Read from a pcap file. ``read_pcap`` return a list of packets.
::

  packets = PacketReader.read_pcap(pcap_file)

3. You can print the information of each packet.
::

  print(packets[0])

4. PacketReader supports IP/TCP/UDP. You can get the MAC address, IP address and flags of packets.
::

    print(packets[0].mac_address)
    print(packets[0].tcp_header['SYN'])


Example
-------
::

    >>> import PacketReader
    >>> pl=PacketReader.read_pcap('test.pcap')
    >>> print(len(pl))
    179
    >>> print(pl[0])
    Packet 1 Information:
    [1] Epoch Time: 1448157839.796592 seconds
    [2] Frame Length: 85 bytes
    [3] Destination Mac Address: 28:C2:DD:1D:75:C1
    [4] Source Mac Address: 88:25:93:37:60:84
    [5] Destination IP Address: 192.168.1.183
    [6] Source IP Address: 192.30.252.88
    [7] Destination Port: 57747
    [8] Source Port :443
    [9] Protocol: 6
