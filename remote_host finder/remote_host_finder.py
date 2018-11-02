"""

This program is made for educational purpose,
This program is find host's Ipv4 addr which are in other networks.
you can use it, if you find other network's hosts or must know their ip addr.

This Progrma is made By Nicht. Lee Joon Sung

(C) 2018 copyright by nicht, Kbu 1822021

"""

import socket

def get_remote_host_addr():

    # interface start
    print "+==================================================================+"
    print "+                         Ipv4 Addr finder                         +"
    print "+                                                                  +"
    print "+                                             for remote  hosts    +"
    print "+                                                                  +"
    print "+                                                                  +"
    print "+              (C) 2018 copyright by nicht, Kbu 1822021            +"
    print "+==================================================================+\n"

    print "[+] ", "type url which you want to know their ipv4 addr"
    print "[+] ", "this program will be print ipv4 addr which are you typed.\n"
   # interface end

    #store the url addres at 'remote_host'
    remote_hosts =raw_input("Type URL and enter !:\n")

    try:
        print "[+]", "find target ipv4 addr !"
        print "[+]", "IP address of %s : %s" %(remote_hosts, socket.gethostbyname(remote_hosts))

    except socket.error, err_msg:
        print "[-]", " Can't find target ipv4 addr !"
        print "[-]", "%s : %s" %(remote_hosts, err_msg)


if __name__ == '__main__':
    print get_remote_host_addr()