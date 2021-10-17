from dataclasses import dataclass


@dataclass
class AccessPoint():
    mac: str
    ssid: str
    channel: str