from scapy.all import *
from threading import Thread
import pandas
import time
import os
import sys

y = 1
x = 250
while (y > 0):
    y = y - 1
    print (x)
    # initialize the networks dataframe that will contain all access points nearby
    networks = pandas.DataFrame(columns=["Mac Address", "SSID", "Channel"]) # "SeCuRiTy"
    # set the index BSSID (MAC address of the AP)
    networks.set_index("Mac Address", inplace=True)

    def callback(packet):
        global x
        
        #while (x > 0):
        #x = x - 1
        if x > 0:
            x = x - 1
            if packet.haslayer(Dot11Beacon) :
                
                # extract the MAC address of the network
                bssid = packet[Dot11].addr2
                # get the name of it
                ssid = packet[Dot11Elt].info.decode()
                try:
                    dbm_signal = packet.dBm_AntSignal
                except:
                    dbm_signal = "N/A"
                # extract network stats
                stats = packet[Dot11Beacon].network_stats()
                 # get the channel of the AP
                channel = stats.get("channel")
                # get the crypto
                crypto = stats.get("crypto")
                networks.loc[bssid] = ([ssid], channel) # crypto
                print (x)
                #sys.exit()
                #if x == 0:
                #    break
        else:
            sys.exit()

    def print_all():
        global x
        x = x - 1
        while True:
            os.system("clear")
            print(networks)
            time.sleep(0.5)
            
            #if x == 0:
            #    break
            

    def change_channel():
        ch = 1
        while True:
            os.system(f"iwconfig {interface} channel {ch}")
            # switch channel from 1 to 14 each 0.5s
            ch = ch % 14 + 1
            time.sleep(0.5)


    if __name__ == "__main__":
        # interface name, check using iwconfig
        interface = "wlan0mon"
        # start the thread that prints all the networks
        printer = Thread(target=print_all)
        printer.daemon = True
        printer.start()
        # start the channel changer
        channel_changer = Thread(target=change_channel)
        channel_changer.daemon = True
        channel_changer.start()
        # start sniffing
        sniff(prn=callback, iface=interface)
