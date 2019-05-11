# -*- coding: utf-8 -*-

import nmap


def port_scan():
    print ("---------------单线程端口扫描-----------------")
    nm = nmap.PortScanner()
    nm.scan(hosts="192.168.199.1/24", ports="21-80")
    for host in nm.all_hosts():
        print ("Host : %s (%s)" % (host, nm[host].hostname()))
        print ("\tState : %s " % nm[host].state())
        for protocol in nm[host].all_protocols():
            print ("\t\tProtocols : %s " % protocol)
            prots = nm[host][protocol].keys()
            prots.sort()
            for prot in prots:
                print ("\t\tProt : %s  \t state : %s " % (prot, nm[host][protocol][int(prot)]['state']))


def port_state():
    print ("---------------在线主机扫描-----------------")
    nm_sp = nmap.PortScanner()
    nm_sp.scan(hosts="192.168.199.1/24", arguments="-sP")
    hosts_list = [(x, nm_sp[x]['status']['state']) for x in nm_sp.all_hosts()]
    for host, statu in hosts_list:
        print (host, " : ", statu)


def call_back():
    return "pass"


def port_scan_async():
    print ("---------------多线程端口扫描-----------------")
    nmaps = nmap.PortScannerAsync()
    nmaps.scan(hosts="192.168.199.1/24", ports="21-80", callback=call_back, sudo=False)
    for host_list in nmaps.all_hosts():
        print ("Host : %s (%s)" % (host_list, nmaps[host_list].hostname()))
        print ("State : %s " % nmaps[host_list].state())
        for protocols in nmaps[host_list].all_protocols():
            print ("\tProtocols : %s " % protocols)
            prots_list = nmaps[host_list][protocols].keys()
            prots_list.sort()
            for prots in prots_list:
                print ("\t\tProt : %s  \t state : %s " % (prots, nmaps[host_list][protocols][int(prots)]['state']))


if __name__ == "__main__":
    port_scan()
    port_state()
