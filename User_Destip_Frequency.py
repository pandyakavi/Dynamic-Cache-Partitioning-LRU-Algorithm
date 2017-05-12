import csv
import sys

a = open("Feb_23_dstip_freq_descending.txt","r+")
f = open("FGTADOM3_wlog_from_2017-02-23_00_08_00_to_.csv","rt")
z = open("Feb_23_all.txt","w+")

b = a.read()
b = b.split("\n")
c = f.read()
c = c.split("\n")

ip2 = []
host = []
for i in range(153282,323418):
	ip_2 = c[i].split(",")[14]
	host_1 = c[i].split(",")[19]
	ip2.append(ip_2)
	host.append(host_1)


for i in range(0,len(b)-1):
	freq = b[i].split(" ")[0]
	ip = b[i].split(" ")[1]
	ip_index = ip2.index(ip)
	hostname = host[ip_index]
	print freq
	print ip
	print hostname
	z.write(freq)
	z.write("\t")
	z.write(ip)
	z.write("\t")
	z.write(hostname)
	z.write("\n")
#print ip2
#print len(host)
