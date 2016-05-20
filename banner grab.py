import socket
import datetime

ports = {"http" : 80, "https" : 443, "ftp" : 21, "telnet" : 23,}

"""
Generic banner grab script.
"""
def bannergrab(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        print "[+] Connection to " + ip + "," + "port" + " " + str(port) + ", " + "Succeeded!"
        print "output: " + str(banner)
        print "**********************************************************"
        return banner
    except Exception, e:
        print "[-] Connection to " + "," + ip + "," + "port" + " " + str(port) + ", " + "Failed"
        print "[-] Error = " + str(e)
        print "**********************************************************"
        return str(e) #returns error message | Always remember to return you n00b

def http(ip,port):
    try:
        socket.setdefaulttimeout(2)
        a = socket.socket()
        a.connect((ip,port))
        socket.send("GET HTTP/1.1 \r\n")
        giveMeUrInfoz = socket.recv(1024)
        print "[+]" + "Huzzah! " + str(giveMeUrInfoz)
        print "**********************************************************"
        return giveMeUrInfoz
    except Exception, e:
        print "[-] Unable to grab info" + str(e)
        print "**********************************************************"
        return str(e)

def main(ip):
    counter = 0
    for tgt in ports:
        if ports[tgt] == "80":
            output_http = http(ip, 80)
            print output_http
            with open("recon.txt", "a") as haha:
                haha.write("port: " + str(ports[tgt]) + "|" + str(output_http) + "\n")
                haha.write("**********************************\n")
            counter += 1
        else:
            output = bannergrab(ip, ports[tgt])
            with open("recon.txt", "a") as haha:
                haha.write("port: " + str(ports[tgt]) + "|" + str(output) + "\n")
                haha.write("**********************************\n\n")
            counter += 1
    if counter == 4:
        with open("recon.txt", "a") as haha:
            haha.write("++++++++++++++++++++++++++++++++++++++Scan complete+++++++++++++++++++++++++++++++++++++" + "\n")
            haha.close()
    #print counter

if __name__=='__main__':
    ip = "192.168.239.128"
    main(ip)

