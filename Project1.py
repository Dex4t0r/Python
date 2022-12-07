from socket import *
def conScan(tgHost, tgPort):
    try:
        connect = socket(AF_INET, SOCK_STREAM)
        connect.connect((tgHost, tgPort))
        print("[+]%d/tcp open"% tgPort)
        connect.close()
    except:
        print("[-]%d/tcp closed"% tgPort)
def portScan(tgHost, tgPorts):
    try:
        tgtIP = gethostbyname(tgHost)
    except:
        print('[-] Cannot resolve %d "% tgPort')
        return
    try:
        tgtname = gethostbyaddr(tgtIP)
        print('/n[-] scan result of: %d "% tgname[0]')
    except:
         print('/n[-] scan result of: %d "% tgIP[0]')
    setdefaulttimeout(1)
    for tgPort in tgPorts:
        print('Scanning Port: %d'% tgPort)
        conScan(tgHost, int(tgPort))
if __name__ == '__main__':
    portScan("site.com", [80, 22])
    
