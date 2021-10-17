from subprocess import run


def monitor_mode(interface: str):
    """
    Set network interface in monitor mode
    """
    run(["systemctl", "stop", "NetworkManager"])
    run(["ifconfig", interface, "down"])
    run(["iwconfig", interface, "mode", "monitor"])
    run(["ifconfig", interface, "up"])


def managed_mode(interface: str):
    """
    Set network interface in managed mode
    """
    run(["ifconfig", interface, "down"])
    run(["iwconfig", interface, "mode", "managed"])
    run(["ifconfig", interface, "up"])
    run(["systemctl", "start", "NetworkManager"])


def hop_channel(interface: str, channel: int):
    """
    Set network interface channel
    """
    run(["iwconfig", interface, "channel", str(channel)])
